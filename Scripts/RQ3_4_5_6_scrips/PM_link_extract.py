# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 10:50:42 2020

@author: SE
"""

import gzip  
import csv  
import pandas as pd
import matplotlib.pyplot as plt
import re
import tldextract
import os

#Please specify your dataset directory. 
os.chdir("your dataset directory")


file1="PM_Maven_all_questions.csv"
 
df1 = pd.read_csv(file1, low_memory=False)
#df2 = pd.read_csv(file2, low_memory=False)

QId=[]
Ans_id=[]
Title=[]
Link=[]
Cause=[]
Question=[]
Q_Body=[]
AcceptedAnswerId=[]
AnswerCount=[]
Ans_body=[]
Ques_CreationDate=[]
Ans_CreationDate=[]
Q_link=[]
A_link=[]



Qlink=[]
Alink=[]

All_qlink=[]
All_alink=[]
test=[]
for i in range(0, len(df1)):
    QId.append(df1['QId'][i])
    Ans_id.append(df1['Ans_id'][i])
    Title.append(df1['Title'][i])
    Q_Body.append(df1['Q_Body'][i])
    Ans_body.append(df1['Ans_body'][i])
    Ques_CreationDate.append(df1['Ques_CreationDate'][i])
    Ans_CreationDate.append(df1['Ans_CreationDate'][i])
    Cause.append(df1['Cause'][i])
    Question.append(df1['Question'][i])
    AcceptedAnswerId.append(df1['AcceptedAnswerId'][i])
    AnswerCount.append(df1['AnswerCount'][i])
    Q_link.append(re.findall(r'(https?://\S+)', df1['Q_Body'][i]))
    A_link.append(re.findall(r'(https?://\S+)', df1['Ans_body'][i]))
    """
    Q=re.findall(r'(?:http:\/\/|www\.|https:\/\/)([^\/]+)', df1['Q_Body'][i])
    A=re.findall(r'(?:http:\/\/|www\.|https:\/\/)([^\/]+)', df1['Ans_body'][i])
    Q_link.append(Q)
    A_link.append(A)
    
    if len(Q)>0:
        test.append(len(Q))
        for k in range(0, len(Q)):
            All_qlink.append(Q[k])
                
     
    if len(A)>0:
        test.append(len(A))
        for k in range(0, len(A)):
            All_alink.append(A[k])
        
    """
    
    
dict={'QId':QId,'Q_link':Q_link,'A_link':A_link, 'Ans_id':Ans_id,'Ans_body':Ans_body,'Ques_CreationDate':Ques_CreationDate, 'Ans_CreationDate':Ans_CreationDate, 'Title':Title,'Q_Body':Q_Body, 'Cause':Cause, 'Question':Question, 'AcceptedAnswerId':AcceptedAnswerId, 'AnswerCount':AnswerCount  }

data=pd.DataFrame(dict)

data.to_csv("PM_Maven_all_links.csv")


