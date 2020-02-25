## 1. Recap ##

import pandas as pd

loans = pd.read_csv('cleaned_loans_2007.csv')
print(loans.info())

## 3. Picking an error metric ##

import pandas as pd
tn=sum((predictions==0)&(loans['loan_status']==0))
tp=sum((predictions==1)&(loans['loan_status']==1))
fn=sum((predictions==0)&(loans['loan_status']==1))
fp=sum((predictions==1)&(loans['loan_status']==0))

## 5. Class imbalance ##

import pandas as pd
import numpy

# Predict that all loans will be paid off on time.
predictions = pd.Series(numpy.ones(loans.shape[0]))
fpr=sum((predictions==1)&(loans['loan_status']==0))/(sum((predictions==1)&(loans['loan_status']==0))+sum((predictions==0)&(loans['loan_status']==0)))
tpr=sum((predictions==1)&(loans['loan_status']==1))/(sum((predictions==1)&(loans['loan_status']==1))+sum((predictions==0)&(loans['loan_status']==1)))

print(fpr)
print(tpr)

## 6. Logistic Regression ##

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

features = loans.drop('loan_status',axis=1)
target = loans['loan_status']
lr.fit(features,target)
predictions = lr.predict(features)


## 7. Cross Validation ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
lr = LogisticRegression()
predictions = cross_val_predict(lr, features, target, cv=3)

predictions = pd.Series(predictions)

tpr = sum((predictions==1)&(loans['loan_status']==1))/(sum((predictions==1)&(loans['loan_status']==1))+sum((predictions==0)&(loans['loan_status']==1)))

fpr = sum((predictions==1)&(loans['loan_status']==0))/(sum((predictions==1)&(loans['loan_status']==0))+sum((predictions==0)&(loans['loan_status']==0)))

print(tpr)
print(fpr)

## 9. Penalizing the classifier ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
lr=LogisticRegression(class_weight='balanced')

predictions=cross_val_predict(lr,features,target)
predictions=pd.Series(predictions)

tpr = sum((predictions==1)&(loans['loan_status']==1))/(sum((predictions==1)&(loans['loan_status']==1))+sum((predictions==0)&(loans['loan_status']==1)))

fpr = sum((predictions==1)&(loans['loan_status']==0))/(sum((predictions==1)&(loans['loan_status']==0))+sum((predictions==0)&(loans['loan_status']==0)))

print(tpr)
print(fpr)

## 10. Manual penalties ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict

penalty = {
    0: 10,
    1: 1
}

lr=LogisticRegression(class_weight=penalty)

predictions=cross_val_predict(lr,features,target)
predictions=pd.Series(predictions)

tpr = sum((predictions==1)&(loans['loan_status']==1))/(sum((predictions==1)&(loans['loan_status']==1))+sum((predictions==0)&(loans['loan_status']==1)))

fpr = sum((predictions==1)&(loans['loan_status']==0))/(sum((predictions==1)&(loans['loan_status']==0))+sum((predictions==0)&(loans['loan_status']==0)))

print(tpr)
print(fpr)

## 11. Random forests ##

from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_predict


rf=RandomForestClassifier(random_state=1, class_weight='balanced')

predictions=cross_val_predict(rf,features,target)
predictions=pd.Series(predictions)

tpr = sum((predictions==1)&(loans['loan_status']==1))/(sum((predictions==1)&(loans['loan_status']==1))+sum((predictions==0)&(loans['loan_status']==1)))

fpr = sum((predictions==1)&(loans['loan_status']==0))/(sum((predictions==1)&(loans['loan_status']==0))+sum((predictions==0)&(loans['loan_status']==0)))

print(tpr)
print(fpr)