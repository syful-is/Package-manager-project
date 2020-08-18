# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 03:03:01 2020

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
PM_ViewCount=list(df1_PM['ViewCount'])

#All SO related
ALL_ViewCount=list(df2_ALL['so_ViewCount'])


data=[PM_ViewCount,ALL_ViewCount]
x=[1,2]
labels=['PM_ViewCount', 'ALL_ViewCount']

#plt.figure(figsize=(10,8))
plt.boxplot(data, 0, '')
plt.xticks(x, labels,  rotation=45)
plt.xlabel("Parameters")
plt.ylabel("Counts (#)")
plt.savefig("F:/1_NAIST_Research_SE/SE_meeting/PM_Stackoverflow/RQ1_answer_12_6_20/RQ1_fig_b_original.svg")
plt.show()

#"""