"""
it is an example for how to get the concat_dataset.
before that, you need to process orignal datasets: delete the data which labels not in [positive,negative,neutral]
and, you should process orignal AmazonReview_all dataset
"""

import pickle
def load_data(data_path):
    with open(data_path, 'rb') as fp:
        data = pickle.load(fp)
    return data
erc_s=[]
erc_m=[]
comment=[]
msa=[]
data_new=[]

#step1:load your processed datasets,add "data_id" for them
"""
Eg:
sst=load_data('./datasets/sst_pretrain.pkl')
amazon_1=load_data('./datasets/amazon_all_pretrain_1.pkl')
iemocap=load_data('./datasets/iemocap_pretrain.pkl')
meld=load_data('./datasets/meld_pretrain.pkl')
emory=load_data('./datasets/emory_pretrain.pkl')
emowoz=load_data('./datasets/emowoz_pretrain.pkl')
daily=load_data('./datasets/daily_pretrain.pkl')
mosi=load_data('./datasets/mosi_pretrain.pkl')

for d in sst:
    d['data_id']='sst'
for d in imdb:
    d['data_id']='imdb'
for d in amazon_1:
    d['data_id']='amazon'
    d['s_label']='negative'
........
"""

#step2: split data based on task_type and labels
"""
Eg:
erc_s=[]
erc_m=[]
comment=[]
msa=[]
data_new=[]

erc_m.extend(iemocap)
erc_m.extend(meld)
msa.extend(mosi)
msa.extend(mosei)
erc_s.extend(emowoz)
erc_s.extend(emory)
erc_s.extend(daily)

erc_m_p,erc_m_n,erc_m_z=[],[],[]
erc_s_p,erc_s_n,erc_s_z=[],[],[]
msa_p,msa_n,msa_z=[],[],[]
comment_p,comment_n,comment_z=[],[],[]

for d in erc_m:
    if d['s_label']=="positive":
        erc_m_p.append(d)
    elif d['s_label']=="negative":
        erc_m_n.append(d)
    elif d['s_label']=="neutral":
        erc_m_z.append(d)

for d in msa:
    if d['s_label']=="positive":
        msa_p.append(d)
    elif d['s_label']=="negative":
        msa_n.append(d)
    elif d['s_label']=="neutral":
        msa_z.append(d)
........
"""

#step3: add "concat_text" for each "task_type list" randomly
"""
import random
for i in range(len(erc_m_p)):
    idx=random.randint(0,len(comment_p)-1)
    erc_m_p[i]['concat_text']=comment_p[idx]['text']
    data_new.append(erc_m_p[i])
for i in range(len(erc_m_p)):
    idx=random.randint(0,len(msa_p)-1)
    erc_m_p[i]['concat_text']=msa_p[idx]['text']
    data_new.append(erc_m_p[i])
for i in range(len(erc_m_n)):
    idx=random.randint(0,len(comment_n)-1)
    erc_m_n[i]['concat_text']=comment_n[idx]['text']
    data_new.append(erc_m_n[i])
......
"""
#step4: save as "concat" dataset
"""
save_path="./datasets/concat_pretrain.pkl"
with open(save_path, 'wb') as handle:
    pickle.dump(data_new, handle)

"""