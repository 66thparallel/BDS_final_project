# coding: utf-8

# In[17]:

import pandas as pd
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

import re
import string
import unittest
from collections import Counter


data = pd.read_csv('metadata.txt', sep="\t", header=None)
data.columns = ["userID","b", "rating", "label", "date"]
data=data.drop(['b', 'date'],axis=1)
data2 = pd.read_csv('reviewContent.txt', sep="\t", header=None)
data2.columns = ["userID","b", "date", "content"]
result=data.set_index('userID').join(data2.set_index('userID'))
result.columns = [ "rating", "lable", "prob_ID","date","content"]
train, validate, test = np.split(result.sample(frac=1), [int(.6*len(result)), int(.8*len(result))])

# Get the top 100 1-grams
class Tokenizer:
    def __init__(self, text):
        self._text = text
        self._tokenized_text = []

    def tokenize(self):
        # Remove punctuation, empty elements, numbers, and dates
        pattern = re.compile('[0-9]+')
        self._tokenized_text = [''.join(c for c in s if c not in string.punctuation) for s in self._text]
        self._tokenized_text[:] = [word for word in self._tokenized_text if not pattern.match(word) and word!='']

        return self._tokenized_text


class RemoveStopWords:
    def __init__(self, text):
        self._text = text
        self._stopwords = []

    def removestopwords(self):
        with open('src/stopwords.txt', 'r') as g:
            self._stopwords = g.read().splitlines()
        for word in self._stopwords:
            self._text = [value for value in self._text if value.lower() != word]

        return self._text


class Preprocessor:
    def __init__(self):
        self._reviews = []
        self._cleantext = []
        self._temptext = []
        self._preprocessedlist = []

    def preprocess(self):

        with open('src/reviewContent.txt', 'r') as f:
            self._reviews = f.read().split()

            # Tokenize the text file
            self._temptext = Tokenizer(self._reviews)
            self._cleantext = self._temptext.tokenize()

            # Remove stop words
            self._temptext = RemoveStopWords(self._cleantext)
            self._cleantext = self._temptext.removestopwords()

            # Lemmatize the text
            lemma_text = []
            lemmatizer = WordNetLemmatizer()

            for word in list(self._cleantext):
                new_word = lemmatizer.lemmatize(word)
                lemma_text.append(new_word)

            for word in lemma_text:
                self._preprocessedlist.append(word)

        return self._preprocessedlist


class Onegrams:
    def __init__(self, topics):
        self._topics = topics

    def get_top_onegrams(self):

        # Find the most frequently occuring 1-grams
        word_freq = Counter(self._topics)
        common_words = word_freq.most_common(100)
        self._topics = dict(common_words)

        return self._topics


def main():

    # preprocessing:
    Prep = Preprocessor()
    prepped_text = Prep.preprocess()

    # Find 1-grams
    onegrams = Onegrams(prepped_text)
    top_onegrams = onegrams.get_top_onegrams()
    [print(x, end=', ') for x in top_onegrams]
    print('')

main()
