# RAHUL GOYAL
# CPE 202-08
# April 10, 2019

import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Test the max_list_iter() function, which returns the maximum of a
        list using recursion."""

        # Test None list input
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(None)

        # Test empty list input
        self.assertEqual(max_list_iter([]), None)

        # Test length 1 list input
        self.assertEqual(max_list_iter([1]), 1)

        # Test typical list inputs
        self.assertEqual(max_list_iter([1, 2, 3]), 3)
        self.assertEqual(max_list_iter([1, 3, 2]), 3)
        self.assertEqual(max_list_iter([3, 2, 1]), 3)

        # Test repeated inputs
        self.assertEqual(max_list_iter([1, 1, 2, 3]), 3)
        self.assertEqual(max_list_iter([1, 2, 2, 3]), 3)
        self.assertEqual(max_list_iter([1, 2, 3, 3]), 3)

        # Test all same input
        self.assertEqual(max_list_iter([1, 1, 1]), 1)

    def test_reverse_rec(self):
        """Test the reverse_rec() function, which returns the reversed list
        using recursion."""

        # Test None list input
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(None)

        # Test empty list input
        self.assertEqual(reverse_rec([]), [])

        # Test length 1 list input
        self.assertEqual(reverse_rec([1]), [1])

        # Test typical list input
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_bin_search(self):
        """Test the bin_search() function, which returns the index of a value in
        a list using recursion."""

        test_list = [1, 3, 5, 7, 9, 10, 12, 14, 16, 18, 20]
        low = 0
        high = len(test_list)-1

        # Test None list input
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(100, low, high, None)

        # Test empty list input
        self.assertEqual(bin_search(100, 0, -1, []), None)

        # Test length 1 list input
        self.assertEqual(bin_search(1, 0, 1, [1]), 0)

        # Test target not in list (smaller than all)
        self.assertEqual(bin_search(0, low, high, test_list), None)
        # Test target not in list (middle)
        self.assertEqual(bin_search(15, low, high, test_list), None)
        # Test target not in list (larger than all)
        self.assertEqual(bin_search(25, low, high, test_list), None)

        # Test first index
        self.assertEqual(bin_search(1, low, high, test_list), 0)
        # Test last index
        self.assertEqual(bin_search(20, low, high, test_list), 10)

        # Test typical indices
        self.assertEqual(bin_search(3, low, high, test_list), 1)
        self.assertEqual(bin_search(5, low, high, test_list), 2)
        self.assertEqual(bin_search(7, low, high, test_list), 3)
        self.assertEqual(bin_search(9, low, high, test_list), 4)
        self.assertEqual(bin_search(10, low, high, test_list), 5)
        self.assertEqual(bin_search(12, low, high, test_list), 6)
        self.assertEqual(bin_search(14, low, high, test_list), 7)
        self.assertEqual(bin_search(16, low, high, test_list), 8)
        self.assertEqual(bin_search(18, low, high, test_list), 9)

        # Test low > 0 and high < len(test_list)-1
        self.assertEqual(bin_search(0, low+1, high-1, test_list), None)     # target not in list (smaller than all)
        self.assertEqual(bin_search(15, low+1, high-1, test_list), None)    # target not in list (middle)
        self.assertEqual(bin_search(25, low+1, high-1, test_list), None)    # target not in list (larger than all)
        self.assertEqual(bin_search(7, low+1, high, test_list), 3)          # low
        self.assertEqual(bin_search(7, low, high-1, test_list), 3)          # high
        self.assertEqual(bin_search(7, low+1, high-1, test_list), 3)        # both
        self.assertEqual(bin_search(12, low+1, high, test_list), 6)         # low
        self.assertEqual(bin_search(12, low, high-1, test_list), 6)         # high
        self.assertEqual(bin_search(12, low+1, high-1, test_list), 6)       # both



if __name__ == "__main__":
        unittest.main()