# -*- coding: utf-8 -*-
#

import unittest
import shutil
from nlpdemo.build_model import *

class TestBuildModelMethods(unittest.TestCase):

    def test_build_model_01(self):
        print('test content_wakati start...')
        content_wakati('work/yahoo_comment_xlsx/all_contents.cls', \
                    'data/yahoo_comment')
        print('test content_wakati end...')

        print('test train_model start...')
        train_model('data/yahoo_comment', \
                    'result/yahoo_comment')
        print('test train_model end...')

if __name__ == '__main__':
   unittest.main()

