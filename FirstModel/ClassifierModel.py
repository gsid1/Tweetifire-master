from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
from sklearn.model_selection import cross_val_score

import pickle


vect = TfidfVectorizer()

file = pd.read_csv('Train1.csv')
cols = ['Tweets', 'Value']
file = file[cols]

stop_words = set(stopwords.words('english'))
t = str.maketrans('', '', string.punctuation)
porter = PorterStemmer()


def clean_str(string):
    try:
        w = nltk.word_tokenize(string)
    except:
        return "default"
    w = [p.lower() for p in w]
    s = [p.translate(t) for p in w]
    w = [word for word in s if word.isalpha()]
    w = [p for p in w if not p in stop_words]
    w = [porter.stem(word) for word in w]
    string = " ".join(w)
    return string.strip().lower()


file['Tweets'] = [clean_str(sent) for sent in file['Tweets']]

vect.fit(file.Tweets)

Xdata = vect.transform(file.Tweets).toarray()
Ydata = file.Value

classifier = LogisticRegression()

classifier.fit(Xdata, Ydata)

saveFile = 'LogisticRegModel.sav'
pickle.dump(classifier, open(saveFile, 'wb'))

saveVectorizer = 'vectorizer.pickle'
pickle.dump(vect, open(saveVectorizer, 'wb'))
