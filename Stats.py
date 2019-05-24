from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from Ingestion import GetArticlesList
from sklearn.feature_extraction.text import CountVectorizer
import re

ValidWordspath = "/media/root/f17bbdca-3166-4f69-8193-546918bcb1cf/Cleared/ValidWords"
Cloudpath = "/media/root/f17bbdca-3166-4f69-8193-546918bcb1cf/Cleared/CloudFiles"
Vectpath = "/media/root/f17bbdca-3166-4f69-8193-546918bcb1cf/Cleared/Vectors/MonoGrams"
stop_words = set(stopwords.words("english"))

fullPaths = GetArticlesList(ValidWordspath)[1]

def getWordsMap(path):
    words=open(path,"r")
    out = [ line.split()[0] for line in words.readlines()]
    words.close()
    # print(str(out))
    wordcloud = WordCloud(
                          background_color='white',
                          stopwords=stop_words,
                          max_words=100,
                          max_font_size=50, 
                          random_state=42
                         ).generate(str(out).replace("'",""))

    print(wordcloud)
    fig = plt.figure(1)
    plt.imshow(wordcloud)
    plt.axis('off')
    # plt.show()
    pathtosave=Cloudpath +"/"+  path.split("/")[-1][0:-10]+ ".png"
    print(pathtosave)
    fig.savefig(pathtosave, dpi=900)

def Monograms(path):
    words=open(path,"r")
    out = [ line.split()[0] for line in words.readlines()]
    words.close()
    cv=CountVectorizer(max_df=0.8,stop_words=stop_words, max_features=10000, ngram_range=(1,3))
    vec=cv.fit_transform(out)
    pathtosave=Vectpath  +"/" + path.split("/")[-1][0:-10]+ ".txt"
    print(pathtosave)
    vec = CountVectorizer().fit(out)
    bag_of_words = vec.transform(out)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in      
                   vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], 
                       reverse=True)
    topTwenty=list(words_freq[:20])
    f=open(pathtosave,"w+")
    f.write(str(topTwenty))
    f.close()

# for f in fullPaths:
#     print(f)
#     getWordsMap(f)

for f in fullPaths:
    print(f)
    Monograms(f)