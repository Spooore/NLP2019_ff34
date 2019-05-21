import os
import shutil
import csv
from tika import parser



csv_out = 'dictionary_combained.csv'
SrcFolder = "/media/root/f17bbdca-3166-4f69-8193-546918bcb1cf/NLP"
UnifiedSrcFolder = "/media/root/f17bbdca-3166-4f69-8193-546918bcb1cf/NLP_combained"
pathToSave =  "/media/root/f17bbdca-3166-4f69-8193-546918bcb1cf/Texted"


def GetArticlesList(src):
    UniqueArticlesList=[]
    Fullpath=[]
    for root, dirs, files in os.walk((os.path.normpath(src)), topdown=True):
        for name in os.walk((os.path.normpath(root)), topdown=True):
            for f in name:
                if isinstance(f, (list,)):
                    for l in f:
                        if ('.pdf' in str(l) or '.PDF' in str(l)) and str(l) not in UniqueArticlesList:
                            UniqueArticlesList.append(str(l))
        for f in files:
            if os.path.abspath(os.path.join(root, f)) not in Fullpath:
                Fullpath.append(os.path.abspath(os.path.join(root, f)))                           
    UniqueArticlesList.sort()
    return [UniqueArticlesList,Fullpath]

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


def toText(path):
    raw = parser.from_file(path)
    return raw['content']


artList=GetArticlesList(SrcFolder)[0]
unifiedList=GetArticlesList(UnifiedSrcFolder)[1]
dictList=UnifyDictionaries()

for art in unifiedList:
    new_path = pathToSave + "/" + art.split("/")[-1][0:-4] + ".txt"
    print(new_path)
    f = open(new_path, "w+")
    try:
        safe_text = toText(art).encode('utf-8', errors='ignore')
    except Exception:
        pass
    safe_text = str(safe_text).replace('\\', '\\\\').replace('"', '\\"').replace('\\n','\n').replace("\\","")
    f.write(safe_text)
    f.close()