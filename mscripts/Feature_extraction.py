#!/usr/bin/env python
# coding: utf-8

# In[21]:


import glob
#!pip install tsfresh
import tsfresh
import pandas as pd
import numpy as np
#import matplotlib.pylab as plt
#!pip install seaborn
#import seaborn as sns
from tsfresh.examples.robot_execution_failures import download_robot_execution_failures, load_robot_execution_failures
from tsfresh import extract_features, extract_relevant_features, select_features
from tsfresh.utilities.dataframe_functions import impute
from tsfresh.feature_extraction import ComprehensiveFCParameters
from sklearn.tree import DecisionTreeClassifier
#from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
import os


# In[38]:





# In[39]:





# In[3]:

total=[0,7,10,12]
# read list of all normal and abnormal files

for X in total:
  
  print(X)
  list_of_normal_files = glob.glob('/workspace/shock/eicu_imputed_corrected/cohort_'+str(X)+'hr/*Normal*.csv')
  list_of_abnormal_files = glob.glob('/workspace/shock/eicu_imputed_corrected/cohort_'+str(X)+'hr/*Abnormal*.csv')
  print(len(list_of_normal_files))
  print(len(list_of_abnormal_files))
  normal_file_list=[]
  j=0
  for f in list_of_normal_files:
    data=list_of_normal_files[j]
    k=os.path.basename(data)
    data1=pd.read_csv(f)
    #data1.head(5)
    
    data1.columns =data1.columns.str.strip().str.lower().str.replace(' ', '').str.replace('.', '').str.replace('x', '')
    data2=data1[['sao2','heartrate','respiration','systemicsystolic','systemicdiastolic']]
    
    data2.insert(0,'ID',k)
    normal_file_list.append(data2)
    j=j+1
  #data1.head(5)        
  normal_file_data_frame = pd.concat(normal_file_list, axis = 0, ignore_index = True)
  print(normal_file_data_frame.shape)
  normal_file_data_frame.head(5)
  
  
  # In[11]:
  
  
  # data_frame of abnormal file
  abnormal_file_list=[]
  j=0
  for f in list_of_abnormal_files:
    data=list_of_abnormal_files[j]
    k=os.path.basename(data)
    data1=pd.read_csv(f)
    data1.columns =data1.columns.str.strip().str.lower().str.replace(' ', '').str.replace('.', '').str.replace('x', '')
    
    data2=data1[['sao2','heartrate','respiration','systemicsystolic','systemicdiastolic']]
    data2.insert(0,'ID',k)
    abnormal_file_list.append(data2)
    j=j+1
  abnormal_file_data_frame = pd.concat(abnormal_file_list, axis = 0, ignore_index = True)
  print(abnormal_file_data_frame.shape)
  abnormal_file_data_frame.describe()        
    
  
  # In[12]:
  
  
  # merge normal and abnormal files
  frames=[normal_file_data_frame,abnormal_file_data_frame]
  merge_normal_abnormal=pd.concat(frames)
  print(merge_normal_abnormal.shape)
  merge_normal_abnormal.head()
  
  
  # In[14]:
  
  
  X_extracted = extract_features(merge_normal_abnormal, column_id='ID')
  
  
  # In[15]:
  
  
  print(X_extracted.isnull().sum().sum())
  
  
  # In[16]:
  
  
  X_impute_extracted=impute(X_extracted)
  print(X_impute_extracted.isnull().sum().sum())
  
  
  # In[17]:
  
  
  X_impute_extracted.head(5)
  
  
  # In[18]:
  
  import pathlib
  pathlib.Path('/workspace/shock/eicu_imputed_corrected/Modeling_'+str(X)+'hr/').mkdir(parents=True, exist_ok=True) 
  output='/workspace/shock/eicu_imputed_corrected/Modeling_'+str(X)+'hr/tsfresh_features_'+str(X)+'hr_420.csv'
  X_impute_extracted.to_csv(output)
  
  
  
  
  # In[ ]:
  
  
  
  
  
  
  
  
  
  
  
  # In[ ]:
  
  
  
  
  
  # In[ ]:
  
  
  
  
  
  # In[ ]:
  
  
  
  
  
  # In[10]:
  
  
              
  
  
              # In[13]:
  
  
              
  

# In[14]:



#X_impute_extracted.columns


# In[ ]:




