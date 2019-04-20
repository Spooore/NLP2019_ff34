import os
import shutil
import csv

csv_out = 'dictionary_combained.csv'
SrcFolder = "/media/root/f17bbdca-3166-4f69-8193-546918bcb1cf/NLP"
def GetArticlesList():
    UniqueArticlesList=[]
    for root, dirs, files in os.walk((os.path.normpath(SrcFolder)), topdown=True):
        for name in os.walk((os.path.normpath(root)), topdown=True):
            for f in name:
                if isinstance(f, (list,)):
                    for l in f:
                        if ('.pdf' in str(l) or '.PDF' in str(l)) and str(l) not in UniqueArticlesList:
                            UniqueArticlesList.append(str(l))
    UniqueArticlesList.sort()
    return UniqueArticlesList

def UnifyDictionaries():
    CSVFiles=[]
    csv_header = 'Nazwisko,Kraj'
    for subdir, dirs, files in os.walk(SrcFolder):
        for file in files:
            if "dictionary" in os.path.join(subdir, file):
                CSVFiles.append(os.path.join(subdir, file))
    csv_merge = open(csv_out, 'w')
    csv_merge.write(csv_header)
    csv_merge.write('\n')
    
    for csvFile in CSVFiles:
     with open (csvFile, 'r') as f:
        reader = csv.reader(f, delimiter=",")
        try:
            next(reader, None)
        except:
            pass
        for row in reader:
            if len(row)!=2:
                continue
            csv_merge.write(row[0])
            csv_merge.write(",")
            csv_merge.write(row[1])
            csv_merge.write("\n")
    
    return CSVFiles



artList=GetArticlesList()
dictList=UnifyDictionaries()