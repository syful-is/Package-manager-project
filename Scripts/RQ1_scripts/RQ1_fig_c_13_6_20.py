# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 16:07:02 2020

@author: SE
"""

import pandas as pd
from matplotlib import pyplot as plt

import os

#Please specify your dataset directory. 
os.chdir("your dataset directory") 
 
# Data set

df1_PM = pd.read_csv("syc06_PM_all_question_post.csv", low_memory=False)
df2_ALL = pd.read_csv("syn08_All_So_post_summary.csv", low_memory=False)
#"""
#Package manager related
PM_reputation=list(df1_PM['reputation'])
PM_Views=list(df1_PM['Views'])

#All SO related
ALL_reputation=list(df2_ALL['reputation'])
ALL_Views=list(df2_ALL['Views'])



data=[PM_reputation,ALL_reputation,PM_Views,ALL_Views ]
x=[1,2,3,4]
labels=['PM_reputation', 'ALL_reputation', 'PM_Views', 'ALL_Views']

#plt.figure(figsize=(10,8))
plt.boxplot(data, 0, '')
plt.xticks(x, labels,  rotation=45)
plt.xlabel("Parameters")
plt.ylabel("Counts (#)")
plt.savefig("F:/1_NAIST_Research_SE/SE_meeting/PM_Stackoverflow/RQ1_answer_12_6_20/RQ1_fig_c_original.svg")
plt.show()

#"""