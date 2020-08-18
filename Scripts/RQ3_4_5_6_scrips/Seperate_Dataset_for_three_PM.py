# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 10:25:22 2020

@author: SE
"""

import pandas as pd
from matplotlib import pyplot as plt
from numpy.random import randn
from numpy.random import seed
from numpy import mean
from numpy import var
from math import sqrt
import re
import numpy as np

import os

#Please specify your dataset directory. 
os.chdir("your dataset directory")
 
 
# Data set

df_PM = pd.read_csv("RQ2_lda_15_topics_with_all_metadata.csv", low_memory=False)


Dominant_Topic=[]
Title=[]
Id=[]
Tags=[]
AcceptedAnswerId=[]
AnswerCount=[]
Body=[]
CommentCount=[]
CommunityOwnedDate=[]
CreationDate=[]
OwnerUserId=[]
FavoriteCount=[]
Score=[]
ViewCount=[]

#for maven
#filtered_tags=["maven","maven-2"]

#for npm
#filtered_tags=["npmignore","pnpm", "npm-shrinkwrap", "npm","npm-install", "npm-scripts"]

#for nuget
filtered_tags=["nuget-package","nuget","nuget-package-restore"]

for i in range(0, len(df_PM)):
    tags=re.findall(r'\<(.*?)\>',df_PM['Tags'][i])
    new_array = np.intersect1d(tags, filtered_tags)
    
    if len(new_array)>=1:
        Dominant_Topic.append(df_PM['Dominant_Topic'][i])
        Title.append(df_PM['Title'][i])
        Id.append(df_PM['Id'][i])
        Tags.append(df_PM['Tags'][i])
        AcceptedAnswerId.append(df_PM['AcceptedAnswerId'][i])
        AnswerCount.append(df_PM['AnswerCount'][i])
        Body.append(df_PM['Body'][i])
        CommentCount.append(df_PM['CommentCount'][i])
        CommunityOwnedDate.append(df_PM['CommunityOwnedDate'][i])
        CreationDate.append(df_PM['CreationDate'][i])
        OwnerUserId.append(df_PM['OwnerUserId'][i])
        FavoriteCount.append(df_PM['FavoriteCount'][i])
        Score.append(df_PM['Score'][i])
        ViewCount.append(df_PM['ViewCount'][i])
        
        
dict={'Dominant_Topic':Dominant_Topic, 'Title':Title, 'Id':Id, 'Tags':Tags, 'AcceptedAnswerId':AcceptedAnswerId, 'AnswerCount':AnswerCount, 'Body':Body, 'CommentCount':CommentCount, 'CommunityOwnedDate':CommunityOwnedDate,  'CreationDate':CreationDate,  'OwnerUserId':OwnerUserId,  'FavoriteCount':FavoriteCount,  'Score':Score, 'ViewCount':ViewCount }
        
data=pd.DataFrame(dict)

#data.to_csv("PM_Maven_all_questions.csv")      

#data.to_csv("PM_npm_all_questions.csv")      

data.to_csv("PM_nuget_all_questions.csv")      

        
        
        
        
        
        

