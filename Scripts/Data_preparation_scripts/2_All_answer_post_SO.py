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
CreationDate=[]
Score=[]
ParentId=[]
Body=[]
CommentCount=[]
OwnerUserId=[]
Id_list=[]


path = "Posts.xml"

# get an iterable
context = et.iterparse(path, events=("start", "end"))

# turn it into an iterator
context = iter(context)

# get the root element
ev, root = next(context)

for ev, el in tqdm(context):
    if ev == 'start' and el.tag == 'row':
        if 'Id' in el.attrib and 'ParentId' in el.attrib:
            Id.append(el.attrib['Id'])
            ParentId.append(el.attrib['ParentId'])
            if 'CreationDate' not in el.attrib:
                CreationDate.append(0)
            else:
                CreationDate.append(el.attrib['CreationDate'])
            if 'Score' not in el.attrib:
                Score.append(0)
            else:
                Score.append(el.attrib['Score'])
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
          
            root.clear()
            
dict = {'Id': Id,'ParentId': ParentId,'CreationDate':CreationDate,'Score': Score, 'Body':Body, 'CommentCount':CommentCount, 'OwnerUserId':OwnerUserId}  
df1 = pd.DataFrame(dict) 
df1.to_csv('syc02_Answer_All_of_posts_SO_26_03_2020.csv',header=True, index=False, encoding='utf-8') 

end = datetime.now()
time_taken = end - start
print('Time: ',time_taken)