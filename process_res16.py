import pandas as pd
import numpy as np
import csv
import pickle
import json

label_dic={
    'POS':'positive',
    'NEG':'negative',
    'NEU':'neutral'
}
data_path="./res16_val.json"

save_path='/mnt/workspace/unimer/datas/absa16_val.pkl'
data_new=[]
texts=[]
labels=[]
terms=[]

with open(data_path, 'r') as fcc_file:
    data = json.load(fcc_file)
for d in data:
    texts.append(d['raw_words'])
    term=""
    label=""
    for l in d['aspects']:
        if l['polarity'] not in ['POS','NEU','NEG']:
            print(l['polarity'])
        term +=' '.join(l['term'])+"<sep>"
        label +=label_dic[l['polarity']]+"<sep>"
    terms.append(term)
    labels.append(label)

for i in range(len(texts)):
    data_dict={
        'audio_features':'noaudio',
        'image_features':'noimg',
        'text':texts[i],
        'label':labels[i],
        'task_type':'absa',
        'speaker':'noone',
        'context':'nocontext',
        'data_id':'absa16',
        'term':terms[i]
    }
    data_new.append(data_dict)
print(len(data_new))
print(data_new[0])
with open(save_path, 'wb') as handle:
    pickle.dump(data_new, handle)