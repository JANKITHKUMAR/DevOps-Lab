import unittest
from product_catalog import app as product_app
from shopping_cart import app as cart_app

class TestMultiNodeApps(unittest.TestCase):
    def setUp(self):
        self.prod_client = product_app.test_client()
        self.cart_client = cart_app.test_client()

    def test_products(self):
        res = self.prod_client.get("/products")
        self.assertEqual(res.status_code, 200)
        items = res.get_json()
        self.assertEqual(len(items), 3)
        self.assertEqual(items[0]["name"], "Laptop")

    def test_cart(self):
        res = self.cart_client.get("/cart")
        self.assertEqual(res.status_code, 200)
        
        post_res = self.cart_client.post("/cart", json={"id": 1, "name": "Laptop", "quantity": 1})
        self.assertEqual(post_res.status_code, 201)
        cart_items = post_res.get_json()
        self.assertEqual(len(cart_items), 1)
        self.assertEqual(cart_items[0]["name"], "Laptop")

if __name__ == '__main__':
    unittest.main()
