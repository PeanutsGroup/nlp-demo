# -*- coding: utf-8 -*-
#

#import sys
#import string
import MeCab
import fasttext

def predict_class(model, infile, outfile):
    contents = []
    t = MeCab.Tagger("-Owakati")
    with open(infile, 'r') as df:
        for i, line in enumerate(df):
            contents.append(t.parse(line))
    classifier = fasttext.load_model(model + '.bin')
    labels = classifier.predict(contents)
    with open(outfile, 'w') as cf:
        for label in labels:
            print(label[0])
            cf.write(label[0][-1:] + '\n')
    return labels

