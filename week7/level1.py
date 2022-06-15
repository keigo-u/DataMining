import numpy as np
import pandas as pd
from pathlib import Path

fileDir = Path('./text/it-life-hack/').glob('**/it*.txt')
pathList = list(fileDir)

column = ['date', 'url', 'title', 'text']
df = pd.DataFrame(columns=column)
for path in pathList:
    with open(path, mode='r') as f:
        url = f.readline()
        date = f.readline()
        title = f.readline()
        article = f.read()
        data = pd.Series(data=[date[:-2], url[:-2],  title[:-3], article], index=column)
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)

print(df.head())
