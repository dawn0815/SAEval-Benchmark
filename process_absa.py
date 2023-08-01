import xml.etree.cElementTree as ET
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
path1 = './lap14_valid.xml'
path2 = './res14_valid.xml'

save_path='/mnt/workspace/unimer/datas/absa14_val.pkl'
data_new=[]

tree = ET.parse(path1)
root = tree.getroot()
texts=[]
terms=[]
labels=[]
for sentence in root.findall('.//aspectTerms/..'):
    texts.append(sentence.find('text').text)
    aspectTerms=sentence.find('aspectTerms')
    term=""
    label=""
    for aspectTerm in aspectTerms.findall('aspectTerm'):
        te=aspectTerm.get('term')
        te=te.replace('"', '')
        term += te+"<sep>"
        label += str(aspectTerm.get('polarity'))+"<sep>"
        if str(aspectTerm.get('polarity')) in ['None']:
            print(sentence.find('text').text)
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
        'data_id':'absa14',
        'term':terms[i]
    }
    data_new.append(data_dict)

tree = ET.parse(path2)
root = tree.getroot()
texts=[]
labels=[]
terms=[]
for sentence in root.findall('.//aspectTerms/..'):
    texts.append(sentence.find('text').text)
    aspectTerms=sentence.find('aspectTerms')
    term=""
    label=""
    for aspectTerm in aspectTerms.findall('aspectTerm'):
        te=aspectTerm.get('term')
        te=te.replace('"', '')
        term += te+"<sep>"
        label += str(aspectTerm.get('polarity'))+"<sep>"
        if str(aspectTerm.get('polarity')) in ['None']:
            print(sentence.find('text').text)
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
        'data_id':'absa14',
        'term':terms[i]
    }
    data_new.append(data_dict)

print(len(data_new))

with open(save_path, 'wb') as handle:
    pickle.dump(data_new, handle)
    


