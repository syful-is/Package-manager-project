# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 16:18:50 2020

@author: SE
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:36:23 2020

@author: SE
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:00:26 2020

@author: SE
"""


import pandas as pd
from matplotlib import pyplot as plt
import statistics
import numpy as np

import os

#Please specify your dataset directory. 
os.chdir("your dataset directory") 
 
# Data set

df1_PM = pd.read_csv("syc10_PM_community_peoples_detail.csv", low_memory=False)
 
#empty_list
post_1=[]
post_2=[]
post_3=[]
post_4=[]
post_5=[]

reputation_1=[]
reputation_2=[]
reputation_3=[]
reputation_4=[]
reputation_5=[]

for i in range(0, len(df1_PM)):
    if df1_PM['Post'][i]==1:
        post_1.append(df1_PM['Id'][i])
        reputation_1.append(df1_PM['reputation'][i])
    if df1_PM['Post'][i]==2:
        post_2.append(df1_PM['Id'][i])
        reputation_2.append(df1_PM['reputation'][i])
    if df1_PM['Post'][i]==3:
        post_3.append(df1_PM['Id'][i])
        reputation_3.append(df1_PM['reputation'][i])
    if df1_PM['Post'][i]==4:
        post_4.append(df1_PM['Id'][i])
        reputation_4.append(df1_PM['reputation'][i])
    if df1_PM['Post'][i]>=5:
        post_5.append(df1_PM['Id'][i])
        reputation_5.append(df1_PM['reputation'][i])
    
Percent_user=[]
average_reputation=[]
label = ["1","2", "3", "4", ">5"]
x=[0, 1,2,3,4]

Percent_user.append((len(post_1)/len(df1_PM))*100)
Percent_user.append((len(post_2)/len(df1_PM))*100)
Percent_user.append((len(post_3)/len(df1_PM))*100)
Percent_user.append((len(post_4)/len(df1_PM))*100)
Percent_user.append((len(post_5)/len(df1_PM))*100)

average_reputation.append(statistics.median(reputation_1))
average_reputation.append(statistics.median(reputation_2))
average_reputation.append(statistics.median(reputation_3))
average_reputation.append(statistics.median(reputation_4))
average_reputation.append(statistics.median(reputation_5))

index = np.arange(len(label))


df = pd.DataFrame({'Percent_user':Percent_user ,
                   'reputation':average_reputation})

    
df['reputation'].plot(kind='line',linewidth=2, c='#000000',marker='o', secondary_y=True, label="Reputation")

df['Percent_user'].plot(kind='bar',width=0.80, color='#93ccea' ,label="Number of User")

  
plt.legend(loc="upper fight")

plt.xticks(x, label,rotation=90)

plt.xlabel("Number of Posts")

        
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
plt.savefig("RQ1_user_reputation_original.svg")
plt.show()

    

        
