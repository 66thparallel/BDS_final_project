# coding: utf-8
# !/usr/bin/python3
"""
Authors: Jiajun Bao, Meng Li, Jane Liu
Classes:
    Main: Calls relevant classes and class methods and outputs all results.

"""

# In[17]:

import pandas as pd
import numpy as np
import nltk
from preprocessor import *


def main():
    # data = pd.read_csv('src/metadata.txt', sep="\t", header=None)
    # data.columns = ["userID","b", "rating", "label", "date"]
    # data = data.drop(['b', 'date'],axis=1)
    # data2 = pd.read_csv('src/reviewContent.txt', sep="\t", header=None)
    # data2.columns = ["userID","b", "date", "content"]
    # result = data.set_index('userID').join(data2.set_index('userID'))
    # result.columns = [ "rating", "label", "prob_ID","date","content"]
    # train, validate, test = np.split(result.sample(frac=1), [int(.6*len(result)), int(.8*len(result))])

    # preprocessing:
    Prep = Preprocessor()
    prepped_text = Prep.preprocess()

    # Find unigrams
    unigrams = Unigrams(prepped_text)
    top_unigrams = unigrams.get_top_unigrams()

    # Find bigrams
    bigrams = Bigrams(prepped_text)
    top_bigrams = bigrams.get_top_bigrams()

    ngram_print(top_unigrams, top_bigrams)


main()
