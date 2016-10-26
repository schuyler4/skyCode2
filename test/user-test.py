from unittest import TestCase
from app import app

class AppTestCase(TestCase):

    def setUp(self):
        self.app = app
        self.client
        self.client = self.app.test_client()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

    