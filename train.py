import numpy as np
import pandas as pd

class Train:
    def __init__(self, file, topics):
        self._train = file
        self._topics = topics

    def LDAtokenize(self):
        #read file
        train = pd.read_csv(self._train)
        #convert column content to list
        content=[]
        content=train.content.tolist()
        #generate feature "length of review"
        listlen=[]
        for elem in content:
            listlen.append(len(str(elem)))
        train["length_of_review"]=listlen
        #split dataset to fake and non-fake
        nfdata=train.loc[train["label"]==1]
        fdata=train.loc[train["label"]==-1]
        #data cleaning
        fdata=fdata.dropna()
        nfdata=nfdata.dropna()
        nfdata=nfdata[nfdata['content']!="nan"]
        fdata=fdata[fdata['content']!="nan"]
        #convert content to list
        contentn=[]
        contentf=[]
        contentn=nfdata.content.tolist()
        contentf=fdata["content"].tolist()
        
        topicdict={}
        ftopicdict={}
