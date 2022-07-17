import numpy as np
import pandas as pd
from pathlib import Path
import spacy
import collections

fileDir = Path('./text/it-life-hack/').glob('**/it*.txt')
pathList = list(fileDir)

column = ['date', 'url', 'title', 'article']
df = pd.DataFrame(columns=column)
for path in pathList[:20]:
    with open(path, mode='r') as f:
        url = f.readline()
        date = f.readline()
        title = f.readline()
        article = f.read()
        data = pd.Series(data=[date[:-2], url[:-2],  title[:-3], article], index=column)
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)

nlp = spacy.load('ja_ginza')

def count_lemma(df, column):
    words_list = []
    for comment in df[column]:
        doc = nlp(comment)
        for token in doc:
          words_list.append(token.lemma_)
        for entity in doc.ents:
          print(entity.text, entity.label_)
    return words_list

words_list = count_lemma(df, 'article')
words_count = collections.Counter(words_list)
num_of_words = 0
for value in words_count.values():
  num_of_words = num_of_words + value

print("num of words =", num_of_words)
print(words_count.most_common(10))
