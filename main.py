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
from Train import *
from Validate import *

def main():
    
    #split the dataset to train, validate and test
    Prep = dataset('metadata.txt','reviewContent.txt')
    t,v,test=Prep.bdsproject_merge()
    
    #read most frequent 100 topics
    text_file = open("ngrams.txt", "r")
    lines = text_file.read().split(", ")
    unigramtopics=lines[:100]
    
    #train the model
    Tra=Train(t,unigramtopics)
    data,topicf,result=Tra.Training()
    
    #validate and print the result of confusion matrix
    vali=Validate(v, topicf, result)
    vali.valid()
    
main()
    
    
