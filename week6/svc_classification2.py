import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Open Excel file as Dataframe
input_book = pd.ExcelFile('week3/default of credit card clients.xls')
input_sheet_name = input_book.sheet_names
df = input_book.parse(input_sheet_name[0])

# Detach label data
X = df.values[1:, 1:-2]
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

#Graph configuration
fig = plt.figure(linewidth=1)
#Left side
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_title('Default')
ax1.set_xlabel("Age")
ax1.set_ylabel("Payment")
ax1.scatter(X_train[:,4], X_train[:,17], s=0.1)

#Left side
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_title('Standardized')
ax2.set_xlabel("Age")
ax2.set_ylabel("Payment")
ax2.scatter(X_train_std[:,4], X_train_std[:,17], s=0.1)
fig.savefig('data.png')

#Show graph
plt.show()

# Machine Learning with SVM 
from sklearn.svm import SVC
clf = SVC(kernel="linear")
clf.fit(X_train_std, y_train)

# Show acccuracy
print('train_std accuracy : ', clf.score(X_train_std, y_train))
print('test_std accuracy : ', clf.score(X_test_std, y_test))

# Make Confusion matrix
predicted = clf.predict(X_test_std)
cm = confusion_matrix(predicted, y_test)
print("Confusion matrix :")
print(cm)