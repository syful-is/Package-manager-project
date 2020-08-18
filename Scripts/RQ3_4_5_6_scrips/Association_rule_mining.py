# -*- coding: utf-8 -*-
"""
Created on Fri May 22 21:38:41 2020

@author: SE
"""


import gzip  
import csv  
import pandas as pd
import matplotlib.pyplot as plt
from tqdm.auto import tqdm
import re
import tldextract
from mlxtend.preprocessing import TransactionEncoder
import os

#Please specify your dataset directory. 
os.chdir("your dataset directory")

name="Maven"

#for 5 support as threshold
#support for Maven=0.001
#support for Npm=0.00244
#support for Nuget=0.0044

file1="PM_All_Answer_%s.csv"%(name)
 
df1 = pd.read_csv(file1, low_memory=False)

#"""
QId=[]
Ans_id=[]
Title=[]
Link=[]
Cause=[]
Question=[]
Ques_Body=[]
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
    if df1['Ans_id'][i]==df1['AcceptedAnswerId'][i]:
        QId.append(df1['QId'][i])
        Ans_id.append(df1['Ans_id'][i])
        Title.append(df1['Title'][i])
        #Ques_Body.append(df1['Ques_Body'][i])
        
        q=re.sub('<code>.*?</code>','',df1['Ques_Body'][i], flags=re.DOTALL)
        Ques_Body.append(q)
        a=re.sub('<code>.*?</code>','',df1['Ans_body'][i], flags=re.DOTALL)
        Ans_body.append(a)
        #Ans_body.append(df1['Ans_body'][i])
        Ques_CreationDate.append(df1['Ques_CreationDate'][i])
        Ans_CreationDate.append(df1['Ans_CreationDate'][i])
        #Cause.append(df1['Cause'][i])
        #Question.append(df1['Question'][i])
        AcceptedAnswerId.append(df1['AcceptedAnswerId'][i])
        AnswerCount.append(df1['AnswerCount'][i])
        
        Q=re.findall(r'(?:http:\/\/|www\.|https:\/\/)([^\/]+)',q)
        A=re.findall(r'(?:http:\/\/|www\.|https:\/\/)([^\/]+)', a)
        Q_link.append(Q)
        A_link.append(A)
        


        
P_link=[]   
for index, j in enumerate(Q_link):
    link=set(Q_link[index])
    linkA=set(A_link[index])
    
    #link=Q_link[index]
    #linkA=A_link[index]
    
    temp=[]
    temp1=[]
    temp2=[]
    for k in link:
        m=k.replace('&lt;','')
        temp.append("Q_%s"%m)
        temp1.append("Q_%s"%m)
    for l in linkA:
        n=l.replace('&lt;','')
        temp.append("A_%s"%n)
        temp2.append("A_%s"%n)
    if len(temp1)>=1 and len(temp2)>=1:
        P_link.append(temp)
    #if index==13:
     #   break
#"""      
te = TransactionEncoder()
te_array = te.fit(P_link).transform(P_link)
df = pd.DataFrame(te_array, columns=te.columns_)

#Find frequently occurring itemsets using Apriori Algorithm
from mlxtend.frequent_patterns import apriori

frequent_itemsets_ap = apriori(df, min_support=0.001, use_colnames=True)

print(frequent_itemsets_ap)


from mlxtend.frequent_patterns import fpgrowth

frequent_itemsets_fp=fpgrowth(df, min_support=0.001, use_colnames=True)
print(frequent_itemsets_fp)

#Mine the Association Rules

from mlxtend.frequent_patterns import association_rules

rules_ap = association_rules(frequent_itemsets_ap, metric="confidence", min_threshold=0.49)
rules_fp = association_rules(frequent_itemsets_fp, metric="confidence", min_threshold=0.49)


rules_ap.to_csv("F:/1_NAIST_Research_SE/SE_meeting/PM_Stackoverflow/RQ3_answer/%s_AP_association_rules.csv"%(name))
rules_fp.to_csv("F:/1_NAIST_Research_SE/SE_meeting/PM_Stackoverflow/RQ3_answer/%s_FP_association_rules.csv"%(name))

print(rules_fp)
            

dict={'QId':QId,'Ans_id':Ans_id,'Ans_body':Ans_body,'Ques_CreationDate':Ques_CreationDate, 'Ans_CreationDate':Ans_CreationDate, 'Title':Title,'Ques_Body':Ques_Body, 'AcceptedAnswerId':AcceptedAnswerId, 'AnswerCount':AnswerCount  }

data=pd.DataFrame(dict)

data.to_csv("PM_All_Answer_%s_accepted_answer_cleaned_1.csv"%(name))

#"""
            
            
