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


Id=[]
PostTypeId=[]
AcceptedAnswerId=[]
OwnerUserId=[]
AnswerCount=[]
CommentCount=[]
FavoriteCount=[]
CommunityOwnedDate=[]
CreationDate=[]
Score=[]
ViewCount=[]
Title=[]
Body=[]
Tags=[]

df1=pd.read_csv("syc05_filtered_tag_used_for_data_extraction.csv")

Filter_list=[]

tag_list=list(df1['Filter_list'])

for i in range(0, len(tag_list)):
    Filter_list.append(str(tag_list[i]))
    
df3=pd.read_csv("syc01_all_question_post_SO_26_03_2020.csv")

for i in tqdm(range(0, len(df3['Id']))):
    line_tag=re.findall(r'\<(.*?)\>',df3['Tags'][i])
    new_array = np.intersect1d(Filter_list, line_tag)
    if len(new_array)>=1:
        Id.append(df3['Id'][i])
        PostTypeId.append(df3['PostTypeId'][i])
        AcceptedAnswerId.append(df3['AcceptedAnswerId'][i])
        OwnerUserId.append(df3['OwnerUserId'][i])
        AnswerCount.append(df3['AnswerCount'][i])
        CommentCount.append(df3['CommentCount'][i])
        FavoriteCount.append(df3['FavoriteCount'][i])
        CommunityOwnedDate.append(df3['CommunityOwnedDate'][i])
        CreationDate.append(df3['CreationDate'][i])
        Score.append(df3['Score'][i])
        ViewCount.append(df3['ViewCount'][i])
        Title.append(df3['Title'][i])
        Body.append(df3['Body'][i])
        Tags.append(df3['Tags'][i])
 
dict = {'Id': Id, 'PostTypeId':PostTypeId, 'AcceptedAnswerId':AcceptedAnswerId,'OwnerUserId':OwnerUserId,'AnswerCount':AnswerCount,'CommentCount':CommentCount, 'FavoriteCount':FavoriteCount, 'CommunityOwnedDate':CommunityOwnedDate,  'CreationDate':CreationDate,'Score': Score, 'ViewCount':ViewCount, 'Title':Title, 'Body':Body, 'Tags':Tags}  
df2 = pd.DataFrame(dict) 
df2.to_csv('syc06_PM_all_question_post.csv', header=True, index=False, encoding='utf-8') 

end = datetime.now()
time_taken = end - start
print('Time: ',time_taken)