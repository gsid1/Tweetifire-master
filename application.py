from tkinter import *
from flask import Flask
import pandas as pd
import pickle


application = Flask(__name__)


def fn(e,e1):
    save(e)
    predict()
    loadme(e1)

def save(e):
    open("predict.csv", "w").close()
    text = e.get()
    with open("predict.csv", "w") as f:
        f.write(text)

def loadme(e1):
    f = open('result.txt','r')
    line = f.readline()
    e1.configure(text=line)

    f.close()
    
def predict():
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

@application.route("/")
def main():
    root = Tk()
    root.title("Tweetifire")
    root.geometry('350x120')
    c = Canvas(root,width=600)
    c.pack(side = 'left',expand=1,fill=BOTH)

    c2 = Canvas(c,width=600)
    c2.pack(side = 'left',expand=1,fill=BOTH)
    c3 = Canvas(c,width=600)
    c3.pack(side = 'left',expand=1,fill=BOTH)

    w1 = Label(c2, text="Tweet ")
    w1.pack()
    e = Entry(c2,width=200)
    e.pack()
    toolbar = Frame(c2)
    toolbar.pack(side=TOP, fill=X)

    l = Label(c2,text=' Output ')
    l.pack()
    l1 = Label(c2, text='')
    l1.pack()
    b = Button(toolbar, text="Classify", width=9, command=lambda:fn(e,l1))
    b.pack(side=LEFT, padx=2, pady=2)
    root.mainloop()

if __name__ == '__main__':
    main()
