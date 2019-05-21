# coding: utf-8
# !/usr/bin/python3
"""
Authors: Jiajun Bao, Meng Li, Jane Liu
Classes:
    Dataset: Takes the data files and creates equal numbers of fake and non-fake data and merges them.
    Textprocess: Tokenizes, removes stopwords, lemmatizes the corpus.
    Main function: calls the preprocessing methods, LDA function, and function to determine the k-nearest neighbors

"""

import numpy as np
import pandas as pd
import re
import string
import unittest
from collections import Counter
import gensim
from gensim import corpora
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
import nltk
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
from preprocessor import *


class Dataset:
    def __init__(self, txt1, txt2):
        self._txt1 = txt1
        self._txt2 = txt2
        self._train = pd.DataFrame()
        self._validate = pd.DataFrame()
        self._test = pd.DataFrame()

    def merge(self):
        # merge dataset by userID
        data = pd.read_csv(self._txt1, sep="\t", header=None)
        data.columns = ["userID", "b", "rating", "lable", "date"]
        data = data.drop(['b', "rating", 'date'], axis=1)
        data2 = pd.read_csv(self._txt2, sep="\t", header=None)
        data2.columns = ["userID", "b", "date", "content"]
        data2 = data2.drop(['b', 'date'], axis=1)
        result = data.set_index('userID').join(data2.set_index('userID'))

        # rename column
        result.columns = ["label", "content"]

        # make the dataset balanced
        fakedata1 = result.loc[result["label"] == -1]
        fakedata2 = fakedata1.sample(n=10000)
        nfakedata1 = result.loc[result["label"] == 1]
        nfakedata2 = nfakedata1.sample(n=10000)
        nfakedata3 = nfakedata1.sample(n=105000)
        result2 = pd.concat([fakedata1, nfakedata3], ignore_index=True)

        # split dataset to train, validate and test and save it as csv.

        train, validate, test = np.split(result2.sample(frac=1), [int(.6 * len(result2)), int(.8 * len(result2))])
        test = test.sample(n=10000)
        final = pd.concat([fakedata2, nfakedata2, test])

        return final


def textprocess(data):
    data = data.content.values.tolist()
    lemmatizer = WordNetLemmatizer()
    wordCollect = []
    for word in data:
        word = str(word)
        wordCollect.append(word.split())
    collect = []
    for data in wordCollect:
        preprocessedlist = []
        temptext = Tokenizer(data)
        cleantext = temptext.tokenize()
        temptext = RemoveStopWords(cleantext)
        cleantext = temptext.removestopwords()
        lemma_text = []

        for word in list(cleantext):
            new_word = lemmatizer.lemmatize(word)
            lemma_text.append(new_word)

        for word in lemma_text:
            preprocessedlist.append(word)
        collect.append(preprocessedlist)
    return collect


def lda(collect):
    # dic for terms
    dictionary = corpora.Dictionary(collect)

    # DT matrix
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in collect]
    return dictionary, doc_term_matrix

def dist(a, b):
    dis = 0
    num_topic=5
    for i in range(0, num_topic):
        dis += ((a[i] - b[i]) ** 2) ** 0.5
    return dis


def main():
    np.random.seed(2018)
    Lda = gensim.models.ldamodel.LdaModel
    num_topic = 5   # number of topics selected.
    k = 5           # k value for Knn

    Prep = Dataset('data/metadata.txt', 'data/reviewContent.txt')

    f = Prep.merge()
    fc = textprocess(f)

    mark = f.label.values.tolist()
    dictionary_f, corpus_f = lda(fc)
    lda_f = Lda(corpus_f, num_topics=num_topic, id2word=dictionary_f, passes=50)
    topics = lda_f.show_topics()
    ct = 0
    print("A few sample rows from the document term matrix: \n")
    for topic in topics:
        if ct<10:
            print(topic)
            ct+=1

    all_topics = lda_f.get_document_topics(corpus_f, per_word_topics=True)
    i = 0
    d_t = []
    ct = 0
    print("LDA topics: \n")
    for doc_topics, word_topics, phi_values in all_topics:
        i += 1
        d_t.append(doc_topics)
        if ct<10:
            print('Review ' + str(i) + ' topics:', doc_topics)
            ct+=1

    print(lda_f)

    vec = []
    for term in d_t:
        temp = []
        for i in range(0, num_topic):
            temp.append(0)
        for topic in term:
            temp[int(topic[0])] = topic[1]
        vec.append(temp)


    def Knn(a, train, k):
        i = 0
        mi = []
        index = []
        for x in range(0, k):
            mi.append(100)
            index.append(0)
        for l in train:
            dis = dist(a, l)
            if dis < mi[-1]:
                mi[k - 1] = dis
                index[k - 1] = i
                j = k - 1
                while mi[j] < mi[j - 1] and j >= 1:
                    temp = mi[j]
                    mi[j] = mi[j - 1]
                    mi[j - 1] = temp
                    temp = index[j]
                    index[j] = index[j - 1]
                    index[j - 1] = temp
                    j -= 1

            i += 1
        return index

main()