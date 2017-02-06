# -*- coding: utf-8 -*-
#

import unittest
import shutil
from nlpdemo.build_model import *

class TestBuildModelMethods(unittest.TestCase):

    def test_build_model_01(self):
        print('test content_wakati start...')
        content_wakati('work/yahoo_comment_xlsx/all_contents.cls', \
                    'work/yahoo_comment_xlsx/all_contents.wkt')
        print('test content_wakati end...')

        shutil.copy2('work/yahoo_comment_xlsx/all_contents.wkt', \
                    'data/yahoo_comment.train')
        shutil.copy2('work/yahoo_comment_xlsx/all_contents.wkt', \
                    'data/yahoo_comment.test')
        shutil.copy2('work/yahoo_comment_xlsx/all_contents.wkt', \
                    'data/yahoo_comment.predict')

        print('test train_model start...')
        train_model('data/yahoo_comment.train', \
                    'result/yahoo_comment')
        print('test train_model end...')

        print('test test_model start...')
        test_model('data/yahoo_comment.test', \
                    'result/yahoo_comment')
        print('test test_model end...')

if __name__ == '__main__':
   unittest.main()

