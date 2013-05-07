import nltk 
from nltk.corpus import names 
from urllib import urlopen 
url="http://www.indianfreedomfighters.in/" 
print 'Data Read' 
import nltk.data 
import random 
from nltk.corpus import PlaintextCorpusReader

names=[] 
locations=[]


corpus_root='./' 
newcorpus=PlaintextCorpusReader(corpus_root,'.*') 
print newcorpus.words('name.txt') 
newcorpus1=PlaintextCorpusReader(corpus_root,'.*') 
print newcorpus1.words('place.txt') 
mynames=newcorpus.words('name.txt') 
mylocations=newcorpus1.words('place.txt')

sent_detector=nltk.data.load('tokenizers/punkt/english.pickle') 
text=urlopen(url).read() 
text=nltk.clean_html(text) 
tokenized_wordlist=nltk.word_tokenize(text)
tagged=nltk.pos_tag(tokenized_wordlist) 
nouns=[] 
for la in tagged: 
    if (la[1].lower() == 'nnp'): 
        nouns.append(la[0].lower()) 
 
name=raw_input("Enter name of freedom fighter") 
if name in mynames: 
    print "Associated:  1.Names 2.Locations" 
    ch=raw_input("Type 1 or 2") 
    ch=int(ch) 
    if ch==1: 
                names=[] 
                for noun in nouns: 
                        for name1 in mynames: 
                            if (noun == name): 
                                    names.append(noun)     
 
                names=list(set(names)) 
                names=names.remove(name) 
                print "The names of freedom fighters associated with "+name+" are:" 
                for i in names: 
                            print i 
    elif ch==2: 
                locations=[] 
                for noun in nouns: 
                        for loc in mylocations: 
                            if (noun == loc): 
                                    locations.append(noun)     
 
                locations=list(set(locations)) 
                print "The location associated with "+name+" are:" 
                for j in locations: 
                            print j 
    else: 
        print "Number entered is invalid.Please enter 1 or 2 only" 
else: 
    print "The name entered is not that of a freedom fighter"
