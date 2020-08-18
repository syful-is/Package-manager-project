# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:53:15 2020

@author: syful
"""

import xml.etree.ElementTree as et
import re
import pandas as pd
from datetime import datetime
start = datetime.now()
from tqdm.auto import tqdm
import numpy as np
from collections import Counter
import os

#Please specify your dataset directory. 
os.chdir("your dataset directory")


Id=[]
CreationDate=[]
Score=[]
ViewCount=[]
Title=[]
Body=[]
Tags=[]



Tag_list=[]

df2 = pd.read_csv("syc01_PM_related_initial_post_detailed_syc.csv")


for element in df2['Tags']:
    res = re.findall(r'\<(.*?)\>', element)
    
    for tag_element in res:
        Tag_list.append(tag_element)

tag=[]
count=[]
data=Counter(Tag_list)

for i in data:
    tag.append(i)
    count.append(data[i])

dict={'tags':tag, 'count':count}

df1=pd.DataFrame(dict)

df1.to_csv('syc02_filtered_tag.csv', header=True, index=False, encoding='utf-8')
