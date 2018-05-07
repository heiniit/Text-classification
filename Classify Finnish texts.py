# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:10:25 2018

@author: Heikki Niittylä
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from pandas import DataFrame
from urllib.request import urlopen
from collections import Counter


def ClassifyBook(name, url, vectorizer):
    book = urlopen(url)
    test_vector = vectorizer.transform(list(book))
    predicted = classifier.predict(test_vector)
    counter = Counter(predicted)
    tot = counter[0]+counter[1]
    print("\n{0}: {1} percent Kivi, {2} percent London".format(name, 100*counter[0]/tot, 100*counter[1]/tot))


# Use a couple of books as a training material
book1 = urlopen("http://www.gutenberg.org/cache/epub/11152/pg11152.txt") # Nummisuutarit
df1 = DataFrame(data=list(book1), columns=["data"])
df1["target"] = 0
book2 = urlopen("http://www.gutenberg.org/cache/epub/48321/pg48321.txt") # Klondyken kuningas
df2 = DataFrame(data=list(book2), columns=["data"])
df2["target"] = 1
df = df1.append(df2)
authors = ["Kivi", "London"]

# Vectorize and normalize
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(df["data"])

# Train naive Bayes
classifier = MultinomialNB()
classifier.fit(vectors, df.target)

# Test the classifier with some strings
test_strings = [# Kivi: Nummisuutarit
                "Niin muuttuu mailma, Eskoni", 
                # Kivi: Seitsemän veljestä
                "Käykäämme juoneen, tuottakaamme itsellemme aapiskirjat Hämeenlinnasta ja lähtekäämme lukkarille kouluun, niinkuin on rovastimme käsky.",
                # Kivi: Seitsemän veljestä
                "Katsokaat: ellemme osaa lukea, niin laillinen vaimokin on meiltä kielletty hedelmä.",
                # London: Klondyken kuningas
                "Jack Kearns ehdotti pokeria.",
                #London: Erämaan kutsu
                "Kaksi päivää ja kaksi yötä retuutettiin tätä tavaravaunua eteenpäin, pitkässä junajonossa kimakasti viheltävän veturin jäljessä.", 
                #London: Erämaan kutsu
                "Eräänä päivänä tuli sinne pieni kurttuinen mies, joka puhui murteellisesti englantia."]
test_vector = vectorizer.transform(test_strings)
predicted = classifier.predict(test_vector)

# Print test classification
for test_str, category in zip(test_strings, predicted):
    print("{0} => {1}".format(test_str, authors[category]))

# Classify whole books, line by line
ClassifyBook("Kihlaus (Kivi)", "http://www.gutenberg.org/cache/epub/12795/pg12795.txt", vectorizer)
ClassifyBook("Lumikenttien tytär (London)", "http://www.gutenberg.org/cache/epub/47983/pg47983.txt", vectorizer)


# Output
'''
Niin muuttuu mailma, Eskoni => Kivi
Käykäämme juoneen, tuottakaamme itsellemme aapiskirjat Hämeenlinnasta ja lähtekäämme lukkarille kouluun, niinkuin on rovastimme käsky. => Kivi
Katsokaat: ellemme osaa lukea, niin laillinen vaimokin on meiltä kielletty hedelmä. => Kivi
Jack Kearns ehdotti pokeria. => London
Kaksi päivää ja kaksi yötä retuutettiin tätä tavaravaunua eteenpäin, pitkässä junajonossa kimakasti viheltävän veturin jäljessä. => London
Eräänä päivänä tuli sinne pieni kurttuinen mies, joka puhui murteellisesti englantia. => London

Kihlaus: 32.6221224031443 percent Kivi, 67.3778775968557 percent London

Lumikenttien tytär: 3.0692301060436242 percent Kivi, 96.93076989395638 percent London
'''
