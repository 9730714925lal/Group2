from flask import Flask, render_template, request
import re
import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.stem import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import sentiwordnet as swn
with open("G:\\Data\\ki.txt", "r") as f:
    tweetsText = f.read()
tweetsTokens = tweetsText.split("\n") # This splits the text file into tokens on the new line character
tweetsTokens[-1:] = [] # This strips out the final empty item
#print(tweetsTokens[:2])
totalp=0
fulltp=0;
posiIntList = []
scoreIntList = []
negaIntList = []
score1IntList = []


for tweet in tweetsTokens:
    sentences = nltk.sent_tokenize(tweet)
    stokens = [nltk.word_tokenize(sent) for sent in sentences]
    taggedlist=[]
    for stoken in stokens:        
         taggedlist.append(nltk.pos_tag(stoken))
    wnl = nltk.WordNetLemmatizer()

    score_list=[]
    for idx,taggedsent in enumerate(taggedlist):
        score_list.append([])
        for idx2,t in enumerate(taggedsent):
            newtag=''
            lemmatized=wnl.lemmatize(t[0])
            if t[1].startswith('NN'):
                newtag='n'
            elif t[1].startswith('JJ'):
                newtag='a'
            elif t[1].startswith('V'):
                newtag='v'
            elif t[1].startswith('R'):
                newtag='r'
            else:
                newtag=''       
            if(newtag!=''):    
                synsets = list(swn.senti_synsets(lemmatized, newtag))
            #Getting average of all possible sentiments, as you requested        
                score=0
                if(len(synsets)>0):
                    for syn in synsets:
                        score+=syn.pos_score()-syn.neg_score()
                    score_list[idx].append(score/len(synsets))
            
    #print(score_list)
    sentence_sentiment=[]



    for score_sent in score_list:
        sentence_sentiment.append(sum([word_score for word_score in score_sent])/len(score_sent))
    print("Sentiment for each sentence for:"+tweet)
    print(sentence_sentiment)
    fulltp=fulltp+1;
    if(sentence_sentiment[0]>0):
            posiIntList.append(tweet)
            scoreIntList.append(sentence_sentiment[0])
            totalp=totalp+1
    else:
            negaIntList.append(tweet)
            score1IntList.append(sentence_sentiment[0])
thefile=open("G:\\Data\\positweet.txt",'w')
for item in posiIntList:
 thefile.write("%s\n" %item)
            

            

        
        


#...............................................
stemmer = LancasterStemmer()
stop_words = set(stopwords.words('english'))
ps=PorterStemmer()
with open("G:\\Data\\intent.txt", "r") as f:
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
    except Exception as e:
        print(str(e))
thefile=open("G:\\Data\\intweet.txt",'w')
for item in posiIntList:
 thefile.write("%s\n" %item)
            
#.......................................................................................................................
posiIntList = []
posireco = []
posiwish = []


# 4 classes of training data
training_data = []
training_data.append({"class":"purchase", "sentence":"Buy an iphone coz its great compact fon . Ultimate size...and nice camera..s7 z also good but not great"})
training_data.append({"class":"purchase", "sentence":"going to buy this phone, it is a good choice for 2018"})
training_data.append({"class":"purchase", "sentence":"I need to get a new phone. My current one is dying slowly (iPhone 6 is my current phone) "})
training_data.append({"class":"purchase", "sentence":"Im getting a new iphone next weekend. "})


training_data.append({"class":"suggestion", "sentence":"if iphone could come with dual camera"})
training_data.append({"class":"suggestion", "sentence":"I suggest you to increase the camera quality of iphone"})
training_data.append({"class":"suggestion", "sentence":" I would suggest to increase quality of iphone"})
training_data.append({"class":"suggestion", "sentence":"It would be nice if iphone comes with dual camera"})

training_data.append({"class":"recommendation", "sentence":"Unless you wanna look like a character from mine craft I suggest you get an iPhone.."})
training_data.append({"class":"recommendation", "sentence":"Yes, I realize that the iPhone 7 announcement is on September 7th. Yes I know that I will be purchasing it with my sister when its released."})
training_data.append({"class":"recommendation", "sentence":"I recommend that all android users invest in an Apple iphone."})
training_data.append({"class":"recommendation", "sentence":"I will recommend you to get this iphone"})


training_data.append({"class":"wish", "sentence":"I desire to purchase a iphone"})
training_data.append({"class":"wish", "sentence":"I am interested in buying phone"})
training_data.append({"class":"wish", "sentence":"I'm not an iPhone person, but might need one for work."})
training_data.append({"class":"wish", "sentence":"Wish i could have the iPhone X without actually having to spend money on it"})



print ("%s sentences of training data" % len(training_data))

# capture unique stemmed words in the training corpus
corpus_words = {}
class_words = {}
# turn a list into a set (of unique items) and then a list again (this removes duplicates)
classes = list(set([a['class'] for a in training_data]))
for c in classes:
    # prepare a list of words within each class
    class_words[c] = []

# loop through each sentence in our training data
for data in training_data:
    # tokenize each sentence into words
    for word in nltk.word_tokenize(data['sentence']):
        # ignore a some things
        if word not in ["?", "'s"]:
            # stem and lowercase each word
            stemmed_word = stemmer.stem(word.lower())
            # have we not seen this word already?
            if stemmed_word not in corpus_words:
                corpus_words[stemmed_word] = 1
            else:
                corpus_words[stemmed_word] += 1

            # add the word to our words in class list
            class_words[data['class']].extend([stemmed_word])

# we now have each stemmed word and the number of occurances of the word in our training corpus (the word's commonality)
print ("Corpus words and counts: %s \n" % corpus_words)
# also we have all words in each class
print ("Class words: %s" % class_words)
# calculate a score for a given class taking into account word commonality
def calculate_class_score(sentence, class_name, show_details=True):
    score = 0
    # tokenize each word in our new sentence
    for word in nltk.word_tokenize(sentence):
        # check to see if the stem of the word is in any of our classes
        if stemmer.stem(word.lower()) in class_words[class_name]:
            # treat each word with relative weight
            score += (1 / corpus_words[stemmer.stem(word.lower())])

            #if show_details:
                #print ("   match: %s (%s)" % (stemmer.stem(word.lower()), 1 / corpus_words[stemmer.stem(word.lower())]))
    return score

# return the class with highest score for sentence
def classify(sentence):
    high_class = None
    high_score = 0
    # loop through our classes
    for c in class_words.keys():
        # calculate score of sentence for each class
        score = calculate_class_score_commonality(sentence, c, show_details=False)
        # keep track of highest score
        if score > high_score:
            high_class = c
            high_score = score

    return high_class, high_score    




# we can now calculate a score for a new sentence
with open("G:\\Data\\int.txt", "r") as f:
    tweetsText = f.read()
tweetsTokens = tweetsText.split("\n") # This splits the text file into tokens on the new line character
tweetsTokens[-1:] = [] # This strips out the final empty item
sugg=0
purch=0
reco=0
wish=0
total=0
for tweet in tweetsTokens:
    high_class = None
    high_score = 0
    total=total+1
#sentence = "shall i purchase new iphone x "

# now we can find the class with the highest score
    for c in class_words.keys():
        score=calculate_class_score(tweet, c)
        print ("Class: %s  Score: %s \n" % (c, calculate_class_score(tweet, c)))
        if score > high_score:
            high_class = c
            high_score = score
    print("Class:"+"-->"+high_class+"  "+"score:"+"-->"+str(high_score))
    if(high_class =='suggestion'):
        sugg=sugg+1
        posiIntList.append(tweet)
    elif(high_class =='recommendation'):
        reco=reco+1
        posiIntList.append(tweet)
    elif(high_class =='wish'):
        wish=wish+1
        posiwish.append(tweet)
    else:
        purch=purch+1
#.............................................................................................................................

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = total,result1=fullt-total)
@app.route('/result1',methods = ['POST', 'GET'])
def result1():
   if request.method == 'POST':
      result = request.form
      return render_template("result1.html",result = totalp,result1=fulltp-totalp)
@app.route('/result2',methods = ['POST', 'GET'])
def result2():
   if request.method == 'POST':
      result = request.form
      return render_template("result2.html",sugg=sugg,purch=purch,wish=wish,recomm=reco)
if __name__ == '__main__':
   app.run()