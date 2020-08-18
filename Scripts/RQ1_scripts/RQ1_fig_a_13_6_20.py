
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
PM_score=list(df1_PM['Score'])
PM_FavoriteCount=list(df1_PM['FavoriteCount'])
PM_AnswerCount=list(df1_PM['AnswerCount'])
PM_CommentCount=list(df1_PM['CommentCount'])

#All SO related
ALL_score=list(df2_ALL['So_Score'])
ALL_FavoriteCount=list(df2_ALL['So_FavoriteCount'])
ALL_AnswerCount=list(df2_ALL['So_AnswerCount'])
ALL_CommentCount=list(df2_ALL['So_CommentCount'])


data=[PM_score, ALL_score, PM_FavoriteCount, ALL_FavoriteCount, PM_AnswerCount,ALL_AnswerCount, PM_CommentCount, ALL_CommentCount]
x=[1,2,3,4,5,6,7,8]
labels=['PM_Score', 'ALL_Score', 'PM_FavoriteCount','ALL_FavouriteCount', 'PM_AnswerCount','ALL_AnswerCount', 'PM_CommentCount', 'ALL_CommentCount']


plt.boxplot(data, 0, '')
plt.xticks(x, labels,  rotation=90)
plt.xlabel("Parameters")
plt.ylabel("Counts (#)")
plt.savefig("RQ1_answer_12_6_20/RQ1_fig_a_original.svg")
plt.show()

#"""