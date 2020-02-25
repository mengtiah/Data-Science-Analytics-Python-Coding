## 1. Introduction to the data ##

import pandas as pd
cars = pd.read_csv("auto.csv")

unique_regions=cars['origin'].unique()

## 2. Dummy variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)

dummy_years=pd.get_dummies(cars['year'],prefix='year')

cars=pd.concat([cars,dummy_years],axis=1)

cars=cars.drop(['year','cylinders'],axis=1)

print(cars.head())

## 3. Multiclass classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]

train=shuffled_cars.iloc[:int(shuffled_cars.shape[0]*.7),]
test=shuffled_cars.iloc[int(shuffled_cars.shape[0]*.7):,]


## 4. Training a multiclass logistic regression model ##

from sklearn.linear_model import LogisticRegression

unique_origins = cars["origin"].unique()
unique_origins.sort()

models = {}

features=[c for c in train.columns if c.startswith('cyl') or c.startswith('year')]

for origin in unique_origins:
    lr=LogisticRegression()
    model=lr.fit(train[features],train['origin']==origin)
    models[origin]=model



## 5. Testing the models ##

testing_probs = pd.DataFrame(columns=unique_origins)

for c in testing_probs.columns:
    testing=models[c].predict_proba(test[features])[:,1]
    testing_probs[c]=testing

## 6. Choose the origin ##

predicted_origins=testing_probs.idxmax(axis=1)