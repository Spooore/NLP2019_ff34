import PyPDF2
import textract 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
from elasticsearch import Elasticsearch

es=Elasticsearch([{'host':'localhost','port':9200}])
print(es)