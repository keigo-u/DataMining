import collections

import numpy as np
import pandas as pd
import spacy

nlp = spacy.load("ja_ginza")

assesment_df = pd.read_pickle('week7/r_assesment.pkl')

# 全体像の観察
print('総件数 = ', len(assesment_df))
print('grade内訳: ', collections.Counter(assesment_df['grade']))
print('授業内訳: ', collections.Counter(assesment_df['title']))

print('comment統計情報')
comments_length = [len(comment) for comment in assesment_df['comment']]
print(pd.Series(comments_length).describe())

doc = nlp('今回は自然言語処理ライブラリであるspaCyについて紹介します。')   # nlpに文章を入力すると、その戻り値に解析結果が保存される。
for token in doc:  # Token単位で処理結果を参照。
  print(token.i, token.lemma_, token.pos_)