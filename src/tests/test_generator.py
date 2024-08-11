# src/tests/test_generator.py

import unittest
from generator import TextGenerator
from config import Config

class TestGenerator(unittest.TestCase):

    def test_generate_text(self):
        generator = TextGenerator(api_key=Config.API_KEY)
        response = generator.generate_text('Test financial data')
        self.assertNotEqual(response, "")

if __name__ == '__main__':
    unittest.main()
