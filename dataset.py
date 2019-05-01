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

class dataset:
    def __init__(self, txt1,txt2):
        self._txt1 = txt1
        self._txt2 = txt2
        self._train=pd.DataFrame()
        self._validate=pd.DataFrame()
        self._test=pd.DataFrame()
        


    def bdsproject_merge(self):
        #merge dataset by userID
        data = pd.read_csv(self._txt1, sep="\t", header=None)
        data.columns = ["userID","b", "rating", "lable", "date"]
        data=data.drop(['b', 'date'],axis=1)
        data2 = pd.read_csv(self._txt2, sep="\t", header=None)
        data2.columns = ["userID","b", "date", "content"]
        result=data.set_index('userID').join(data2.set_index('userID'))
        
        #rename column
        result.columns = [ "rating", "label", "prob_ID","date","content"]
        
        #make the dataset balanced
        fakedata1=result.loc[result["label"]==-1]
        nfakedata1=result.loc[result["label"]==1]
        nfakerdata2=nfakedata1.sample(n=105000)
        result2=pd.concat([fakedata1,nfakerdata2],ignore_index=True)
        
        #split dataset to train, validate and test and save it as csv.
        self._train, self._validate, self._test = np.split(result2.sample(frac=1), [int(.6*len(result2)), int(.8*len(result2))])
        
        self._train.to_csv("train.csv")
        self._validate.to_csv("validate.csv")
        self._test.to_csv("test.csv")
        
        return self._train, self._validate, self._test

        


