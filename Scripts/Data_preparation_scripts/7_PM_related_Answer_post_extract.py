import pandas as pd

import xml.etree.ElementTree as et
import re
import pandas as pd
from datetime import datetime
start = datetime.now()
from tqdm.auto import tqdm
import numpy as np
import os

#Please specify your dataset directory. 
os.chdir("your dataset directory")




df1=pd.read_csv("syc02_Answer_All_of_posts_SO_26_03_2020.csv")

df2 pd.read_csv("syc06_PM_all_question_post.csv",low_memory=False)

Id_list=list(df2['Id'])


Id=[]
Ques_CreationDate=[]
Ans_CreationDate=[]
Score=[]
ParentId=[]
Body=[]
CommentCount=[]
OwnerUserId=[]
Id_list=[]
post_category=[]
post_language=[]
Dominant_Topic=[]
Topic_Perc_Contrib=[]
Title=[]
Tags=[]
AcceptedAnswerId=[]
for ind, i in tqdm(enumerate(list(df2['Id'][0:10]))):
   for index, j in enumerate(list(df1['ParentId'])):
        if i==j:
            Id.append(df1['Id'][index])
            ParentId.append(df1['ParentId'][index])
            Ans_CreationDate.append(df1['CreationDate'][index])
            Score.append(df1['Score'][index])
            Body.append(df1['Body'][index])
            CommentCount.append(df1['CommentCount'][index])
            OwnerUserId.append(df1['OwnerUserId'][index])
            
            Ques_CreationDate.append(df4['CreationDate'][ind])
            post_category.append(df2['post_category'][ind])
            post_language.append(df2['post_language'][ind])
            Dominant_Topic.append(df2['Dominant_Topic'][ind])
            Title.append(df2['Title'][ind])
            Tags.append(df2['Tags'][ind])
            AcceptedAnswerId.append(df2['AcceptedAnswerId'][ind])
            Topic_Perc_Contrib.append(df2['Topic_Perc_Contrib'][ind])
            
            

dict = {'Id': Id,'ParentId': ParentId,'Ques_CreationDate':Ques_CreationDate,'Ans_CreationDate':Ans_CreationDate,'Score': Score, 'Body':Body, 'CommentCount':CommentCount, 'OwnerUserId':OwnerUserId, 'post_category':post_category, 'post_language':post_language, 'Dominant_Topic':Dominant_Topic, 'Title':Title, 'Tags':Tags, 'AcceptedAnswerId':AcceptedAnswerId, 'Topic_Perc_Contrib':Topic_Perc_Contrib }  
df3 = pd.DataFrame(dict) 
df3.to_csv('syc07_PM_all_answer.csv',header=True, index=False, encoding='utf-8') 

end = datetime.now()
time_taken = end - start
print('Time: ',time_taken)