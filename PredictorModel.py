import pandas as pd
import pickle

openFile = 'LogisticRegModel.sav'
saveVectorizer = 'vectorizer.pickle'

predictor = pickle.load(open(openFile, 'rb'))
vect = pickle.load(open(saveVectorizer, 'rb'))

readFile = pd.read_csv('predict.csv')

pred = vect.transform(readFile).toarray()
result = predictor.predict(pred)
res = result[0]

if res == 1:
    data = "Availability"
elif res == 2:
    data = "Need"
else:
    data = "None"

with open("result.txt", "w") as f:
    f.write(data)


