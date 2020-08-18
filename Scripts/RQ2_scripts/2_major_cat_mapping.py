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

df_PM=pd.read_csv("RQ2_LDA_topics_mapped_detail_27_6_20.csv", low_memory=False)

#""" 
post_category=[]
post_language=[]
post_Enviroment=[]
post_Dependency=[]
Document_No=[]
Dominant_Topic=[]
Topic_Perc_Contrib=[]
Keywords=[]
Title=[]
Id=[]
Tags=[]
AcceptedAnswerId=[]

Major_cat=[]




for i in range(0, len(df_PM)):
    
    
    if df_PM['Dominant_Topic'][i]==0 or df_PM['Dominant_Topic'][i]==1 or df_PM['Dominant_Topic'][i]==3 or df_PM['Dominant_Topic'][i]==6 or df_PM['Dominant_Topic'][i]==8 or df_PM['Dominant_Topic'][i]==11 or df_PM['Dominant_Topic'][i]==9 or df_PM['Dominant_Topic'][i]==14 or df_PM['Dominant_Topic'][i]==7 :
        Major_cat.append(0)
        post_category.append(df_PM['post_category'][i])
        post_language.append(df_PM['post_language'][i])
        post_Enviroment.append(df_PM['post_Enviroment'][i])
        post_Dependency.append(df_PM['post_Dependency'][i])
        Document_No.append(df_PM['Document_No'][i])
        Dominant_Topic.append(df_PM['Dominant_Topic'][i])
        Topic_Perc_Contrib.append(df_PM['Topic_Perc_Contrib'][i])
        Keywords.append(df_PM['Keywords'][i])
        Title.append(df_PM['Title'][i])
        Id.append(df_PM['Id'][i])
        Tags.append(df_PM['Tags'][i])
        AcceptedAnswerId.append(df_PM['AcceptedAnswerId'][i])
        
    if df_PM['Dominant_Topic'][i]==2 or df_PM['Dominant_Topic'][i]==5 or df_PM['Dominant_Topic'][i]==10:
        Major_cat.append(1)
        post_category.append(df_PM['post_category'][i])
        post_language.append(df_PM['post_language'][i])
        post_Enviroment.append(df_PM['post_Enviroment'][i])
        post_Dependency.append(df_PM['post_Dependency'][i])
        Document_No.append(df_PM['Document_No'][i])
        Dominant_Topic.append(df_PM['Dominant_Topic'][i])
        Topic_Perc_Contrib.append(df_PM['Topic_Perc_Contrib'][i])
        Keywords.append(df_PM['Keywords'][i])
        Title.append(df_PM['Title'][i])
        Id.append(df_PM['Id'][i])
        Tags.append(df_PM['Tags'][i])
        AcceptedAnswerId.append(df_PM['AcceptedAnswerId'][i])
    
    if df_PM['Dominant_Topic'][i]==4 or df_PM['Dominant_Topic'][i]==12 or df_PM['Dominant_Topic'][i]==13:
        Major_cat.append(2)
        post_category.append(df_PM['post_category'][i])
        post_language.append(df_PM['post_language'][i])
        post_Enviroment.append(df_PM['post_Enviroment'][i])
        post_Dependency.append(df_PM['post_Dependency'][i])
        Document_No.append(df_PM['Document_No'][i])
        Dominant_Topic.append(df_PM['Dominant_Topic'][i])
        Topic_Perc_Contrib.append(df_PM['Topic_Perc_Contrib'][i])
        Keywords.append(df_PM['Keywords'][i])
        Title.append(df_PM['Title'][i])
        Id.append(df_PM['Id'][i])
        Tags.append(df_PM['Tags'][i])
        AcceptedAnswerId.append(df_PM['AcceptedAnswerId'][i])
    
dict={'Major_cat':Major_cat,'post_Enviroment':post_Enviroment, 'post_Dependency':post_Dependency,'post_category':post_category, 'post_language':post_language,'Document_No':list(df_PM['Document_No']), 'Dominant_Topic':list(df_PM['Dominant_Topic']), 'Topic_Perc_Contrib':list(df_PM['Topic_Perc_Contrib']), 'Keywords':list(df_PM['Keywords']), 'Title':list(df_PM['Title']), 'Id':list(df_PM['Id']), 'Tags':list(df_PM['Tags']), 'AcceptedAnswerId':list(df_PM['AcceptedAnswerId'])   }

df=pd.DataFrame(dict)

df.to_csv("RQ2_LDA_topics_mapped_by_major_detail_27_6_20.csv")

#""" 