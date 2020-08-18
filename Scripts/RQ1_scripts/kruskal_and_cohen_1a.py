# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 00:00:25 2020

@author: SE
"""


import pandas as pd
from matplotlib import pyplot as plt
from numpy.random import randn
from numpy.random import seed
from numpy import mean
from numpy import var
from math import sqrt
import os

#Please specify your dataset directory. 
os.chdir("your dataset directory")

#os.chdir("F:/1_NAIST_Research_SE/SE_meeting/PM_Stackoverflow/Replication_package/Dataset/")
 
 
# Data set

df1_PM = pd.read_csv("syc06_PM_all_question_post.csv", low_memory=False)
df2_ALL = pd.read_csv("syn08_All_So_post_summary.csv", low_memory=False)

#Package manager related
PM_score=list(df1_PM['Score'])
PM_FavoriteCount=list(df1_PM['FavoriteCount'])
PM_AnswerCount=list(df1_PM['AnswerCount'])
PM_CommentCount=list(df1_PM['CommentCount'])

#All SO related
ALL_score=list(df2_ALL['Score'])
ALL_FavoriteCount=list(df2_ALL['FavoriteCount'])
ALL_AnswerCount=list(df2_ALL['AnswerCount'])
ALL_CommentCount=list(df2_ALL['CommentCount'])


data=[PM_score, ALL_score, PM_FavoriteCount, ALL_FavoriteCount, PM_AnswerCount,ALL_AnswerCount, PM_CommentCount, ALL_CommentCount]
x=[1,2,3,4,5,6,7,8]
labels=['PM_Score', 'ALL_Score', 'PM_FavoriteCount','ALL_FavouriteCount', 'PM_AnswerCount','ALL_AnswerCount', 'PM_CommentCount', 'ALL_CommentCount']


# function to calculate Cohen's d for independent samples
def cohend(d1, d2):
	# calculate the size of samples
	n1, n2 = len(d1), len(d2)
	# calculate the variance of the samples
	s1, s2 = var(d1, ddof=1), var(d2, ddof=1)
	# calculate the pooled standard deviation
	s = sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
	# calculate the means of the samples
	u1, u2 = mean(d1), mean(d2)
	# calculate the effect size
	return (u1 - u2) / s

# seed random number generator
seed(1)
# prepare data
data1 = PM_CommentCount
data2 = ALL_CommentCount
# calculate cohen's d
d = cohend(data1, data2)
print('Cohens d: %.3f' % d)

# Kruskal-Wallis H-test
from numpy.random import seed
from numpy.random import randn
from scipy.stats import kruskal
# seed the random number generator
seed(1)
# generate three independent samples

# compare samples
stat, p = kruskal(data1, data2)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('Same distributions (fail to reject H0)')
else:
	print('Different distributions (reject H0)')