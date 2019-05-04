# coding: utf-8
# !/usr/bin/python3
"""
Authors: Jiajun Bao, Meng Li, Jane Liu
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import classification_report, confusion_matrix

class Validate:
    def __init__(self, file, ftopic, result):
        self._val = file
        self._ftopic= ftopic
        self._result=result
        self._len = []
        self._cols_to_keep=[]


    def valid(self):
        #read validation file and data cleaning
        validate=self._val.dropna()
        validate=validate[validate['content']!="nan"]
        
        #generate topic features:
        for topic in self._ftopic:
            tlist=[]
            for c in validate["content"]:
                count=0
                p=c.split()
                for word in p:
                    if word==topic:
                        count+=1
                tlist.append(count)
            validate[topic]=tlist
        
        #generate feature: "length of review":
        for elem in validate.content:
            self._len.append(len(str(elem)))
        validate["length_of_review"]=self._len
        
        #treat the feature "rating" as dummy variable
        dummy_ranks = pd.get_dummies(validate['rating'], prefix='rating')
        
        #create dataset for regression
        
        self._cols_to_keep=["label","length_of_review"]
        
        for elem in self._ftopic:
            self._cols_to_keep.append(elem)
        
        val = validate[self._cols_to_keep].join(dummy_ranks.ix[:, 'rating_2.0':])
             
        #change the label of fake data from -1 to 0
        val.loc[val.label==-1,'label'] =0
        
        #standarized train data
        val_cols = val.columns[1:]
        val[val_cols]=val[val_cols].apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
        
        #add intercept
        val['intercept'] = 1.0
        
        val_cols1 = val.columns[1:]
        #run the model
        
        val['predict'] = self._result.predict(val[val_cols1])
        
                
        #print the accuracy of logistic model
        total=[]
        for value in val.values:

            predict = value[-1]
            # actural
            label = int(value[0])
 
            # if the value of predict is bigger than 0.5, assign it as non-fake
            if predict > 0.5:
                total.append(1)
            else:
                total.append(0)
                
        print(confusion_matrix(val['label'],total))
        print(classification_report(val['label'],total))
        
        


