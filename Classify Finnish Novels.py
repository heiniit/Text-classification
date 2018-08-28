# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 13:16:12 2018

@author: Heikki
"""


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

def ClassifyTestNovel(name, file_name):
    test_data = pd.read_csv(file_name, names=["data"], encoding="ansi", delimiter="NOTUSED", engine='python')
    test_vector = vectorizer.transform(test_data["data"])
    predicted = classifier.predict(test_vector)

    counter = Counter(predicted)
    values = [counter[0], counter[1], counter[2]]
    labels = "Kivi", "London", "Shakespeare"
    
    plt.title(name)
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.show()


# Prepare training materials (Kivi. London, Shakespeare), sample 1000 rows from each
train_a = pd.read_csv("a_train.txt", names=["data"], encoding="ansi", delimiter="NOTUSED", engine='python').sample(1000)
train_a["target"] = 0
train_b = pd.read_csv("b_train.txt", names=["data"], encoding="ansi", delimiter="NOTUSED", engine='python').sample(1000)
train_b["target"] = 1
train_c = pd.read_csv("c_train.txt", names=["data"], encoding="ansi", delimiter="NOTUSED", engine='python').sample(1000)
train_c["target"] = 2
train = train_a.append(train_b).append(train_c)

# Vectorize and normalize
vectorizer = TfidfVectorizer(analyzer="word")
#vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 3))
vectors = vectorizer.fit_transform(train["data"])

# Train naive Bayes
classifier = MultinomialNB()
classifier.fit(vectors, train.target)

# Classify each of three test sets
ClassifyTestNovel("Karkurit (Kivi)", "a_test.txt")
ClassifyTestNovel("Kultaa ja kuntoa (London)", "b_test.txt")
ClassifyTestNovel("Macbeth (Shakespeare)", "c_test.txt")


