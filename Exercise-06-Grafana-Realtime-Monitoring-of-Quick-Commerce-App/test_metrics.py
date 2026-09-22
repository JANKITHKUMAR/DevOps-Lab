import unittest
from prometheus_client import generate_latest
import delivery_metrics

class TestMetricsSimulation(unittest.TestCase):
    def test_metrics_collection(self):
        delivery_metrics.simulate_delivery()
        output = generate_latest().decode('utf-8')
        self.assertIn("total_deliveries", output)
        self.assertIn("pending_deliveries", output)
        self.assertIn("on_the_way_deliveries", output)
        self.assertIn("average_delivery_time", output)

if __name__ == '__main__':
    unittest.main()
