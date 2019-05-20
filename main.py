# coding: utf-8
# !/usr/bin/python3
"""
Authors: Jiajun Bao, Meng Li, Jane Liu
Classes:
    Main: Calls relevant classes and class methods and outputs all results.

"""

import numpy as np
import pandas as pd
from dataset import *
from train import *
from validate import *
from preprocessor import *
from neuralnetwork import *
from detecting_sys_window import *

def main():
    
    # split the dataset to train, validate and test
    Prep = Dataset('data/metadata.txt','data/reviewContent.txt')
    t,v,test = Prep.bdsproject_merge()
    
    # output the most frequent unigrams
    prep_data = Preprocessor()
    unigramtopics = prep_data.preprocess()
    ngram_print(unigramtopics)    # print the most frequent unigrams to ngrams.txt
    
    # train the logistic regression model using ngrams only
    Tra = Train(t, unigramtopics)
    data,topicf,result = Tra.Training()
    
    # test and print the result of confusion matrix
    vali = Validate(v, topicf, result)
    valdata = vali.valid()
    
    # use MLPClassifier of NN to train the model and get the accuracy
    NNt = NN(data, valdata)
    NNt.train()

    #run the detecting window
    # frame = MainWindow(v, topicf, result)
 
    
main()
