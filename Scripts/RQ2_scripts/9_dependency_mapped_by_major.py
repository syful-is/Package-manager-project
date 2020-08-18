# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:51:50 2020

@author: SE
"""


"""
Created on Mon Mar 30 16:57:13 2020

@author: SE
"""

import re
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
from collections import Counter
import numpy as np
import random
import os

#Please specify your dataset directory. 
os.chdir("your dataset directory")

df_PM=pd.read_csv("RQ2_LDA_topics_mapped_detail_15_6_20_version_2.csv", low_memory=False)


df_PM_topics=pd.read_csv("syc08_PM_all_question_post_12_6_20.csv", low_memory=False)

gk = df_PM.groupby('Major_cat') 


 
Flat=[]
Multi=[]
Nested=[]

Topic=[]

#no of posts after manual categorization
 
n_Flat=164570
n_Multi=645
n_Nested=57555
 

for i in range(0, 10):
    Topic.append(i)
    data=gk.get_group(i)
    df4=data.reset_index()
    
    Flat1=[]
    Multi1=[]
    Nested1=[]
    
    for j in range(0, len(df4)):
        if df4['post_Dependency'][j]=='Flat':
            Flat1.append('Flat')
        if df4['post_Dependency'][j]=='Multi':
            Multi1.append('Multi')
        if df4['post_Dependency'][j]=='Nested':
            Nested1.append('Nested')
        
    Flat.append((len(Flat1)/n_Flat)*100)
    Multi.append((len(Multi1)/n_Multi)*100)
    Nested.append((len(Nested1)/n_Nested)*100)
         
dict={'Topic':Topic,'Flat':Flat, 'Multi':Multi, 'Nested':Nested}

LDA_data=pd.DataFrame(dict)

LDA_data.to_csv("topic_15_Dependency_SemiMajorCat_mapping_result_15_6_2020.csv")    

        

#"""