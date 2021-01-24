from hello_world import app
import unittest

class TestHelloWorld(unittest.TestCase):
    
    # Check for response 200
    def test_index(self):
        self.tester = app.test_client()
        response = self.tester.get('/')
        self.assertEqual(response.status_code, 200)

    if __name__=='__main__':
        unittest.main()