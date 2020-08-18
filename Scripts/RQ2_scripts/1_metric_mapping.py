# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:59:19 2020

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

df_PM=pd.read_csv("RQ2_15_topic_keywords_detail_14_06_2020.csv", low_memory=False)

df_PM_tag=pd.read_csv("PM_RQ2_Tag_word_list.csv", low_memory=False)

filtered_tags=list(df_PM_tag['Filter_list'])

post_category=[]
post_language=[]
post_Enviroment=[]
post_Dependency=[]



for i in range(0, len(df_PM)):
    tags=re.findall(r'\<(.*?)\>',df_PM['Tags'][i])
    new_array = np.intersect1d(tags, filtered_tags)
    
    if len(new_array)==1:
        for j in range(0, len(df_PM_tag)):
            if new_array[0]==df_PM_tag['Filter_list'][j]:
                PM=df_PM_tag['PM'][j]
                Language=df_PM_tag['Language'][j]
                Environment=df_PM_tag['Enviroment'][j]
                Dependency=df_PM_tag['Dependency'][j]
    
    else:
        pos=random.randint(0, len(new_array)-1)
        for j in range(0, len(df_PM_tag)):
            
            if new_array[pos]==df_PM_tag['Filter_list'][j]:
                PM=df_PM_tag['PM'][j]
                Language=df_PM_tag['Language'][j]
                Environment=df_PM_tag['Enviroment'][j]
                Dependency=df_PM_tag['Dependency'][j]
                
    post_category.append(PM)
    post_language.append(Language)
    post_Enviroment.append(Environment)
    post_Dependency.append(Dependency)
    
dict={'post_Enviroment':post_Enviroment, 'post_Dependency':post_Dependency,'post_category':post_category, 'post_language':post_language,'Document_No':list(df_PM['Document_No']), 'Dominant_Topic':list(df_PM['Dominant_Topic']), 'Topic_Perc_Contrib':list(df_PM['Topic_Perc_Contrib']), 'Keywords':list(df_PM['Keywords']), 'Title':list(df_PM['Title']), 'Id':list(df_PM['Id']), 'Tags':list(df_PM['Tags']), 'AcceptedAnswerId':list(df_PM['AcceptedAnswerId'])   }

df=pd.DataFrame(dict)

df.to_csv("RQ2_LDA_topics_mapped_detail_27_6_20.csv")
    