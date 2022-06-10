import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix

# Open Excel file as Dataframe
input_book = pd.ExcelFile('week3/default of credit card clients.xls')
input_sheet_name = input_book.sheet_names
df = input_book.parse(input_sheet_name[0])

# Detach label data
X = df.values[1:, :-2]
y = df.values[1:,-1]
y = y.astype('int')

# Split the dataset into training and testing set
num_of_training = 29000

X_train = X[:num_of_training]
X_test = X[num_of_training:]

y_train = y[:num_of_training]
y_test = y[num_of_training:]

#Standardize data
from sklearn.preprocessing import StandardScaler
std_scaler = StandardScaler()
std_scaler.fit(X_train)

X_train_std = std_scaler.transform(X_train)
X_test_std = std_scaler.transform(X_test)

# Machine Learning with SVM 
from sklearn.svm import SVC
clf = SVC(kernel="linear")
clf.fit(X_train_std, y_train)

# Show acccuracy
print('train accuracy : ', clf.score(X_train_std, y_train))
print('test accuracy : ', clf.score(X_test_std, y_test))

# Make Confusion matrix
predicted = clf.predict(X_test)
cm = confusion_matrix(predicted, y_test)
print("Confusion matrix :")
print(cm)