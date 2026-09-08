import unittest
from app import app

class TestDockerNetworkingFlask(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_about(self):
        res = self.client.get('/about')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["name"], "Simple REST API")
        self.assertEqual(data["version"], "1.0")

if __name__ == '__main__':
    unittest.main()
