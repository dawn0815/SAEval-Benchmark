import pickle
import csv
import os 
import pandas as pd
import numpy as np
class TaskType:
    ERC = 'erc'
    MSA = 'msa'
    COMMENT = 'comment'


text_path='./aclImdb/imdb_train.csv'
save_path='/mnt/workspace/unimer/datas/imdb_pretrain.pkl'
data_new=[]
text=[]
label=[]
df_train=pd.read_csv(text_path)
text=df_train['text'].values.tolist()

label=df_train['label'].values.tolist()
s_label=[]
for i in range(len(label)):
    if label[i]==0:
        label[i]=float(-1.0)
        s_label.append('negative')
    else:
        label[i]=float(1.0)
        s_label.append('positive')
for i in range(len(text)):
    data_dict={
        'audio_features':'noaudio',
        'image_features':'noimg',
        'text':text[i],
        'label':label[i],
        's_label':s_label[i],
        'task_type':TaskType.COMMENT,
        'speaker':'noone',
        'context':'nocontext'
    }
    data_new.append(data_dict)
print(len(data_new))
print(data_new[0])
with open(save_path, 'wb') as handle:
    pickle.dump(data_new, handle)