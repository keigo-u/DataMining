import numpy as np
import pandas as pd
from pathlib import Path
import spacy
import sklearn.feature_extraction.text as fe_text

nlp = spacy.load("ja_ginza")

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

def text_to_sequence_of_words(text, sep=' '):
    '''テキストをtokenに分割し、sep区切りの文字列として結合した文字列を返す。
    args:
      text (str): 処理対象となるテキスト。
      sep (str): 処理結果を結合するための区切り文字。
    return
      str: sepで結合した分かち書き結果。
    '''
    doc = nlp(text)
    sequence = []
    for token in doc:
        sequence.append(token.lemma_)
    return sep.join(sequence)

def df_to_sequence_of_words(df, column, sep=' '):
    '''df[column]を対象として分かち書きする。
    args:
      df (pd.DataFrame): テキストを含むデータフレーム。
      column (str): dfにおける処理対象となる列名。
      sep (str): 分かち書き結果を結合する文字。
    return
      result ([str]): text_to_sequence_of_words()で分かち書き処理された文字列のリスト。
    '''
    result = []
    for comment in df[column]:
        result.append(text_to_sequence_of_words(comment, sep))
    return result

def bow(docs, stop_words=[]):
    '''Bag-of-Wordsによるベクトルを生成。

    :param docs(list): 1文書1文字列で保存。複数文書をリストとして並べたもの。
    :return: 文書ベクトル。
    '''
    vectorizer = fe_text.CountVectorizer(stop_words=stop_words)
    vectors = vectorizer.fit_transform(docs)
    return vectors, vectorizer

sequence_of_words = df_to_sequence_of_words(df, 'article')
stop_words = ['こと', '\r\n', 'ため', '思う', 'いる', 'ある', 'する', '■']
vectors_bow, vectorizer_bow = bow(sequence_of_words, stop_words)

query = df["article"][0] 
sequence_of_words = text_to_sequence_of_words(query)
print(sequence_of_words[:100])
target_vector_bow = vectorizer_bow.transform([sequence_of_words])
#print(target_vector_bow)

from sklearn.metrics.pairwise import cosine_similarity

def most_similar_comment_indices(vectors, query_vector, n=3):
    similarities = cosine_similarity(vectors, query_vector)
    similarities = similarities.reshape(len(similarities)) # 1行に整形
    most_similar_indicies = np.argsort(similarities)[::-1][:n]
    most_similarities = np.sort(similarities)[::-1][:n]
    return most_similar_indicies, most_similarities

def print_comment_with_similarity(df, column, indicies, similarities):
    for i in range(1, len(indicies)):
        comment = df[column][indicies[i]]
        similarity = similarities[i]
        print(f'similarity = {similarity:.3f} => {comment[:100]}')

indicies, similarities = most_similar_comment_indices(vectors_bow, target_vector_bow, 4)
print_comment_with_similarity(df, 'article', indicies, similarities)