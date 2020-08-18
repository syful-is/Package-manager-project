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

df_PM=pd.read_csv("RQ2_LDA_topics_mapped_detail_15_6_20_version_2.csv", low_memory=False)


df_PM_topics=pd.read_csv("syc08_PM_all_question_post_12_6_20.csv", low_memory=False)

gk = df_PM.groupby('Major_cat') 


 
RUBYGEMS=[]
Maven=[]
CPAN=[]
PM=[]
PYPI=[]
GO=[]
CRAN=[]
PUPPET=[]
NUGET=[]
NPM=[]
JULIA=[]
METEOR=[]
PUB=[]
PACKAGIST=[]
ELM=[]
CONDA=[]

Topic=[]

#no of posts after manual categorization
 
n_RUBYGEMS=9540
n_Maven=74559
n_CPAN=1128
n_PM=645
n_PYPI=1004
n_GO=42019
n_CRAN=551
n_PUPPET=3641
n_NUGET=9990
n_NPM=29403
n_JULIA=6096
n_METEOR= 27944
n_PUB=465
n_PACKAGIST=241
n_ELM=1573
n_CONDA=10852

 

for i in range(0, 10):
    Topic.append(i)
    data=gk.get_group(i)
    df4=data.reset_index()
    
    EMACS_1=[]
    RUBYGEMS_1=[]
    Maven_1=[]
    CPAN_1=[]
    PM_1=[]
    HOMEBREW_1=[]
    PYPI_1=[]
    GO_1=[]
    CRAN_1=[]
    PUPPET_1=[]
    NUGET_1=[]
    NPM_1=[]
    JULIA_1=[]
    METEOR_1=[]
    PUB_1=[]
    PACKAGIST_1=[]
    ELM_1=[]
    CONDA_1=[]
    
    for j in range(0, len(df4)):
        if df4['post_category'][j]=='RUBYGEMS':
            RUBYGEMS_1.append('RUBYGEMS')
        if df4['post_category'][j]=='Maven':
            Maven_1.append('Maven')
        if df4['post_category'][j]=='CPAN':
            CPAN_1.append('CPAN')
        if df4['post_category'][j]=='PM':
            PM_1.append('PM')
        if df4['post_category'][j]=='PYPI':
            PYPI_1.append('PYPI')
        if df4['post_category'][j]=='GO':
            GO_1.append('GO')
        if df4['post_category'][j]=='CRAN':
            CRAN_1.append('CRAN')
        if df4['post_category'][j]=='PUPPET':
            PUPPET_1.append('PUPPET')
        if df4['post_category'][j]=='NUGET':
            NUGET_1.append('NUGET')
        if df4['post_category'][j]=='NPM':
            NPM_1.append('NPM')
        if df4['post_category'][j]=='JULIA':
            JULIA_1.append('JULIA')
        if df4['post_category'][j]=='METEOR':
            METEOR_1.append('METEOR')
        if df4['post_category'][j]=='PUB':
            PUB_1.append('PUB')
        if df4['post_category'][j]=='PACKAGIST':
            PACKAGIST_1.append('PACKAGIST')
        if df4['post_category'][j]=='ELM':
            ELM_1.append('ELM')
        if df4['post_category'][j]=='CONDA':
            CONDA_1.append('CONDA')
    

    RUBYGEMS.append((len(RUBYGEMS_1)/n_RUBYGEMS)*100)
    Maven.append((len(Maven_1)/n_Maven)*100)
    CPAN.append((len(CPAN_1)/n_CPAN)*100)
    PM.append((len(PM_1)/n_PM)*100)
    PYPI.append((len(PYPI_1)/n_PYPI)*100)
    GO.append((len(GO_1)/n_GO)*100)
    CRAN.append((len(CRAN_1)/n_CRAN)*100)
    PUPPET.append((len(PUPPET_1)/n_PUPPET)*100)
    NUGET.append((len(NUGET_1)/n_NUGET)*100)
    NPM.append((len(NPM_1)/n_NPM)*100)
    JULIA.append((len(JULIA_1)/n_JULIA)*100)
    METEOR.append((len(METEOR_1)/n_METEOR)*100)
    PUB.append((len(PUB_1)/n_PUB)*100)
    PACKAGIST.append((len(PACKAGIST_1)/n_PACKAGIST)*100)
    ELM.append((len(ELM_1)/n_ELM)*100)
    CONDA.append((len(CONDA_1)/n_CONDA)*100)
    
dict={'Topic':Topic,'RUBYGEMS':RUBYGEMS, 'Maven':Maven, 'CPAN':CPAN, 'GO':GO, 'PM':PM,'PYPI':PYPI,'GO':GO,'CRAN':CRAN,  'PUPPET':PUPPET, 'NUGET':NUGET, 'NPM':NPM, 'JULIA':JULIA, 'METEOR':METEOR, 'PUB':PUB, 'PACKAGIST':PACKAGIST, 'ELM':ELM, 'CONDA':CONDA   }

LDA_data=pd.DataFrame(dict)

LDA_data.to_csv("topic_15_PM_SemiMajorcat_result_5_5_2020.csv")    

        

#"""