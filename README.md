# SAEval-Benchmark
The SAEval is a benchmark for sentiment analysis to evaluate the model's performance on various subtasks. All datasets were standardized to the same format and divided into training, validation and test sets.

## SAEval: The Benchmark
In order to study the differences and connections between the various sub-tasks of sentiment analysis, we reorganize the sentiment analysis subtasks into two categories, namely main tasks and downstream tasks, based on their relevance to sentiment. As shown in Figure below, the main tasks, which are the subtasks most correlated with human emotional representation, include emotion recognition in conversation (ERC), multimodal sentiment analysis (MSA), aspect-based sentiment analysis (ABSA), and comment analysis (CA). Downstream tasks include tasks related to sentiment analysis but not necessarily detecting human emotion categories, such as irony detection, humor detection, and emoji prediction.

![pdf](https://github.com/dawn0815/SAEval-Benchmark/blob/master/p2.png)

In this project, we compose four main tasks into a new sentiment analysis benchmark, SAEval, with a total of 12 datasets constituting it. The figure below shows the statistics of our SAEval benchmark, where T, A, and V represent text, acoustic, and visual, respectively.

![image](https://github.com/dawn0815/SAEval-Benchmark/blob/master/p1.png)

### ERC
Emotion recognition in conversation aims to identify the speaker's emotion from multiple utterances in a conversation. IEMOCAP and MELD are both multimodal datasets. EmoryNLP, DailyDialog, and EmoWOZ are textual datasets. The SAEval benchmark uses these datasets to identify the emotion category of each utterance based on the multimodal information (if available) and context available.

### MSA
Multimodal sentiment analysis (MSA) involves identifying the speaker's emotion from a single-turn utterance by considering multiple modalities. MOSI and MOSEI are two widely used multimodal sentiment analysis datasets. The goal of SAEval for these two datasets is to predict the sentiment score, which is a continuous value ranging from -3 to +3, of single-turn utterances by incorporating multiple modalities. 

### ABSA
Aspect-based sentiment analysis (ABSA) is a task that aims to identify the sentiment polarity associated with aspect terms in a single-turn utterance. SemEval-2014 and SemEval-2016 are subtasks of the Semeval Aspect-based Sentiment Analysis challenge. The goal of these subtasks is to identify the sentiment polarity (positive, negative, neutral, conflict) corresponding to all attribute words contained in each sentence. 

### CA
Comment analysis (CA) involves identifying the user's emotion from one or more sentences in a comment. SST-2, IMDB, and Amazon Review are datasets for comment analysis.  The goal of SAEval for these datasets is to identify the sentiment polarity of comments. It is important to note that Amazon Review is only used for the pre-training and does not have a test set for evaluation in SAEval.

## Download Formatted Data
Here are some examples of formatted data, with all datasets processed based on the same rules.

![pdf](https://github.com/dawn0815/SAEval-Benchmark/blob/master/p3.png)

![pdf](https://github.com/dawn0815/SAEval-Benchmark/blob/master/p4.png)

Limitted by the license of the original datasets, we are unable to provide the original datas. You can get the license and download the original datasets, then process datas using scripts (process_{name_of_dataset}.py) we provided. 
**Note that you need to obtain a license to download the raw data before downloading the formatted data we provide.** The link to download the formatted data will be updated soon!

## Evaluating your system
For evaluating your system, you simply need an individual predictions file for each of the dataset. We encourage researchers to add more baseline datasets into SAEval and promote the development of multi-task unified modeling for sentiment analysis.

## Citing SAEval
If you use SAEval in your research, please use the following `bib` entry to cite the paper (paper link is coming soon).

## License
SAEval is released without any restrictions but restrictions may apply to individual tasks (which are derived from existing datasets). We refer users to the original licenses accompanying each dataset.


## Citing Original datasets

If you use any of the SAEval datasets, please cite their original publications:

#### ERC:
```
@inproceedings{poria2019meld,
  title={MELD: A Multimodal Multi-Party Dataset for Emotion Recognition in Conversations},
  author={Poria, Soujanya and Hazarika, Devamanyu and Majumder, Navonil and Naik, Gautam and Cambria, Erik and Mihalcea, Rada},
  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
  pages={527--536},
  year={2019}
}

```

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
```
@article{li2017dailydialog,
  title={Dailydialog: A manually labelled multi-turn dialogue dataset},
  author={Li, Yanran and Su, Hui and Shen, Xiaoyu and Li, Wenjie and Cao, Ziqiang and Niu, Shuzi},
  journal={arXiv:1710.03957},
  year={2017}
}

```
```
@inproceedings{feng2022emowoz,
  title={EmoWOZ: A Large-Scale Corpus and Labelling Scheme for Emotion Recognition in Task-Oriented Dialogue Systems},
  author={Feng, Shutong and Lubis, Nurul and Geishauser, Christian and Lin, Hsien-Chin and Heck, Michael and van Niekerk, Carel and Gasic, Milica},
  booktitle={Proceedings of the Thirteenth Language Resources and Evaluation Conference},
  pages={4096--4113},
  year={2022}
}

```
```
@article{zahiri2017emotion,
  title={Emotion detection on tv show transcripts with sequence-based convolutional neural networks},
  author={Zahiri, Sayyed M and Choi, Jinho D},
  journal={arXiv:1708.04299},
  year={2017}
}
```
#### MSA:
```
@article{zadeh2016mosi,
  title={Mosi: multimodal corpus of sentiment intensity and subjectivity analysis in online opinion videos},
  author={Zadeh, Amir and Zellers, Rowan and Pincus, Eli and Morency, Louis-Philippe},
  journal={arXiv:1606.06259},
  year={2016}
}
```
```
@inproceedings{zadeh2018multimodal,
  title={Multimodal language analysis in the wild: Cmu-mosei dataset and interpretable dynamic fusion graph},
  author={Zadeh, AmirAli Bagher and Liang, Paul Pu and Poria, Soujanya and Cambria, Erik and Morency, Louis-Philippe},
  booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages={2236--2246},
  year={2018}
}
```

#### ABSA:
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

#### CA:
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
```
@inproceedings{socher2013recursive,
  title={Recursive deep models for semantic compositionality over a sentiment treebank},
  author={Socher, Richard and Perelygin, Alex and Wu, Jean and Chuang, Jason and Manning, Christopher D and Ng, Andrew Y and Potts, Christopher},
  booktitle={Proceedings of the 2013 conference on empirical methods in natural language processing},
  pages={1631--1642},
  year={2013}
}
```
```
@inproceedings{ni2019justifying,
  title={Justifying recommendations using distantly-labeled reviews and fine-grained aspects},
  author={Ni, Jianmo and Li, Jiacheng and McAuley, Julian},
  booktitle={Proceedings of the 2019 conference on empirical methods in natural language processing and the 9th international joint conference on natural language processing (EMNLP-IJCNLP)},
  pages={188--197},
  year={2019}
}
```
