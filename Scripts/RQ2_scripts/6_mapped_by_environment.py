# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:51:54 2020

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
RUBY_MRI=[]
JVM=[]
Perl=[]
Multi=[]
Python=[]
Gc=[]
R=[]
NET=[]
Node=[]
Julia=[]
Dart_VM=[]
Zend=[]
Elm=[]
 

Topic=[]

#no of posts after manual categorization
 
n_RUBY_MRI=13189
n_JVM=74557
n_Perl=1127
n_Multi=10856
n_Python=999
n_Gc=42025
n_R=550
n_NET=9976
n_Node=60475
n_Julia=6098
n_Dart_VM=463
n_Zend=242
n_Elm=1574
 

for i in range(0, 10):
    Topic.append(i)
    data=gk.get_group(i)
    df4=data.reset_index()
    
    RUBY_MRI1=[]
    JVM1=[]
    Perl1=[]
    Multi1=[]
    Python1=[]
    Gc1=[]
    R1=[]
    NET1=[]
    Node1=[]
    Julia1=[]
    Dart_VM1=[]
    Zend1=[]
    Elm1=[]
    
    for j in range(0, len(df4)):
        if df4['post_Enviroment'][j]=='Ruby MRI':
            RUBY_MRI1.append('Ruby MRI')
        if df4['post_Enviroment'][j]=='JVM':
            JVM1.append('JVM')
        if df4['post_Enviroment'][j]=='Perl':
            Perl1.append('Perl')
        if df4['post_Enviroment'][j]=='Multi':
            Multi1.append('Multi')
        if df4['post_Enviroment'][j]=='Python':
            Python1.append('Python')
        if df4['post_Enviroment'][j]=='Gc':
            Gc1.append('Gc')
        if df4['post_Enviroment'][j]=='R':
            R1.append('R')
        if df4['post_Enviroment'][j]=='.NET':
            NET1.append('.NET')
        if df4['post_Enviroment'][j]=='Node.js':
            Node1.append('Node.js')
        if df4['post_Enviroment'][j]=='Julia':
            Julia1.append('Julia')
        if df4['post_Enviroment'][j]=='Dart VM':
            Dart_VM1.append('Dart VM')
        if df4['post_Enviroment'][j]=='Zend Engine':
            Zend1.append('Zend Engine')
        if df4['post_Enviroment'][j]=='Elm':
            Elm1.append('Elm')
        
        

    RUBY_MRI.append((len(RUBY_MRI1)/n_RUBY_MRI)*100)
    JVM.append((len(JVM1)/n_JVM)*100)
    Perl.append((len(Perl1)/n_Perl)*100)
    Multi.append((len(Multi1)/n_Multi)*100)
    Python.append((len(Python1)/n_Python)*100)
    Gc.append((len(Gc1)/n_Gc)*100)
    R.append((len(R1)/n_R)*100)
    NET.append((len(NET1)/n_NET)*100)
    Node.append((len(Node1)/n_Node)*100)
    Julia.append((len(Julia1)/n_Julia)*100)
    Dart_VM.append((len(Dart_VM1)/n_Dart_VM)*100)
    Zend.append((len(Zend1)/n_Zend)*100)
    Elm.append((len(Elm1)/n_Elm)*100)
    
     
dict={'Topic':Topic,'Ruby MRI':RUBY_MRI, 'JVM':JVM, 'Perl':Perl, 'Multi':Multi, 'Python':Python,'Gc':Gc,'R':R,'.NET':NET,  'Node.js':Node, 'Julia':Julia, 'Dart VM':Dart_VM, 'Zend Engine':Zend, 'Elm':Elm}

LDA_data=pd.DataFrame(dict)

LDA_data.to_csv("topic_10_Environment_mapping_result_26_6_2020.csv")    

        

#"""