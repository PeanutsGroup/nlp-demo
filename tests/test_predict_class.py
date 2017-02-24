# -*- coding: utf-8 -*-
#

import unittest
import shutil
from nlpdemo.predict_class import *

class TestPredictClassMethods(unittest.TestCase):

    def test_predict_class_01(self):
        print('test predict_class start...')
        predict_class('result/yahoo_comment', \
                    'data/yahoo_comment_predict.in', \
                    'result/yahoo_comment_predict.out')
        print('test predict_class end...')

if __name__ == '__main__':
   unittest.main()

