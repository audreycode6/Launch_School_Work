import unittest
import shutil
import os
from app import app

'''import functions you want to test 
+ funcs start with test '''
class FileCMSTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.data_path = os.path.join(os.path.dirname(__file__), 'data')
        # creates directory specified by self.data_path
        os.makedirs(self.data_path, exist_ok=True)

    def tearDown(self):
        # deletes the entire directory & contents specified by self.data_path
        shutil.rmtree(self.data_path, ignore_errors=True)

    def admin_session(self): # TODO figure out what needs to change when using user.yaml
        # simulate user signed in
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = "admin"
            return c
        
    def create_document(self, name, content=''):
        with open(os.path.join(self.data_path, name), 'w') as file:
            file.write(content)

    def test_get_file_contents(self):
        self.create_document('changes.txt', "There are many changes.")

        with self.client.get("/changes.txt") as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "text/plain; charset=utf-8")
            self.assertEqual("There are many changes.", response.get_data(as_text=True))

    def test_file_not_found(self):
        # assert if non existing file is in path then it results in a redirect
        with self.client.get("/notafile.txt") as response:
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, "/")

        # assert that the redirect is successful and flash message appears
        with self.client.get(response.headers["Location"]) as response:
            self.assertEqual(response.status_code, 200)
            self.assertIn("notafile.txt does not exist.", response.get_data(as_text=True))

        # assert that flash message is cleared when reloaded
        with self.client.get("/") as response:
            self.assertNotIn("notafile.txt does not exist.", response.get_data(as_text=True))

    def test_md_file_as_html(self):
        self.create_document('about.md', '# Welcome')

        with self.client.get("/about.md") as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "text/html; charset=utf-8")
            self.assertIn("<h1>Welcome</h1>", response.get_data(as_text=True))

    def test_edit_file(self):
        self.admin_session()
        self.create_document('changes.txt', "There are many changes.")

        # assert that edit link works and containts content from 
        with self.client.get("/changes.txt/edit") as response:
            self.assertEqual(response.status_code, 200)
            self.assertIn("Edit content of changes.txt", response.get_data(as_text=True))
            self.assertIn("There are many changes.", response.get_data(as_text=True)) 
        
    def test_submit_edit(self):
        self.admin_session()
        self.create_document('changes.txt')
        # assert post request results in redirect to "/" 
        with self.client.post(
            "/changes.txt", 
            data={"content": "There are many changes."},
            follow_redirects=False
            ) as response:
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, "/")

        # assert flash message works
        with self.client.get("/", follow_redirects=True) as response:
            self.assertIn("changes.txt has been updated.", response.get_data(as_text=True))

        # assert flash message clears after refresh
        with self.client.get("/") as response:
            self.assertNotIn("changes.txt has been updated.", response.get_data(as_text=True))

    def test_new(self):
        self.admin_session()
        with self.client.get('/new') as response:
            self.assertEqual(response.status_code, 200)
            self.assertIn("Add a new document:", response.get_data(as_text=True))

    def test_new_file_submission(self):
        self.admin_session()
        with self.client.post("/new", data={'file_name': "test.txt"}) as response:
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, "/")
        
        with self.client.get('/') as response:
            self.assertIn("test.txt was created", response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)

    def test_no_name_file_submission(self):
        self.admin_session()
        with self.client.post('/new', data={'file_name': ''}) as response:
            self.assertEqual(response.status_code, 422)
            self.assertIn("A name is required", response.get_data(as_text=True))

    def test_file_name_exists_submission(self):
        self.admin_session()
        self.create_document("foo")

        with self.client.post('/new', data={'file_name': 'foo'}) as response:
            self.assertEqual(response.status_code, 422)
            self.assertIn("foo already exists", response.get_data(as_text=True))

    def test_delete_file(self):
        self.admin_session()
        self.create_document("file_to_delete.ext")

        with self.client.post("/file_to_delete.ext/delete", follow_redirects=True) as response:
            self.assertEqual(response.status_code, 200)
            self.assertIn("file_to_delete.ext has been deleted", response.get_data(as_text=True))

        with self.client.get("/") as response: # make sure file is deleted from index
            self.assertNotIn("file_to_delete.ext", response.get_data(as_text=True))

    def test_delete_non_existent_file(self):
        self.admin_session()
        with self.client.post("/nada.ext/delete") as response:
            self.assertEqual(response.status_code, 422)
            self.assertIn("nada.ext does not exist", response.get_data(as_text=True))

    def test_index_signed_out(self):
        self.create_document("file.ext")

        with self.client.get("/") as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "text/html; charset=utf-8")
            self.assertIn('Sign In', response.get_data(as_text=True))

    def test_signin_form(self):
        with self.client.get("/users/signin") as response:
            self.assertEqual(response.status_code, 200)
            self.assertIn("Username", response.get_data(as_text=True))
            self.assertIn("Sign In", response.get_data(as_text=True))

    def test_success_sign_in_and_out(self):
        with self.client.post(
            "/users/signin", 
            data={"username":"admin", "password":"secret"}, follow_redirects=True
            ) as response:
            self.assertIn("Signed in as admin", response.get_data(as_text=True))
            self.assertIn("Sign Out", response.get_data(as_text=True))
            self.assertIn("Welcome", response.get_data(as_text=True))

        with self.client.post("/users/signout", follow_redirects=True) as response:
            self.assertNotIn("Signed in as admin", response.get_data(as_text=True))
            self.assertIn("You have been signed out", response.get_data(as_text=True))
            self.assertIn("Sign In", response.get_data(as_text=True))

    def test_signin_unsuccessful(self):
        with self.client.post(
            "/users/signin", 
            data={"username":"foo", "password":"bar"}, follow_redirects=True
            ) as response:
            self.assertEqual(response.status_code, 422)
            self.assertIn("Invalid credentials, please try again", response.get_data(as_text=True))
            self.assertIn("Sign In", response.get_data(as_text=True))
            self.assertIn("foo", response.get_data(as_text=True))

    def test_signed_out_view(self):
        signed_out_message = "You must be signed in to do that"

        # try to access the edit view
        with self.client.get("/changes.txt/edit", follow_redirects=True) as response:
            self.assertIn(signed_out_message, response.get_data(as_text=True))

        # try to access the new document view 
        with self.client.get('/new', follow_redirects=True) as response:
            self.assertIn(signed_out_message, response.get_data(as_text=True))
 
        self.create_document("foo")
        # try to edit a doc 
        with self.client.post("/foo", data={"content": "There are many changes."}, follow_redirects=True) as response:
            self.assertIn(signed_out_message, response.get_data(as_text=True))

        # try to delete a doc
        with self.client.post("/foo/delete", follow_redirects=True) as response:
            self.assertIn(signed_out_message, response.get_data(as_text=True))

        # try to create new doc
        with self.client.post("/new", data={'file_name': "test.txt"}, follow_redirects=True) as response:
            self.assertIn(signed_out_message, response.get_data(as_text=True))

    def test_credential_in_yaml(self):
        # credentials in test.users.yaml
        with self.client.post(
            "/users/signin", 
            data={"username":"test_user", "password":"test_secret"}, 
            follow_redirects=True) as response:
                self.assertIn("Signed in as test", response.get_data(as_text=True))
                self.assertIn("Sign Out", response.get_data(as_text=True))
                self.assertIn("Welcome", response.get_data(as_text=True))
                self.assertEqual(200, response.status_code)

        # credentials not in test.users.yaml
        with self.client.post(
            "/users/signin", 
            data={"username":"audrey", "password":"secret"}, 
            follow_redirects=True) as response:
                self.assertNotIn("Signed in as audrey", response.get_data(as_text=True))
                self.assertIn("Invalid credentials", response.get_data(as_text=True))
                self.assertEqual(422, response.status_code)

    def test_hash_pw(self):
        # using hashed pw does not give access
        with self.client.post(
            "/users/signin",
            data={"username":"test_user", 
                  "password":"$2b$12$D2SLHxDKrTJJMwSGa9de5.FIK6TkyDYnqKzTB.OB8jV3MvnKgDlzq"},
            follow_redirects=True) as response:
                self.assertNotIn("Signed in as test_user", response.get_data(as_text=True))
                self.assertIn("Invalid credentials", response.get_data(as_text=True))
                self.assertEqual(422, response.status_code)


if __name__ == "__main__":
    unittest.main()