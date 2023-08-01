import pickle
import csv
import os 
import pandas as pd
import numpy as np
class TaskType:
    ERC = 'erc'
    MSA = 'msa'
    EMOJI = 'emoji'

data_path='./mosi_data_0610.pkl'
text_path='./mosi/test.tsv'
save_path='/mnt/workspace/unimer/datas/mosi_test.pkl'
#data for pretraining
data_new=[]
text=[]
label=[]
with open(data_path, 'rb') as fp:
    data = pickle.load(fp)
df_train=pd.read_csv(text_path,delimiter='\t')
text=df_train['text'].values.tolist()

label=df_train['label'].values.tolist()
s_label=[]
for i in range(len(label)):
    if label[i]<0:
        s_label.append('negative')
    elif label[i]>0:
        s_label.append('positive')
    else:
        s_label.append('neutral')

for i in range(len(data['test']['audio'])):
    data_dict={
        'audio_features':data['test']['audio'][i],
        'image_features':data['test']['vision'][i],
        'text':text[i],
        'label':label[i],
        's_label':s_label[i],
        'task_type':TaskType.MSA,
        'speaker':"noone",
        'context':"nocontext"
    }
    data_new.append(data_dict)
print(len(data_new))
print(data_new[0])
with open(save_path, 'wb') as handle:
    pickle.dump(data_new, handle)