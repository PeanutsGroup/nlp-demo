# -*- coding: utf-8 -*-
#

#import sys
#import string
import MeCab
import fasttext

def content_wakati(infile, tdata):
    t = MeCab.Tagger("-Owakati")
    with open(tdata + '.train', 'w') as nf, open(tdata + '.test', 'w') as tf:
        with open(infile, 'r') as df:
            for i, line in enumerate(df):
                if i % 5 == 0:
                    tf.write('__label__' + t.parse(line))
                else:
                    nf.write('__label__' + t.parse(line))
    return i

def train_model(tdata, model):
    classifier = fasttext.supervised(tdata + '.train', model)
    result = classifier.test(tdata + '.test')
    print('P@1:', result.precision)
    print('R@1:', result.recall)
    print('Number of examples:', result.nexamples)
    return result

def predict_class(model, contents):
    classifier = fasttext.load_model(model + '.bin')
    labels = classifier.predict(contents)
    print(labels)
    return labels

