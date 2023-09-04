import pickle
import csv
import os 
import pandas as pd
class TaskType:
    ERC = 'erc'
    MSA = 'msa'
    EMOJI = 'emoji'

data_path='./iemocap_data_0610.pkl'
text_path='./iemocap_data_train.csv'
save_path='/mnt/workspace/unimer/datas/iemocap_pretrain.pkl'
data_new=[]
label_sets={
    'fru':'frustrate',
    'neu':'neutral',
    'ang':'angry',
    'sad':'sad',
    'exc':'excited',
    'hap':'happy'
}
with open(data_path, 'rb') as fp:
    data = pickle.load(fp)
df_train=pd.read_csv(text_path)

df_train=df_train[df_train['label'].isin(['fru', 'neu', 'ang', 'sad', 'exc', 'hap'])]
text=df_train['text'].values.tolist()
context=df_train['context'].values.tolist()
speaker=df_train['speaker'].values.tolist()
labels=df_train['label'].values.tolist()
index=df_train['index'].values.tolist()

for i in range(len(labels)):
    labels[i]=label_sets[labels[i]]
print(context[6])
for i in range(len(text)):
    vid_cid = df_train.iloc[i]['vid_cid']
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
