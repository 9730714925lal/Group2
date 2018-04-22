# use natural language toolkit
import nltk
from nltk.stem.lancaster import LancasterStemmer
# word stemmer
stemmer = LancasterStemmer()
import matplotlib.pyplot as plt


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
with open("G:\\int.txt", "r") as f:
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

        
print("Total intended tweets"+"--->"+str(total))
print("Total suggestion tweets"+"--->"+str(sugg))
print("Total recommendation tweets"+"--->"+str(reco))
print("Total wish tweets"+"--->"+str(wish))
print("Total purchase tweets"+"--->"+str(purch))

labels = 'Suggestion', 'Purchase','Recommendation','Wish'
sizes = [sugg, purch,reco,wish]
colors = ['gold','lightcoral','red','blue']
explode = (0.1, 0,0,0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
#.....feature detection
#print(posiIntList)

from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.stem import PorterStemmer
stop_words = set(stopwords.words('english'))
camerasum=0
batsum=0
dissum=0
dessum=0
persum=0
cossum=0
def process(sentence):
    #print(sentence)
    global camerasum
    global batsum
    global dissum
    global dessum
    global persum
    global cossum
    for (w1,t1), (w2,t2) in nltk.bigrams(sentence):
        #print(t1+"...........")
        #print(w1)
        if (t1.startswith('NN') and w1=='camera'):
            camerasum+=1
        if (t1.startswith('NN') and w1=='battery'):
            batsum+=1
        if (t1.startswith('NN') and w1=='display'):
            dissum+=1
        if (t1.startswith('NN') and w1=='design'):
            dessum+=1
        if (t1.startswith('NN') and w1=='performance'):
            persum+=1
        if (t1.startswith('NN') and w1=='cost'):
            cossum+=1
        
for tweet in posiIntList:
    x=[]
    tokens = nltk.word_tokenize(tweet)
    try:
        for i in tokens:
            if not i in stop_words:
                x.append(i)
                tagged=nltk.pos_tag(x)
        #print(tagged)
        process(tagged)

    except Exception as e:
        print(str(e))
labels = 'Camera', 'Battery','Display','Design','Performanace','Cost'
sizes = [camerasum, batsum,dissum,dessum,persum,cossum]
colors = ['gold','lightcoral','green','blue','red','orange']
explode = (0.1, 0,0,0,0,0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()

