import unittest
from app import app

class TestFlashSaleApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["message"], "Welcome to Big Sale!")
        self.assertIn("pod", data)

    def test_buy(self):
        res = self.client.get('/buy?user=alice')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["user"], "alice")
        self.assertIn("item", data)

    def test_health(self):
        res = self.client.get('/health')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["status"], "healthy")

if __name__ == '__main__':
    unittest.main()
