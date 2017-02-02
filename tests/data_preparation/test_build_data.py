# -*- coding: utf-8 -*-
#

import unittest
from nlpdemo.data_preparation.build_data import *

class TestStringMethods(unittest.TestCase):

    def test_retrieve_contents(self):
        retrieve_contents('data/yahoo_comment_xlsx/', \
                    'result/yahoo_comment_xlsx/all_contents.txt')

if __name__ == '__main__':
   unittest.main()

