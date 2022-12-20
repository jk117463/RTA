#!/usr/bin/env python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
import pickle
filename='Cancer.csv'
names =['Age','DryCough','Smoking','BalancedDiet','Alcohol','Obesity','Outcome']
dataframe = pd.read_csv(filename,names = names)
array = dataframe.values
x=array[1:,:6]
y=array[1:,6]
scaler = MinMaxScaler(feature_range=(0,1))
rescaledX =scaler.fit_transform(x)
test_size=0.4
seed = 7
x_train,x_test,y_train,y_test = train_test_split(x ,y ,test_size = test_size,random_state=seed)
model =LogisticRegression(solver='liblinear')
model.fit(x_train,y_train)
result = model.score(x_test,y_test)
print("Accuracy - Model 1: %.3f%%" % (result*100.0))
from sklearn.svm import SVC
model_2 = SVC(kernel='linear')
model_2.fit(x_train,y_train)
result = model_2.score(x_test,y_test)
print("Accuracy - Model 2: %.3f%%" % (result*100.0))
model_3 = DecisionTreeClassifier()
model_3.fit(x_train,y_train)
result = model_3.score(x_test,y_test)
print("Accuracy - Model 3: %.3f%%" % (result*100.0))
model_4 = MultinomialNB()
model_4.fit(x_train,y_train)
result = model_4.score(x_test,y_test)
print("Accuracy - Model 4: %.3f%%" % (result*100.0))
#Rule out 4th model as accuracy is the least
predicted_1 = model.predict(x_test)
predicted_2 = model_2.predict(x_test)
predicted_3 = model_3.predict(x_test)
report1 = classification_report(y_test,predicted_1)
print(report1)
report2 = classification_report(y_test,predicted_2)
print(report2)
report3 = classification_report(y_test,predicted_3)
print(report3)
matrix1 = confusion_matrix(y_test,predicted_1)
print(matrix1)
matrix2 = confusion_matrix(y_test,predicted_2)
print(matrix2)
matrix3 = confusion_matrix(y_test,predicted_3)
print(matrix3)
with open('CancerPredictonModel.pkl','wb') as f:
    pickle.dump(model_3,f)
with open ('CancerPredictonModel.pkl','rb') as f:
    loaded_model = pickle.load(f)
test_set =[[35,7,8,6,5,7]]
print(loaded_model.predict(test_set))
test_set =[[34,7,7,7,7,7]]
print(loaded_model.predict(test_set))
