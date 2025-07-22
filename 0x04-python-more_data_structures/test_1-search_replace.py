import unittest

from 1-search_replace import search_replace

class TestSearchReplace(unittest.TestCase):
    def test_replace_single_occurrence(self):
        self.assertEqual(search_replace([1, 2, 3], 2, 99), [1, 99, 3])

    def test_replace_multiple_occurrences(self):
        self.assertEqual(search_replace([1, 2, 2, 3], 2, 99), [1, 99, 99, 3])

    def test_no_occurrence(self):
        self.assertEqual(search_replace([1, 2, 3], 4, 99), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(search_replace([], 1, 99), [])

    def test_replace_with_same_value(self):
        self.assertEqual(search_replace([1, 2, 3], 2, 2), [1, 2, 3])

    def test_replace_strings(self):
        self.assertEqual(search_replace(['a', 'b', 'c'], 'b', 'z'), ['a', 'z', 'c'])

    def test_mixed_types(self):
        self.assertEqual(search_replace([1, 'a', 2, 'a'], 'a', 99), [1, 99, 2, 99])

if __name__ == '__main__':
    unittest.main()