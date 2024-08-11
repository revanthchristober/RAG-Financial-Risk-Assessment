# src/tests/test_retriever.py

import unittest
from retriever import DataRetriever

class TestRetriever(unittest.TestCase):

    def test_load_data(self):
        retriever = DataRetriever('data/processed/processed_data.csv')
        data = retriever.load_data()
        self.assertFalse(data.empty)

if __name__ == '__main__':
    unittest.main()
