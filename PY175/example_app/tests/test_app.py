import unittest # import necessasry modules
from app import app # import functions from file you're testing

class AppTest(unittest.TestCase): # define test class
    def setUp(self): # called before running each test
        app.config['TESTING'] = True
        self.client = app.test_client() # test client, will simulate requests to our app

    def test_index(self): # methods start with test
        response = self.client.get('/') # make request and store response
        # make assertions based on response
        self.assertEqual(response.status_code, 200) # 
        self.assertEqual(response.get_data(), b"Hello, world!") # get_data returns a byte string 
                                        # so we use b prefix to indicate byte string response


if __name__ == "__main__":
    unittest.main()


''' from root project directory:
poetry run python -m unittest tests.test_app'''