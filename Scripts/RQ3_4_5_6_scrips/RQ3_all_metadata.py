# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:37:31 2020

@author: SE
"""


import re
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
from collections import Counter
import numpy as np
import random
import os

#Please specify your dataset directory. 
os.chdir("your dataset directory")

df_LDA=pd.read_csv("RQ2_15_topic_keywords_detail_14_06_2020.csv", low_memory=False)

df_PM=pd.read_csv("syc06_PM_all_question_post.csv", low_memory=False)


dict={'Document_No':df_LDA['Document_No'], 'Dominant_Topic':df_LDA['Dominant_Topic'], 'Topic_Perc_Contrib':df_LDA['Topic_Perc_Contrib'], 'new_keys':df_LDA['new_keys'],'Title':df_LDA['Text'], 'Id':df_PM['Id'], 'Tags':df_PM['Tags'] ,'AcceptedAnswerId':df_PM['AcceptedAnswerId'], 'AnswerCount':df_PM['AnswerCount'],'Body':df_PM['Body'], 'CommentCount':df_PM['CommentCount'], 'CommunityOwnedDate':df_PM['CommunityOwnedDate'],'CreationDate':df_PM['CreationDate'], 'FavoriteCount':df_PM['FavoriteCount'], 'OwnerUserId':df_PM['OwnerUserId'], 'PostTypeId':df_PM['PostTypeId'],'Score':df_PM['Score'], 'ViewCount':df_PM['ViewCount']    }

data=pd.DataFrame(dict)

data.to_csv("RQ3/RQ2_lda_15_topics_with_all_metadata.csv")
