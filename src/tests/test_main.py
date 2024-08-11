# src/tests/test_main.py

import unittest
from main import main

class TestMain(unittest.TestCase):

    def test_main(self):
        """Tests the main function of the pipeline."""
        try:
            main()
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
