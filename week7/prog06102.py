import collections

import numpy as np
import pandas as pd
import spacy

nlp = spacy.load("ja_ginza")

doc = nlp('今回は自然言語処理ライブラリであるspaCyについて紹介します。')   # nlpに文章を入力すると、その戻り値に解析結果が保存される。
for token in doc:  # Token単位で処理結果を参照。
  print(token.i, token.lemma_, token.pos_)