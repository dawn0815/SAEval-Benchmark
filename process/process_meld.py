import pickle
import csv
import os 
import pandas as pd
class TaskType:
    ERC = 'erc'
    MSA = 'msa'
    EMOJI = 'emoji'

data_path='./meld_data_0610.pkl'
text_path='./meld_data_train.csv'
save_path='/mnt/workspace/unimer/datas/meld_pretrain.pkl'
data_new=[]


with open(data_path, 'rb') as fp:
    data = pickle.load(fp)
df_train=pd.read_csv(text_path)


text=df_train['text'].values.tolist()
context=df_train['context'].tolist()
speaker=df_train['speaker'].values.tolist()
labels=df_train['label'].values.tolist()
index=df_train['index'].values.tolist()

for i in range(len(labels)):
    if labels[i]=='sadness':
        labels[i]='sad'
    elif labels[i]=='anger':
        labels[i]='angry'

print(context[6])
for i in range(len(text)):
    vid_cid = df_train.loc[i]['vid_cid']
    data_dict={
        'audio_features':data['audio'][0][vid_cid],
        'image_features':data['video'][0][vid_cid],
        'text':text[i],
        'label':labels[i],
        'task_type':TaskType.ERC,
        'speaker':speaker[i],
        'context':context[i],
        'index':index[i]
    }
    data_new.append(data_dict)
print(len(data_new))

with open(save_path, 'wb') as handle:
    pickle.dump(data_new, handle)
