# RAHUL GOYAL
# CPE 202-03
# April 10, 2019

import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_eq(self):
        pass



    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")



if __name__ == "__main__":
        unittest.main()