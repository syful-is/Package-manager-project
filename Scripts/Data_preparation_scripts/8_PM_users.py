# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 15:45:00 2020

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


df1=pd.read_csv("syc06_PM_all_question_post.csv", low_memory=False)

Filter_list1=list(df1['OwnerUserId'])

Filter_list=list(set(Filter_list1))

df3=pd.read_csv("syc09_all_users_details.csv", low_memory=False)

#"""
for i in tqdm(range(0, len(df3['Id']))):
    Id1=df3['Id'][i]
    new_array = np.intersect1d(Filter_list, Id1)
    if len(new_array)>=1:
        Id.append(df3['Id'][i])
        AboutMe.append(df3['AboutMe'][i])
        DownVotes.append(df3['DownVotes'][i])
        Location.append(df3['Location'][i])
        Post.append(df3['Post'][i])
        UpVotes.append(df3['UpVotes'][i])
        Views.append(df3['Views'][i])
        reputation.append(df3['reputation'][i])
        
 
dict = {'Id': Id, 'AboutMe':AboutMe, 'DownVotes':DownVotes,'Location':Location,'Post':Post,'UpVotes':UpVotes, 'Views':Views, 'reputation':reputation}  
df2 = pd.DataFrame(dict) 
df2.to_csv('syc10_PM_community_peoples_detail.csv', header=True, index=False, encoding='utf-8') 

end = datetime.now()
time_taken = end - start
print('Time: ',time_taken)

#"""



