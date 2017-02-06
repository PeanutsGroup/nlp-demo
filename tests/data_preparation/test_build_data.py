# -*- coding: utf-8 -*-
#

import unittest
from nlpdemo.data_preparation.build_data import *

class TestStringMethods(unittest.TestCase):

    def test_build_data_01(self):
        print('test retrieve_contents start...')
        retrieve_contents('data/yahoo_comment_xlsx/', \
                    'work/yahoo_comment_xlsx/all_contents.raw')
        print('test retrieve_contents end...')

        print('test machine_filter start...')
        machine_filter('work/yahoo_comment_xlsx/all_contents.raw', \
                    'work/yahoo_comment_xlsx/all_contents.cls', \
                    'data/yahoo_comment.kws')
        print('test machine_filter end...')

if __name__ == '__main__':
   unittest.main()

