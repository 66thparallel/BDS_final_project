# coding: utf-8
# !/usr/bin/python3
"""
Author: Jane Liu
Classes:
    Tokenizer:
        Accepts a list of words and outputs tokenized text.
    RemoveStopWords:
        Accepts a list of tokens and removes stop words
    Preprocessor:
        Calls Tokenizer, RemoveStopWords, and lemmatizes the text. Determines 1-grams and 2-grams. Generates
        topics sorted by frequency and outputs results to the console and topics.txt.
"""

import re
import string
import unittest
from collections import Counter
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams


# Get the top 100 1-grams
class Tokenizer:
    def __init__(self, text):
        self._text = text
        self._tokenized_text = []

    def tokenize(self):
        # Remove punctuation, empty elements, numbers, and dates
        pattern = re.compile('[0-9]+')
        self._tokenized_text = [''.join(c for c in s if c not in string.punctuation) for s in self._text]
        self._tokenized_text[:] = [word for word in self._tokenized_text if not pattern.match(word) and word != '']

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


class Unigrams:
    def __init__(self, topics):
        self._topics = topics
        self._unigrams = {}

    def get_top_unigrams(self):
        # Find the most frequently occuring unigrams
        word_freq = Counter(self._topics)
        common_words = word_freq.most_common(100)
        self._unigrams = dict(common_words)

        return self._unigrams


class Bigrams:
    def __init__(self, topics):
        self._topics = topics
        self._output = []
        self._bigrams = []

    # Find the most frequently occuring bigrams
    def get_top_bigrams(self):

        # Generate 2-grams
        self._output = list(ngrams(self._topics, 2))
        word_freq = Counter(self._output)
        common_words = word_freq.most_common(100)
        tempdict = dict(common_words)
        tup2str = ""

        for tup in tempdict:
            for i in tup:
                tup2str += i + " "
            tup2str = tup2str.strip()
            self._bigrams.append(tup2str)
            tup2str = ""

        return self._bigrams
