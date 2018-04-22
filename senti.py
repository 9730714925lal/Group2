import nltk
import matplotlib.pylab as plt
import numpy as np
from nltk.corpus import sentiwordnet as swn
with open("G:\\Data\\ki.txt", "r") as f:
    tweetsText = f.read()
tweetsTokens = tweetsText.split("\n") # This splits the text file into tokens on the new line character
tweetsTokens[-1:] = [] # This strips out the final empty item
#print(tweetsTokens[:2])
total=0
fullt=0;
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
    fullt=fullt+1;
    if(sentence_sentiment[0]>0):
            posiIntList.append(tweet)
            scoreIntList.append(sentence_sentiment[0])
            total=total+1
    else:
            negaIntList.append(tweet)
            score1IntList.append(sentence_sentiment[0])
            

            

        
        


print("no of total tweets:"+str(fullt))
print("no of positive tweets:"+str(total))
print("no of negative tweets:"+str((fullt-total)))
datas = [{'label':'tweets', 'color': 'r', 'height': fullt},
    {'label':'positivity', 'color': 'g', 'height': total},
    {'label':'nagitivity', 'color': 'b', 'height': (fullt-total)}]

i = 0
for data in datas:
    plt.bar(i, data['height'],align='center',color=data['color'])
    i += 1

labels = [data['label'] for data in datas]
pos = [i for i in range(len(datas)) ]
plt.xticks(pos, labels)
plt.xlabel('People Reviews')
plt.title('Sentiment Analysis')
plt.show()
#print(posiIntList)
#print(scoreIntList)
for j in range(len(scoreIntList)):
    #initially swapped is false
    swapped = False
    i = 0
    while i<len(scoreIntList)-1:
        #comparing the adjacent elements
        if scoreIntList[i]<scoreIntList[i+1]:
            #swapping
            scoreIntList[i],scoreIntList[i+1] = scoreIntList[i+1],scoreIntList[i]
            posiIntList[i],posiIntList[i+1] = posiIntList[i+1],posiIntList[i]
            #Changing the value of swapped
            swapped = True
        i = i+1
    #if swapped is false then the list is sorted
    #we can stop the loop
    if swapped == False:
        break
print ("Sorted")
#print (scoreIntList)
#print (posiIntList)
print ("Top 5 positive reviews:")
for i in range(0,4):
    print(posiIntList[i])
#......negative Tweets
for j in range(len(score1IntList)):
    #initially swapped is false
    swapped = False
    i = 0
    while i<len(score1IntList)-1:
        #comparing the adjacent elements
        if score1IntList[i]<score1IntList[i+1]:
            #swapping
            score1IntList[i],score1IntList[i+1] = score1IntList[i+1],score1IntList[i]
            negaIntList[i],negaIntList[i+1] = negaIntList[i+1],negaIntList[i]
            #Changing the value of swapped
            swapped = True
        i = i+1
    #if swapped is false then the list is sorted
    #we can stop the loop
    if swapped == False:
        break
print ("Sorted")
#print (scoreIntList)
#print (posiIntList)
print ("Top 5 negative reviews:")
for i in range(0,4):
    print(negaIntList[i])

