# -*- coding: utf-8 -*-
#

import unittest
from nlpdemo.data_preparation.build_data import *

class TestStringMethods(unittest.TestCase):

    def test_retrieve_contents(self):
        retrieve_contents('data/yahoo_comment_xlsx/T_SNS_YAHOO_0914-1020_STOCK-1408_sjis.xlsx', \
                    'result/yahoo_comment_xlsx/T_SNS_YAHOO_0914-1020_STOCK-1408_sjis.txt')
        #self.assertEqual('', '')

if __name__ == '__main__':
   unittest.main()

