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


df1=pd.read_csv("syc09_all_users_details.csv", low_memory=False)

df2=pd.read_csv("syc10_PM_community_peoples_detail.csv", low_memory=False)




dict = {'Id': list(df1['Id']), 'AboutMe':list(df1['AboutMe']), 'DownVotes':list(df1['DownVotes']),'Location':list(df1['Location']),'UpVotes':list(df1['UpVotes']), 'Views':list(df1['Views']), 'reputation':list(df1['Reputation'])}  
df3 = pd.DataFrame(dict) 


dict = {'Id': list(df2['Id']), 'AboutMe':list(df2['AboutMe']), 'DownVotes':list(df2['DownVotes']),'Location':list(df2['Location']),'UpVotes':list(df2['UpVotes']), 'Views':list(df2['Views']), 'reputation':list(df2['reputation'])}  
df4 = pd.DataFrame(dict) 
#df1=pd.DataFrame({'A':[1,2,3,4],'B':[2,3,4,5]})
#df2=pd.DataFrame({'A':[1],'B':[2]})

df5=pd.concat([df3, df4]).drop_duplicates(keep=False)

df5.to_csv('syc09_all_users_details.csv', header=True, index=False, encoding='utf-8') 



