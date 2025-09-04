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
        
    def create_document(self, name, content=''):
        with open(os.path.join(self.data_path, name), 'w') as file:
            file.write(content)

    def test_index(self):
        self.create_document('about.md')
        self.create_document('changes.txt')

        with self.client.get("/") as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "text/html; charset=utf-8")
            self.assertIn('about.md', response.get_data(as_text=True))
            self.assertIn('changes.txt', response.get_data(as_text=True))

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
        self.create_document('changes.txt', "There are many changes.")

        # assert that edit link works and containts content from 
        with self.client.get("/changes.txt/edit") as response:
            self.assertEqual(response.status_code, 200)
            self.assertIn("Edit content of changes.txt", response.get_data(as_text=True))
            self.assertIn("There are many changes.", response.get_data(as_text=True)) 
        
    def test_submit_edit(self):
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


if __name__ == "__main__":
    unittest.main()