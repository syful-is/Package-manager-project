# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 00:06:42 2020

@author: SE
"""

import re
import pandas as pd
from datetime import datetime
start = datetime.now()
from tqdm.auto import tqdm
import numpy as np
import os

#Please specify your dataset directory. 
os.chdir("your dataset directory")


Id=[]
AboutMe=[]
DownVotes=[]
Location=[]
Post=[]
UpVotes=[]
Views=[]
reputation=[]


df1=pd.read_csv("syn08_All_So_post_summary_RQ1.csv", low_memory=False)

df2=pd.read_csv("syc07_PM_all_answer.csv", low_memory=False)




dict1 = {'So_AnswerCount': list(df1['So_AnswerCount']), 'So_CommentCount':list(df1['So_CommentCount']), 'So_FavoriteCount':list(df1['So_FavoriteCount']),'So_Id':list(df1['So_Id']),'So_Score':list(df1['So_Score']), 'so_ViewCount':list(df1['so_ViewCount'])}  
df3 = pd.DataFrame(dict1) 


dict2 = {'So_AnswerCount': list(df2['AnswerCount']), 'So_CommentCount':list(df2['CommentCount']), 'So_FavoriteCount':list(df2['FavoriteCount']),'So_Id':list(df2['Id']),'So_Score':list(df2['Score']), 'so_ViewCount':list(df2['ViewCount'])}  
df4 = pd.DataFrame(dict2) 
#df1=pd.DataFrame({'A':[1,2,3,4],'B':[2,3,4,5]})
#df2=pd.DataFrame({'A':[1],'B':[2]})

df5=pd.concat([df3, df4]).drop_duplicates(keep=False)

df5.to_csv('syn08_All_So_post_summary.csv', header=True, index=False, encoding='utf-8') 

 
