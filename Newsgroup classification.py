# -*- coding: utf-8 -*-
"""
Created on Sun May  6 12:31:23 2018

@author: Heikki
"""

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
categories = ["alt.atheism", "soc.religion.christian", "comp.graphics", "sci.med"]
newsgroups_train = fetch_20newsgroups(subset="train",categories=categories)
print(len(newsgroups_train.data))
#print(newsgroups_train.data[0])

# Vectorize and normalize
vectorizer = TfidfVectorizer()
train_vectors = vectorizer.fit_transform(newsgroups_train.data)
print(len(vectorizer.get_feature_names()))
print(vectorizer.get_feature_names()[10000:10100])

# Train naive Bayes
classifier = MultinomialNB()
classifier.fit(train_vectors, newsgroups_train.target)

# Test the classifier with some strings
test_strings = ["God is love", 
                "OpenGL on the GPU is fast", 
                "I'm an atheist", 
                "Medical students are specialized"]
test_vectors = vectorizer.transform(test_strings)
predicted = classifier.predict(test_vectors)

# Print test classification
for doc, category in zip(test_strings, predicted):
    print("%r => %s" % (doc, newsgroups_train.target_names[category]))
