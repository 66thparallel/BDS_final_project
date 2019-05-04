# coding: utf-8
# !/usr/bin/python3
"""
Authors: Jiajun Bao, Meng Li, Jane Liu
Classes:
    Main: Calls relevant classes and class methods and outputs all results.

"""

import numpy as np
import pandas as pd

def main():

    Prep = dataset('metadata.txt','reviewContent.txt')
    t,v,test=Prep.bdsproject_merge()
    
    
    unigramtopics=["place","sandwich", "salad", "good", "food", "Greek", "lamb", "lunch", "Snack", "great", "time", "service", "friend", "chicken", "small", "delicious", "eat", "soup", "back", "table", "restaurant", "dinner", "special", "ordered", "pretty", "bite", "recommend", "make", "huge", "quick", "perfect", "wall", "fresh", "tomato", "spot", "super", "tiny", "flavor", "cozy", "roasted", "big", "Soho", "wine", "price", "meal", "ingredient", "star", "bean", "light", "greek", "favorite", "pepper", "olive", "entree", "atmosphere", "bit", "hole", "gem", "hummus", "Great", "love", "tuna", "SoHo", "authentic", "fantastic", "souvlaki", "dish", "hard", "glass", "expect", "quaint", "review", "onion", "tasty", "cold", "winter", "avgolemono", "lemony", "butter", "feel", "fan", "juicy", "oil", "Chicken", "worth", "wait", "stuffed", "decided", "find", "people", "full", "Food", "Lamb", "Good", "orzo", "pastitsio", "cute", "die", "spinach", "pie"]
    
    Tra=Train(t,unigramtopics)
    data,topicf,result=Tra.Training()
    
    vali=Validate(v, topicf, result)
    vali.valid()
    
main()
    
    
