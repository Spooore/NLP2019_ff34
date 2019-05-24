import numpy as np
import os
import shutil
import csv
import nltk
import bisect
from tika import parser
from nltk.corpus import brown
from Ingestion import GetArticlesList
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import words
from nltk.corpus import brown
from bisect import bisect_left
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

TextifiedPath = "/media/root/f17bbdca-3166-4f69-8193-546918bcb1cf/Texted"
ClearedPath = "/media/root/f17bbdca-3166-4f69-8193-546918bcb1cf/Cleared"
Sentencespath = "/media/root/f17bbdca-3166-4f69-8193-546918bcb1cf/Cleared/Sentences"
ValidWordspath = "/media/root/f17bbdca-3166-4f69-8193-546918bcb1cf/Cleared/ValidWords"

fullPaths = []
stop_words = []

fullPaths = GetArticlesList(TextifiedPath)[1]
brown_sorted = list(brown.words())
brown_sorted.sort()
stem = PorterStemmer()
lem = WordNetLemmatizer()

def GetSentences(art,dir_to_save):
    Sentences = []
    # art = "/media/root/f17bbdca-3166-4f69-8193-546918bcb1cf/Texted/AbelPowell.txt"
    filename_to_save= dir_to_save +"/"+art.split("/")[-1][0:-4] + "_sentences.txt"
    file = open(art, 'r+')
    file_out = open(filename_to_save, 'w+')
    text = file.read()
    sentences = sent_tokenize(text)
    i = 1
    for s in sentences:
        file_out.write(s + "\n" )
    file.close()
    file_out.close()
    
   
def GetValidWords(art, dir_to_save):
    ValidWords = []
    filename_to_save= dir_to_save +"/"+art.split("/")[-1][0:-4] + "_words.txt"
    file = open(art, 'r+')
    file_out = open(filename_to_save, 'w+')
    text = file.read()
    tokens = word_tokenize(text)
    i=1
    for t in tokens:
        t = t.lower()
        if bisect_left(brown_sorted, t) < len(brown_sorted) and brown_sorted[bisect_left(brown_sorted, t)] == t and t.isalpha() and t not in stop_words: 
            file_out.write(lem.lemmatize(t)+"\n")
            print(lem.lemmatize(t)+"\n")
    file.close()
    file_out.close()

def getWordCount():
    pass



#nltk.download('words')
#nltk.download('brown')
nltk.download('stopwords')
nltk.download('wordnet') 

stop_words = set(stopwords.words("english"))

# for a in fullPaths:
#     print(a + " ------------> Sentance")
#     GetSentences(a,Sentencespath)


for a in fullPaths:
    print(a + " ------------>ValidTerms")
    GetValidWords(a,ValidWordspath)