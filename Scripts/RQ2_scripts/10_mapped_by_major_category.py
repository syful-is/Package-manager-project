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
BOWER=[]

Topic=[]

#no of posts after manual categorization
 
n_RUBYGEMS=9548
n_Maven=74557
n_CPAN=1127
n_PM=639
n_PYPI=999
n_GO=42025
n_CRAN=550
n_PUPPET=3641
n_NUGET=9976
n_NPM=29414
n_JULIA=6098
n_METEOR= 28158
n_PUB=463
n_PACKAGIST=242
n_BOWER=2903
n_ELM=1574
n_CONDA=10856
 

for i in range(0, 3):
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
    BOWER_1=[]
    ELM_1=[]
    CONDA_1=[]
    
    for j in range(0, len(df4)):
        if df4['post_category'][j]=='RubyGems':
            RUBYGEMS_1.append('RUBYGEMS')
        if df4['post_category'][j]=='Maven':
            Maven_1.append('Maven')
        if df4['post_category'][j]=='CPAN':
            CPAN_1.append('CPAN')
        if df4['post_category'][j]=='PM':
            PM_1.append('PM')
        if df4['post_category'][j]=='PyPI':
            PYPI_1.append('PYPI')
        if df4['post_category'][j]=='Go':
            GO_1.append('GO')
        if df4['post_category'][j]=='CRAN':
            CRAN_1.append('CRAN')
        if df4['post_category'][j]=='Puppet':
            PUPPET_1.append('PUPPET')
        if df4['post_category'][j]=='Nuget':
            NUGET_1.append('NUGET')
        if df4['post_category'][j]=='npm':
            NPM_1.append('NPM')
        if df4['post_category'][j]=='Julia':
            JULIA_1.append('JULIA')
        if df4['post_category'][j]=='Meteor':
            METEOR_1.append('METEOR')
        if df4['post_category'][j]=='Pub':
            PUB_1.append('PUB')
        if df4['post_category'][j]=='Packagist':
            PACKAGIST_1.append('PACKAGIST')
        if df4['post_category'][j]=='Bower':
            BOWER_1.append('BOWER')
        if df4['post_category'][j]=='Elm':
            ELM_1.append('ELM')
        if df4['post_category'][j]=='Conda':
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
    BOWER.append((len(BOWER_1)/n_BOWER)*100)
    ELM.append((len(ELM_1)/n_ELM)*100)
    CONDA.append((len(CONDA_1)/n_CONDA)*100)
    
dict={'Topic':Topic,'RubyGems':RUBYGEMS, 'Maven':Maven, 'CPAN':CPAN, 'PM':PM, 'PyPI':PYPI,'Go':GO,'CRAN':CRAN,  'Puppet':PUPPET, 'Nuget':NUGET, 'npm':NPM, 'Julia':JULIA, 'Meteor':METEOR, 'Pub':PUB, 'Packagist':PACKAGIST, 'Bower':BOWER, 'Elm':ELM, 'Conda':CONDA   }

LDA_data=pd.DataFrame(dict)

LDA_data.to_csv("topic_3_PM_mapping_result_27_6_2020.csv")  