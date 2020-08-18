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


TRT=[]
TST=[]
No_post=[]


Tag_list=[]



df1 = pd.read_csv("1_all_post_details.csv")
df2 = pd.read_csv("syc02_filtered_tag.csv")

meta_tag=list(df1['Tags'])

Final_Tags1=list(df2['tags'])

Final_Tags=[]

for i in range(0, len(Final_Tags1)):
    Final_Tags.append(str(Final_Tags1[i]))

all_tag=[]
for i in range(0, len(meta_tag)):
    res = re.findall(r'\<(.*?)\>', meta_tag[i])
    
    for tag_element in res:
        all_tag.append(tag_element)
        

total_post=[]
for i in Final_Tags:
    num=all_tag.count(i)
    total_post.append(num)
    
dict={'tags':Final_Tags,'total_post_SO':total_post }

df3=pd.DataFrame(dict)

df3.to_csv("syc03_All_tags_frequency_on_SO.csv")


    
    

    
