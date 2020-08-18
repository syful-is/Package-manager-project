# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 18:18:56 2020

@author: SE
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:31:45 2020

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
df1_PM = pd.read_csv("syc10_PM_community_peoples_detail.csv", low_memory=False)
df2_ALL = pd.read_csv("syc09_all_users_details.csv", low_memory=False)


#Package manager related
PM_reputation=list(df1_PM['reputation'])
PM_profileViews=list(df1_PM['Views'])


#All SO related
ALL_Reputation=list(df2_ALL['reputation'])
ALL_profileViews=list(df2_ALL['Views'])



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
data1 =PM_reputation
data2 =ALL_Reputation
# calculate cohen's d
d = cohend(data1, data2)
print('Cohens d: %.3f' % d)


# Kruskal-Wallis H-test
from numpy.random import seed
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
	print('Same distributions (fail to reject H0) --no significant difference')
else:
	print('Different distributions (reject H0)-significant difference')
    
    
