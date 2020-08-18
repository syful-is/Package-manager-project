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


path = "Posts.xml"

# get an iterable
context = et.iterparse(path, events=("start", "end"))

# turn it into an iterator
context = iter(context)

# get the root element
ev, root = next(context)

for ev, el in tqdm(context):
    if ev == 'start' and el.tag == 'row':
        if 'Id' in el.attrib and el.attrib['PostTypeId']=='1':
            
            Id.append(el.attrib['Id'])
            
            if 'PostTypeId' not in el.attrib:
                PostTypeId.append(0)
            else:
                PostTypeId.append(el.attrib['PostTypeId'])
            if 'AcceptedAnswerId' not in el.attrib:
                AcceptedAnswerId.append(0)
            else:
                AcceptedAnswerId.append(el.attrib['AcceptedAnswerId'])
            if 'AnswerCount' not in el.attrib:
                AnswerCount.append(0)
            else:
                AnswerCount.append(el.attrib['AnswerCount'])
            if 'FavoriteCount' not in el.attrib:
                FavoriteCount.append(0)
            else:
                FavoriteCount.append(el.attrib['FavoriteCount'])
            if 'CommunityOwnedDate' not in el.attrib:
                CommunityOwnedDate.append(0)
            else:
                CommunityOwnedDate.append(el.attrib['CommunityOwnedDate'])
            
            if 'CreationDate' not in el.attrib:
                CreationDate.append(0)
            else:
                CreationDate.append(el.attrib['CreationDate'])
            if 'Score' not in el.attrib:
                Score.append(0)
            else:
                Score.append(el.attrib['Score'])
            if 'Title' not in el.attrib:
                Title.append(0)
            else:
                Title.append(el.attrib['Title'])
            if 'Body' not in el.attrib:
                Body.append(0)
            else:
                Body.append(el.attrib['Body'])
            if 'CommentCount' not in el.attrib:
                CommentCount.append(0)
            else:
                CommentCount.append(el.attrib['CommentCount'])
            if 'OwnerUserId' not in el.attrib:
                OwnerUserId.append(0)
            else:
                OwnerUserId.append(el.attrib['OwnerUserId'])
            if 'ViewCount' not in el.attrib:
                ViewCount.append(0)
            else:
                ViewCount.append(el.attrib['ViewCount'])
            if 'Tags' not in el.attrib:
                Tags.append(0)
            else:
                Tags.append(el.attrib['Tags'])
            
          
            root.clear()
            
dict = {'Id': Id, 'PostTypeId':PostTypeId, 'AcceptedAnswerId':AcceptedAnswerId,'OwnerUserId':OwnerUserId,'AnswerCount':AnswerCount,'CommentCount':CommentCount, 'FavoriteCount':FavoriteCount, 'CommunityOwnedDate':CommunityOwnedDate,  'CreationDate':CreationDate,'Score': Score, 'ViewCount':ViewCount, 'Title':Title, 'Body':Body, 'Tags':Tags}  
df1 = pd.DataFrame(dict) 
df1.to_csv('syc01_all_question_post_SO_26_03_2020.csv', header=True, index=False, encoding='utf-8') 

end = datetime.now()
time_taken = end - start
print('Time: ',time_taken)