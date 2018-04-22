from flask import Flask, render_template, request
import nltk
import matplotlib.pylab as plt
import numpy as np
from nltk.corpus import sentiwordnet as swn
import re
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.stem import PorterStemmer

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('home.html')
	stop_words = set(stopwords.words('english'))
	ps=PorterStemmer()
with open("G:\\Data\\ki.txt", "r") as f:
    inText = f.read()
inTokens = inText.split("\n") # This splits the text file into tokens on the new line character
inTokens[-1:] = [] # This strips out the final empty item

def process(sentence):
    print('hi.......................................................')
    flag=0
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        #print(w1+"  "+t1+"   "+w2+"  "+t2+"  "+w3+"   "+t3)
        if(t1.startswith('VBP') and t2.startswith('VB') and (t3.startswith('NN') or t3.startswith('JJ'))):
            if((w2 in inTokens) or (w1 in inTokens)):
                flag=1
                break
        elif(t1.startswith('RB') and t2.startswith('VBP') and t3.startswith('NN')):
            if(w2 in inTokens):
                flag=1           
                break
        elif(t1.startswith('VBP') and t2.startswith('NN') and t3.startswith('NN')):
            if(w1 in inTokens):
                flag=1           
                break
        
        elif(t1.startswith('VBP') and t2.startswith('JJ') and t3.startswith('NN')):
            flag=1           
            break
        elif(t1.startswith('MD') and t2.startswith('VB') and t3.startswith('JJ')):
            flag=1
            break
        elif(t1.startswith('MD') and t2.startswith('VB') and t3.startswith('NN')):
            if((w2 in inTokens) or (w3 in inTokens)):
                flag=1
                break
        elif(t1.startswith('VBG') and t2.startswith('VB') and t3.startswith('NN')):
            flag=1           
            break
        elif(t1.startswith('VBD') and t2.startswith('VBG') and t3.startswith('NN')):
            flag=1           
            break
        elif(t1.startswith('VBP') and t2.startswith('NNS') and t3.startswith('VBP')):
            flag=1           
            break
       
        elif(t1.startswith('MD') and t2.startswith('VB') and t3.startswith('RB')):
            flag=1           
            break
        elif(t1.startswith('VBG') and t2.startswith('VB') and t3.startswith('JJ')):
            flag=1           
            break
       
        
        elif(t1.startswith('MD') and t2.startswith('RB') and t3.startswith('VB')):
            flag=1
            break
        else:
            flag=0
    if(flag == 1):
        return 1
    else:
        return 0

    
       
with open("G:\\Data\\ki.txt", "r") as f:
    tweetsText = f.read()
tweetsTokens = tweetsText.split("\n") # This splits the text file into tokens on the new line character
tweetsTokens[-1:] = [] # This strips out the final empty item
#print(tweetsTokens)
def tokenizer(theText):
    theTokens = re.findall(r'\b\w[\w-]*\b', theText.lower())
    return theTokens
posiIntList = []
total=0
fullt=0
for tweet in tweetsTokens:
    x=[]
    tokens = nltk.word_tokenize(tweet)
    try:
        for i in tokens:
            if not i in stop_words:
                x.append(i)
                tagged=nltk.pos_tag(x)
  
        print(tagged)
        sume = process(tagged)
        print(sume)
        fullt=fullt+1
        if(sume > 0):
            total+=1
            posiIntList.append(tweet)
    except Exception as e
	        print(str(e))
#print("Total tweets:   " + str(fullt))
#print("number of intent tweets:   " + str(total))





   return render_template("result.html",result = fullt,result1=total)
if __name__ == '__main__':
   app.run()