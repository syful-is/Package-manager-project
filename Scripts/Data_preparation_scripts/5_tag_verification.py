# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 17:58:49 2020

@author: SE
"""

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
PM_post_count=[]
total_post_SO=[]


Tag_list=[]

df2 = pd.read_csv("syc04_All_tags_detail_information.csv")


Final_Tags1=list(df2['Final_Tags'])

Final_Tags=[]

for i in range(0, len(Final_Tags1)):
    Final_Tags.append(str(Final_Tags1[i]))
    


Filter_list=[]

for i, element in enumerate(Final_Tags):
    if re.findall(r'Go', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
        
    elif re.findall(r'NuGet', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Bower', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Clojars', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Atom', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Puppet', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Carthage', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Dub', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Nimble', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Inqlude', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'npm', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Maven', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'WordPress', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'CRAN', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Pub', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Emacs', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Julia', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Jam', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Shards', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Packagist', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Rubygems', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Cargo', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Hackage', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Hex', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Homebrew', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Sublime', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Elm', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Alcatraz', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'PyPI', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'CocoaPods', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'CPAN', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Meteor', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'NuGet', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'PlatformIO', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'SwiftPM', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'conda', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'Haxelib', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
    elif re.findall(r'PureScript', element, flags=re.IGNORECASE):
        Filter_list.append(element)
        PM_post_count.append(df2['PM_post_count'][i])
        total_post_SO.append(df2['total_post_SO'][i])
        TRT.append(df2['TRT'][i])
        TST.append(df2['TST'][i])
   

#print("-------------------------------------\n")
        
#print("Total number of tags:%s"%len(Final_Tags))

dict={'Filter_list':Filter_list,'PM_post_count':PM_post_count,'total_post_SO':total_post_SO,'TRT':TRT, 'TST':TST  }
df = pd.DataFrame(dict) 
df.to_csv('syc05_filtered_tag_used_for_data_extraction.csv', header=True, index=False, encoding='utf-8') 

