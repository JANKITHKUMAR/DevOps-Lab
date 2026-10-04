import subprocess
import unittest

class TestHelloWorldScript(unittest.TestCase):
    def test_output(self):
        result = subprocess.run(["bash", "hello-world.sh"], capture_output=True, text=True, shell=True)
        self.assertIn("Hello, Jenkins!", result.stdout)

if __name__ == '__main__':
    unittest.main()
