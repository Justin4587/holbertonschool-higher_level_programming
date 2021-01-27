#!/usr/bin/python3


"""I'm not sure how to even make a unit test
 totally winging it just to get something in the folder"""


import unittest
import models.base import Base
import models.rectangle import Rectangle
import models.square import Square


class TestThings(unittest.TestCase):
    """ more doc strings so that people know this is a test"""
    def test_id(self):
        base = Base()
        self.assertEqual(base.id, 1)

if __name__ == '__main__':
    unittest.__main__()
