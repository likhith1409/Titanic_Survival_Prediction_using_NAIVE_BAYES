# -*- coding: utf-8 -*-
"""Titanic_Survival_Prediction_using_NAIVE_BAYES.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1utYq-U7Qb6SimQVcaniuUE_4k8jRN8C1

### ***Titanic Survival Prediction using NAIVE BAYES***

---
"""

import pandas as pd  #import libraries
import numpy as np

from google.colab import files   #choose dataset
uploaded = files.upload()

dataset = pd.read_csv('titanicsurvival.csv')  #load Dataset

print(dataset.shape)    #summarize Dataset
print(dataset.head(5))

income_set = set(dataset['Sex'])   #mapping Text Data to Binary Value
dataset['Sex'] = dataset['Sex'].map({'female': 0, 'male':1}).astype(int)
print(dataset.head(5))

X = dataset.drop('Survived',axis='columns')  #segregate dataset into X and Y
X

Y = dataset.Survived
Y

X.columns[X.isna().any()]   # Removing NA Values

X.Age = X.Age.fillna(X.Age.mean())

X.columns[X.isna().any()]

from sklearn.model_selection import train_test_split  #Splitting Dataset into Train and Test
x_train,x_test,y_train,y_test =  train_test_split(X,Y,test_size =0.25,random_state=0)

from sklearn.naive_bayes import GaussianNB  # Training
model = GaussianNB()
model.fit(x_train,y_train)

pclassNo = int(input("Enter Person's Pclass number: "))  #Predicting wheather Person Survived or Not
gender = int(input("Enter Person's Gender 0-female 1-male(0 or 1): "))
age = int(input("Enter Person's Age: "))
fare = float(input("Enter Person's Fare: "))
person = [[pclassNo,gender,age,fare]]
result = model.predict(person)
print(result)

if result == 1:
  print("Person might be Survived")
else:
  print("Person might not be Survived")

y_pred = model.predict(x_test)  #Prediction for all Test Data
print(np.column_stack((y_pred,y_test)))

from sklearn.metrics import accuracy_score  # Accuracy of Model
print("Accuracy of the model: {0}%".format(accuracy_score(y_test,y_pred)*100))