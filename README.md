# SAEval-Benchmark

<div align="center">
<strong>Zaijing Li, Ting-En Lin, Yuchuan Wu, Meng Liu, Fengxiao Tang†, Ming Zhao†, Yongbin Li† </strong>
</div>
<div align="center">
Central South University, Alibaba Group
</div>
<div align="center">
† Corresponding Author
</div>

[[Paper]](https://dl.acm.org/doi/10.1145/3581783.3612336) [[Codes]](https://github.com/dawn0815/UniSA) [[Benchmark]](https://github.com/dawn0815/SAEval-Benchmark)

The SAEval is a benchmark for sentiment analysis to evaluate the model's performance on various subtasks. All datasets were standardized to the same format and divided into training, validation and test sets.

## SAEval: The Benchmark
In order to study the differences and connections between the various sub-tasks of sentiment analysis, we reorganize the sentiment analysis subtasks into two categories, namely main tasks and downstream tasks, based on their relevance to sentiment. 

As shown in Figure below, the main tasks, which are the subtasks most correlated with human emotional representation, including **emotion recognition in conversation (ERC)**, **multimodal sentiment analysis (MSA)**, **aspect-based sentiment analysis (ABSA)**, and **comment analysis (CA)**. Downstream tasks include tasks related to sentiment analysis but not necessarily detecting human emotion categories, such as **irony detection**, **humor detection**, and **emoji prediction**.

![image](https://github.com/dawn0815/SAEval-Benchmark/blob/master/p2.png)

In this project, we compose four main tasks into a new sentiment analysis benchmark, SAEval, with a total of 12 datasets constituting it. The figure below shows the statistics of our SAEval benchmark, where T, A, and V represent text, acoustic, and visual, respectively.

![image](https://github.com/dawn0815/SAEval-Benchmark/blob/master/p1.png)

### ERC
Emotion recognition in conversation (ERC) aims to identify the speaker's emotion from multiple utterances in a conversation. [IEMOCAP](https://sail.usc.edu/iemocap/) and [MELD](https://github.com/declare-lab/MELD) are both multimodal datasets. [EmoryNLP](https://github.com/emorynlp/character-mining), [DailyDialog](http://yanran.li/dailydialog), and [EmoWOZ](https://zenodo.org/record/6506504) are textual datasets. The SAEval benchmark uses these datasets to identify the emotion category of each utterance based on the multimodal information (if available) and context available.

### MSA
Multimodal sentiment analysis (MSA) involves identifying the speaker's emotion from a single-turn utterance by considering multiple modalities. [MOSI](http://multicomp.cs.cmu.edu/resources/cmu-mosi-dataset/) and [MOSEI](http://multicomp.cs.cmu.edu/resources/cmu-mosei-dataset/) are two widely used multimodal sentiment analysis datasets. The goal of SAEval for these two datasets is to predict the sentiment score, which is a continuous value ranging from -3 to +3, of single-turn utterances by incorporating multiple modalities. 

### ABSA
Aspect-based sentiment analysis (ABSA) is a task that aims to identify the sentiment polarity associated with aspect terms in a single-turn utterance. [SemEval-2014](https://alt.qcri.org/semeval2014/task4/#) and [SemEval-2016](https://alt.qcri.org/semeval2016/) are subtasks of the Semeval Aspect-based Sentiment Analysis challenge. The goal of these subtasks is to identify the sentiment polarity (positive, negative, neutral, conflict) corresponding to all attribute words contained in each sentence. 

### CA
Comment analysis (CA) involves identifying the user's emotion from one or more sentences in a comment. [SST-2](https://nlp.stanford.edu/sentiment/), [IMDB](https://ai.stanford.edu/~amaas/data/sentiment/), and [AmazonReview](https://nijianmo.github.io/amazon/index.html) are datasets for comment analysis.  The goal of SAEval for these datasets is to identify the sentiment polarity of comments. **It is important to note that AmazonReview is only used for the pre-training and does not have a test set for evaluation in SAEval.**

## Formatted Data
All datasets are unified and stored in a dictionary format. The dictionary includes specific-task/dataset keywords, such as ``Task Type``, ``Dataset ID``. Different modal features is distinguished by keywords such as ``Text``, ``Audio``, and ``Image``. For ERC datasets, additional information such as ``Context``, ``Speaker ID``, and ``Utterance index`` are included to determine the conversation information of the current query.

Here are some examples of formatted data, with all datasets processed based on the same rules.

![image](https://github.com/dawn0815/SAEval-Benchmark/blob/master/p3.png)

![image](https://github.com/dawn0815/SAEval-Benchmark/blob/master/p4.png)

### Process
Limitted by the license of the original datasets, you should get the license and download the original datasets, then process datas using scripts (process_{name_of_dataset}.py) we provided. 

1. datasets for pretrain-stage-2/fine-tune
   
   ```
    python process_{dataset_name}.py
   ```
   
**You need to modify the dataset path to get training set, validation set, and test set file of each dataset**

Thanks [UniMSE](https://github.com/LeMei/UniMSE) for their contribution, you can download the multimodal features of [MOSI](http://multicomp.cs.cmu.edu/resources/cmu-mosi-dataset/), [MOSEI](http://multicomp.cs.cmu.edu/resources/cmu-mosei-dataset/), [IEMOCAP](https://sail.usc.edu/iemocap/) and [MELD](https://github.com/declare-lab/MELD), according to this [link](https://github.com/LeMei/UniMSE).

2. datasets for pretrain-stage-1
   
   ```
    python process_concat.py
   ```

### Download

**Note that you need to obtain a license to download the raw data before downloading the formatted data we provide.** The link to download the formatted data will be updated soon!

## Evaluating Your System
For evaluating your system, you just need an individual predictions file for the benchmark. Here are the experimental results of [UniSA](https://arxiv.org/abs/2309.01339), the first baseline for multi-tasks unified molding of sentiment analysis, on SAEval compared to SOTA models of various subtasks.

![image](https://github.com/dawn0815/SAEval-Benchmark/blob/master/p5.png)

We encourage more researchers to join the study on multi-tasks unified modeling for sentiment analysis, and contribute their wisdom to build sentiment intelligence.

## Citing SAEval
If you use SAEval in your research, please use the following `bib` entry to cite the paper.
```
@inproceedings{li-unisa,
author = {Li, Zaijing and Lin, Ting-En and Wu, Yuchuan and Liu, Meng and Tang, Fengxiao and Zhao, Ming and Li, Yongbin},
title = {UniSA: Unified Generative Framework for Sentiment Analysis},
year = {2023},
publisher = {Association for Computing Machinery},
url = {https://doi.org/10.1145/3581783.3612336},
booktitle = {Proceedings of the 31st ACM International Conference on Multimedia},
pages = {6132–6142},
numpages = {11},
series = {MM '23}
}
```

## License
SAEval is released without any restrictions but restrictions may apply to individual tasks (which are derived from existing datasets). We refer users to the original licenses accompanying each dataset.


## Citing Original Datasets

If you use any of the SAEval datasets, please cite their original publications:

#### MELD:
```
@inproceedings{poria2019meld,
  title={MELD: A Multimodal Multi-Party Dataset for Emotion Recognition in Conversations},
  author={Poria, Soujanya and Hazarika, Devamanyu and Majumder, Navonil and Naik, Gautam and Cambria, Erik and Mihalcea, Rada},
  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
  pages={527--536},
  year={2019}
}
```
#### IEMOCAP:
```
@article{busso2008iemocap,
  title={IEMOCAP: Interactive emotional dyadic motion capture database},
  author={Busso, Carlos and Bulut, Murtaza and Lee, Chi-Chun and Kazemzadeh, Abe and Mower, Emily and Kim, Samuel and Chang, Jeannette N and Lee, Sungbok and Narayanan, Shrikanth S},
  journal={Language resources and evaluation},
  volume={42},
  pages={335--359},
  year={2008},
  publisher={Springer}
}
```
#### DailyDialog:
```
@article{li2017dailydialog,
  title={Dailydialog: A manually labelled multi-turn dialogue dataset},
  author={Li, Yanran and Su, Hui and Shen, Xiaoyu and Li, Wenjie and Cao, Ziqiang and Niu, Shuzi},
  journal={arXiv:1710.03957},
  year={2017}
}
```
#### EmoWoz:
```
@inproceedings{feng2022emowoz,
  title={EmoWOZ: A Large-Scale Corpus and Labelling Scheme for Emotion Recognition in Task-Oriented Dialogue Systems},
  author={Feng, Shutong and Lubis, Nurul and Geishauser, Christian and Lin, Hsien-Chin and Heck, Michael and van Niekerk, Carel and Gasic, Milica},
  booktitle={Proceedings of the Thirteenth Language Resources and Evaluation Conference},
  pages={4096--4113},
  year={2022}
}
```
#### EmoryNLP:
```
@article{zahiri2017emotion,
  title={Emotion detection on tv show transcripts with sequence-based convolutional neural networks},
  author={Zahiri, Sayyed M and Choi, Jinho D},
  journal={arXiv:1708.04299},
  year={2017}
}
```

#### MOSI:
```
@article{zadeh2016mosi,
  title={Mosi: multimodal corpus of sentiment intensity and subjectivity analysis in online opinion videos},
  author={Zadeh, Amir and Zellers, Rowan and Pincus, Eli and Morency, Louis-Philippe},
  journal={arXiv:1606.06259},
  year={2016}
}
```
#### MOSEI:
```
@inproceedings{zadeh2018multimodal,
  title={Multimodal language analysis in the wild: Cmu-mosei dataset and interpretable dynamic fusion graph},
  author={Zadeh, AmirAli Bagher and Liang, Paul Pu and Poria, Soujanya and Cambria, Erik and Morency, Louis-Philippe},
  booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages={2236--2246},
  year={2018}
}
```

#### SemEval-2014:
```
@inproceedings{pontiki-etal-2014-semeval,
    title = "{S}em{E}val-2014 Task 4: Aspect Based Sentiment Analysis",
    author = "Pontiki, Maria  and
      Galanis, Dimitris  and
      Pavlopoulos, John  and
      Papageorgiou, Harris  and
      Androutsopoulos, Ion  and
      Manandhar, Suresh",
    booktitle = "Proceedings of the 8th International Workshop on Semantic Evaluation ({S}em{E}val 2014)",
    month = aug,
    year = "2014",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    doi = "10.3115/v1/S14-2004",
    pages = "27--35",
}
```
#### SemEval-2016:
```
@inproceedings{pontiki2016semeval,
  title={Semeval-2016 task 5: Aspect based sentiment analysis},
  author={Pontiki, Maria and Galanis, Dimitris and Papageorgiou, Haris and Androutsopoulos, Ion and Manandhar, Suresh and AL-Smadi, Mohammed and Al-Ayyoub, Mahmoud and Zhao, Yanyan and Qin, Bing and De Clercq, Orph{\'e}e and others},
  booktitle={ProWorkshop on Semantic Evaluation (SemEval-2016)},
  pages={19--30},
  year={2016},
  organization={Association for Computational Linguistics}
}
```

#### IMDB:
```
@InProceedings{imdb,
  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
}
```
#### SST-2:
```
@inproceedings{socher2013recursive,
  title={Recursive deep models for semantic compositionality over a sentiment treebank},
  author={Socher, Richard and Perelygin, Alex and Wu, Jean and Chuang, Jason and Manning, Christopher D and Ng, Andrew Y and Potts, Christopher},
  booktitle={Proceedings of the 2013 conference on empirical methods in natural language processing},
  pages={1631--1642},
  year={2013}
}
```
#### AmazonReview:
```
@inproceedings{ni2019justifying,
  title={Justifying recommendations using distantly-labeled reviews and fine-grained aspects},
  author={Ni, Jianmo and Li, Jiacheng and McAuley, Julian},
  booktitle={Proceedings of the 2019 conference on empirical methods in natural language processing and the 9th international joint conference on natural language processing (EMNLP-IJCNLP)},
  pages={188--197},
  year={2019}
}
```
