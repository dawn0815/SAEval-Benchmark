import random
import pandas as pd
import pickle
map_dic={}
for line in open("./mapping.txt"):
    a=line.split('\t')
    label=a[2].replace('_',' ')  
    label=label.strip()
    map_dic[a[0]]=label

labels=[]
texts=[]
data=[]
save_path='/mnt/workspace/unimer/datas/emoji_few_test.pkl'
for line in open("./test_label.txt"):
    lab=str(line).strip()
    label=map_dic[lab]
    labels.append(label)
for line in open("./test_text.txt"):
    txt=line.strip()
    texts.append(txt)

for i in range(len(texts)):
    data_dict={
        'audio_features':'noaudio',
        'image_features':'noimg',
        'text':texts[i],
        'label':labels[i],
        'task_type':'emoji',
        'speaker':"noone",
        'context':'nocontext'}
    data.append(data_dict)
print(len(data))
print(data[0])
with open(save_path, 'wb') as handle:
    pickle.dump(data, handle)