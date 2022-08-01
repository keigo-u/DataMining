import numpy as np
import pandas as pd
from pathlib import Path
import spacy
import sklearn.feature_extraction.text as fe_text
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix