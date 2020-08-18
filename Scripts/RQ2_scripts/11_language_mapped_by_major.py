

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

df_PM=pd.read_csv("RQ2_LDA_topics_mapped_detail_15_6_20_version_2.csv", low_memory=False)

df_PM_topics=pd.read_csv("syc08_PM_all_question_post_12_6_20.csv", low_memory=False)

gk = df_PM.groupby('Major_cat') 



Csharp_NET=[]
Dart=[]
elm=[]
GO=[]
Java=[]
JavaScript=[]
Julia=[]
Multi=[]
Perl=[]
php=[]
Python=[]
R=[]
Ruby=[]
Cross_lang=[]

Topic=[]

#no of posts after manual categorization
 
n_Csharp_NET=9990
n_Dart=465
n_elm=1573
n_GO=42019
n_Java= 74559
n_JavaScript=60466
n_Julia=6096
n_Multi=645
n_Perl=1128
n_php=241
n_Python=1004
n_R=551
n_Ruby=13181
n_Cross_lang=10852




for i in range(0, 10):
    Topic.append(i)
    data=gk.get_group(i)
    df4=data.reset_index()
    
    
    Csharp_NET_1=[]
    Dart_1=[]
    elm_1=[]
    GO_1=[]
    Java_1=[]
    JavaScript_1=[]
    Julia_1=[]
    Multi_1=[]
    Perl_1=[]
    php_1=[]
    Python_1=[]
    R_1=[]
    Ruby_1=[]
    Crosslang_1=[]
  
    
    for j in range(0, len(df4)):
       
        if df4['post_language'][j]=='.NET':
            Csharp_NET_1.append('.NET')
        if df4['post_language'][j]=='Dart':
            Dart_1.append('Dart')
        if df4['post_language'][j]=='Elm':
            elm_1.append('elm')
        if df4['post_language'][j]=='Golang':
            GO_1.append('GO')
        if df4['post_language'][j]=='Java':
            Java_1.append('Java')
        if df4['post_language'][j]=='JavaScript':
            JavaScript_1.append('JavaScript')
        if df4['post_language'][j]=='Julia':
            Julia_1.append('Julia')
        if df4['post_language'][j]=='Multi':
            Multi_1.append('Multi')
        if df4['post_language'][j]=='Perl':
            Perl_1.append('Perl')
        if df4['post_language'][j]=='Php':
            php_1.append('php')
        if df4['post_language'][j]=='Python':
            Python_1.append('Python')
        if df4['post_language'][j]=='R':
            R_1.append('R')
        if df4['post_language'][j]=='Ruby':
            Ruby_1.append('Ruby')
        if df4['post_language'][j]=='Cross-lang':
            Crosslang_1.append('C')
    
    Csharp_NET.append((len(Csharp_NET_1)/n_Csharp_NET)*100)
    Dart.append((len(Dart_1)/n_Dart)*100)
    elm.append((len(elm_1)/n_elm)*100)
    GO.append((len(GO_1)/n_GO)*100)
    Java.append((len(Java_1)/n_Java)*100)
    JavaScript.append((len(JavaScript_1)/n_JavaScript)*100)
    Julia.append((len(Julia_1)/n_Julia)*100)
    Multi.append((len(Multi_1)/n_Multi)*100)
    Perl.append((len(Perl_1)/n_Perl)*100)
    php.append((len(php_1)/n_php)*100)
    Python.append((len(Python_1)/n_Python)*100)
    R.append((len(R_1)/n_R)*100)
    Ruby.append((len(Ruby_1)/n_Ruby)*100)
    Cross_lang.append((len(Crosslang_1)/n_Cross_lang)*100)
    
dict={'Topic':Topic,'Csharp_NET':Csharp_NET, 'Dart':Dart, 'elm':elm, 'GO':GO, 'Java':Java,'JavaScript':JavaScript,'Julia':Julia,'Multi':Multi,'Perl':Perl,  'php':php, 'Python':Python, 'R':R, 'Ruby':Ruby, 'Cross_lang':Cross_lang  }

LDA_data=pd.DataFrame(dict)

LDA_data.to_csv("Dendogram_topic_15_languageSemiMajor_mapping_15_6_2020.csv")    

        


