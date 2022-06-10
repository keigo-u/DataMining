# Prepare the dataset
# Load the diabetes dataset
# ref. https://scikit-learn.org/stable/datasets/index.html#diabetes-dataset

from sklearn import datasets
diabetes = datasets.load_diabetes()

orig_X = diabetes.data # get a feature matrix (input dataset)
print(type(orig_X))    # check the type
print(orig_X.shape)    # check the size of feature matrix
print(orig_X[:5])      # display the first 5 samples
print(diabetes.feature_names)    # display the name of each element of feature

# convert np.ndarray to pd.dataframe for readability

import pandas as pd
df = pd.DataFrame(orig_X, columns=diabetes.feature_names)
df.head()

# Here, use just one feature 'bmi' for simple exercise
import numpy as np
X = diabetes.data[:, np.newaxis, 2]
print(X.shape)
print(X[:5])

y = diabetes.target
print(y.shape)
print(y[:5])

# split the dataset into training and testing set
num_of_training = 400

X_train = X[:num_of_training]
X_test = X[num_of_training:]

y_train = y[:num_of_training]
y_test = y[num_of_training:]

#print(X_train.shape)
#print(X_test.shape)
print(y_train)
#print(y_test.shape)
#print(X_train)
#print(type(X_train))

# Select a model
# => Linear Regression

from sklearn import linear_model

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training set
regr.fit(X_train, y_train)

# Make predictions using the testing set
predicted = regr.predict(X_test)

# Check the predictions vs true answer
print(np.c_[predicted, y_test])

# Check the differences (errors)
print(y_test - predicted)

# Check the sum of absolute error
print(sum(np.abs(y_test - predicted)))

# MAE (Mean Absolute Error)
print(sum(np.abs(y_test - predicted)) / len(X_test))

# Plot testing set and predictions
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.scatter(X_test, y_test,  color='black', label='test data')
ax.plot(X_test, predicted, color='blue', linewidth=3, label='predicted')
ax.legend(loc='best', fontsize=20)
ax.set_xlabel('bmi', fontsize=20)
ax.set_ylabel('disease progression', fontsize=20)
plt.show()

# Check the model (obtained parameters)
print('coefficients: ', regr.coef_)
print('intercept: ', regr.intercept_)