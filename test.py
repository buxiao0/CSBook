# Your original test.py code
import unittest
from main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), "Hello, this is the main function.")

if __name__ == "__main__":
    unittest.main()
