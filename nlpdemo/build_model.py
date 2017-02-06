# -*- coding: utf-8 -*-
#

#import sys
#import string
import MeCab
import fasttext

def content_wakati(infile, outfile):
    t = MeCab.Tagger("-Owakati")
    with open(outfile, 'w') as rf:
        with open(infile, 'r') as df:
            for i, line in enumerate(df):
                rf.write('__label__' + t.parse(line))
    return i

def train_model(data, model):
    classifier = fasttext.supervised(data, model)
    return classifier

def test_model(data, model):
    classifier = fasttext.load_model(model + '.bin')
    result = classifier.test(data)
    print('P@1:', result.precision)
    print('R@1:', result.recall)
    print('Number of examples:', result.nexamples)
    return result

def predict_class(model, contents):
    classifier = fasttext.load_model(model + '.bin')
    labels = classifier.predict(contents)
    print(labels)
    return labels

