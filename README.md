#  Intelligent Question Pair Deduplication: An NLP-Based Approach for Enhancing Search Efficiency and Content Quality

![login](https://github.com/addyarishabh/Duplicate-Question-Pairs-Checker/blob/8dc0acfdca557f64d5916484a830b41262fa0b1d/Quora%20image.png?raw=true)


## Problem Statement:

Develop a machine learning-based system utilizing Natural Language Processing (NLP) techniques to identify duplicate question pairs within a dataset sourced from Quora. The objective is to optimize the efficiency of question answering platforms by reducing redundancy and enhancing search accuracy through NLP-driven analysis. The system should proficiently classify question pairs as duplicates or non-duplicates by leveraging semantic similarity, syntactic structure, and contextual relevance. This approach aims to streamline content curation processes and improve user experience on the platform by facilitating the identification of high-quality content.

## Project Goal:

The project goal is to develop a machine learning-based system utilizing Natural Language Processing (NLP) techniques to identify duplicate question pairs within a dataset sourced from Quora. The primary objective is to enhance the efficiency of question answering platforms by reducing redundancy and improving search accuracy. By accurately classifying question pairs as duplicates or non-duplicates based on semantic similarity, syntactic structure, and contextual relevance, the project aims to streamline content curation processes and facilitate the identification of high-quality content. Ultimately, the goal is to improve the user experience on the platform by providing more relevant and diverse content while minimizing duplicate entries.

## Dataset Link:

https://www.kaggle.com/datasets/quora/question-pairs-dataset

## Project Workflow diagram:

![login](https://github.com/addyarishabh/Duplicate-Question-Pairs-Checker/blob/ae32323706eea5128acd101acadd88f55202d361/workflow_duplicate.png?raw=True)

## Dataset Description:

In the given dataset we have six features/ columns :

1) id:
   Serial number for every record.
2) qid1:
   Question ID 1 represent first question ID of a serial number(id).
3) qid2:
   Question ID 2 represent second question ID of the same serial number.
4) question1:
   Question 1 define the first question of a serial number(id).
5) question2:
   QUestion 2 define the second question of a serial number(id).
6) is_duplicate:
   0 means 'Non duplicate' and 1 means 'Duplicate'.

## Python Editor used:

Visual Studio Code, Jupyter Notebook IDE

## Libraries Used:

Pandas

Numpy

Matplotlib 

Seaborn

Regular Expression

BeautifulSoup

NLTK (Natural Language Toolkit)

Scikit Learn

fuzzywazzy

gensim

## Classification Models Used:

RandomForest Classifier 

SVC (Support Vector Classifier)

Logistics Regression

DecisionTreeClassifier

K-NN( K Nearest Neighbors Classfier)

XGB (Extreme Gradient Boosting) classifier

## Web Framework used:

Streamlit

## Best Model Found:

RandomForest Classifier (Accuracy : 76.17%

## Screenshots of some sample results:

![login](https://github.com/addyarishabh/Duplicate-Question-Pairs-Checker/blob/93050aa407c0e3e77053cce058c11b27fe3f8f7c/Duplicate_image.png?raw=true)


![login](https://github.com/addyarishabh/Duplicate-Question-Pairs-Checker/blob/93050aa407c0e3e77053cce058c11b27fe3f8f7c/Non%20duplicate_image.png?raw=true)
