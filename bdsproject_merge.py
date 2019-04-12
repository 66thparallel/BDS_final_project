
# coding: utf-8

# In[17]:

import pandas as pd
import numpy as np
data = pd.read_csv('metadata.txt', sep="\t", header=None)
data.columns = ["userID","b", "rating", "lable", "date"]
data=data.drop(['b', 'date'],axis=1)
data2 = pd.read_csv('reviewContent.txt', sep="\t", header=None)
data2.columns = ["userID","b", "date", "content"]
result=data.set_index('userID').join(data2.set_index('userID'))
result.columns = [ "rating", "lable", "prob_ID","date","content"]
train, validate, test = np.split(result.sample(frac=1), [int(.6*len(result)), int(.8*len(result))])
