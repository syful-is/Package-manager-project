# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:58:44 2020

@author: SE
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:57:13 2020

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

df_PM=pd.read_csv("1_RQ2_LDA_topics_mapped_by_major_minor_detail_27_6_20.csv", low_memory=False)


 
gk = df_PM.groupby('Semi_major') 

#"""

Ruby=[]
Java=[]
Perl=[]
Others=[]
Python=[]
Golang=[]
R=[]
Multi=[]
JavaScript=[]
Julia=[]
Dart=[]
Php=[]
Elm=[]

Topic=[]

#no of posts after manual categorization
 
n_Ruby=13189
n_Java=74557
n_Perl=1127
n_Others=639
n_Python=999
n_Golang=42025
n_R=550
n_Multi=20832
n_JavaScript=60475
n_Julia=6098
n_Dart=463
n_Php=242
n_Elm=1574




for i in range(0, 10):
    Topic.append(i)
    data=gk.get_group(i)
    df4=data.reset_index()
    
    
    Ruby_1=[]
    Java_1=[]
    Perl_1=[]
    Others_1=[]
    Python_1=[]
    Golang_1=[]
    R_1=[]
    Multi_1=[]
    JavaScript_1=[]
    Julia_1=[]
    Dart_1=[]
    Php_1=[]
    Elm_1=[]
  
    
    for j in range(0, len(df4)):
       
        if df4['post_language'][j]=='Ruby':
            Ruby_1.append('Ruby')
        if df4['post_language'][j]=='Java':
            Java_1.append('Java')
        if df4['post_language'][j]=='Perl':
            Perl_1.append('Perl')
        if df4['post_language'][j]=='Others':
            Others_1.append('Others')   
        if df4['post_language'][j]=='Python':
            Python_1.append('Python')
        if df4['post_language'][j]=='Golang':
            Golang_1.append('Go')
        if df4['post_language'][j]=='R':
            R_1.append('R')   
        if df4['post_language'][j]=='Multi':
            Multi_1.append('Multi')
        if df4['post_language'][j]=='JavaScript':
            JavaScript_1.append('JavaScript')
        if df4['post_language'][j]=='Julia':
            Julia_1.append('Julia')
        if df4['post_language'][j]=='Dart':
            Dart_1.append('Dart')
        if df4['post_language'][j]=='Php':
            Php_1.append('php')
        if df4['post_language'][j]=='Elm':
            Elm_1.append('Elm')
        
    
    Ruby.append((len(Ruby_1)/n_Ruby)*100)
    Java.append((len(Java_1)/n_Java)*100)
    Perl.append((len(Perl_1)/n_Perl)*100)
    Others.append((len(Others_1)/n_Others)*100)
    Python.append((len(Python_1)/n_Python)*100)
    
    Golang.append((len(Golang_1)/n_Golang)*100)
    R.append((len(R_1)/n_R)*100)
    Multi.append((len(Multi_1)/n_Multi)*100)
    JavaScript.append((len(JavaScript_1)/n_JavaScript)*100)
    Julia.append((len(Julia_1)/n_Julia)*100)
    Dart.append((len(Dart_1)/n_Dart)*100)
    Php.append((len(Php_1)/n_Php)*100)
    Elm.append((len(Elm_1)/n_Elm)*100)

    
dict={'Topic':Topic,'Ruby':Ruby, 'Java':Java, 'Perl':Perl, 'Others':Others, 'Python':Python, 'Golang':Golang, 'R':R, 'Multi':Multi,'JavaScript':JavaScript,'Julia':Julia, 'Dart': Dart,  'PhP':Php, 'Elm':Elm }

LDA_data=pd.DataFrame(dict)

LDA_data.to_csv("topic_10_language_mapping_27_6_2020.csv")    

        
#"""

