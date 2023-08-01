import pickle
import csv
import os 
import pandas as pd
import numpy as np
class TaskType:
    ERC = 'erc'
    MSA = 'msa'
    EMOJI = 'emoji'


text_path='./EmoWoz/emowoz_data_train.csv'
save_path='/mnt/workspace/unimer/datas/emowoz_pretrain.pkl'
data_new=[]
text=[]
label=[]
df_train=pd.read_csv(text_path,lineterminator="\n")
text=df_train['text'].values.tolist()
context=df_train['context'].values.tolist()

label=df_train['label'].values.tolist()
index=df_train['index'].values.tolist()
speaker=df_train['speaker'].values.tolist()
print(context[6])
for i in range(len(text)):
    data_dict={
        'audio_features':'noaudio',
        'image_features':'noimg',
        'text':text[i],
        'label':label[i],
        'task_type':TaskType.ERC,
        'speaker':speaker[i],
        'context':context[i],
        'index':index[i]
    }
    data_new.append(data_dict)
print(len(data_new))
with open(save_path, 'wb') as handle:
    pickle.dump(data_new, handle)