## 1. Introduction ##

import numpy as np
import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

dc_listings_index=np.random.permutation(dc_listings.index)
dc_listings=dc_listings.reindex(dc_listings_index)
split_one=dc_listings.iloc[:1862].copy()
split_two=dc_listings.iloc[1862:].copy()

## 2. Holdout Validation ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one

knn=KNeighborsRegressor(n_neighbors=5,algorithm='auto')
knn.fit(train_one[['accommodates']],train_one['price'])
pred1=knn.predict(test_one[['accommodates']])
iteration_one_rmse=mean_squared_error(test_one['price'],pred1)**.5

knn=KNeighborsRegressor(n_neighbors=5,algorithm='auto')
knn.fit(train_two[['accommodates']],train_two['price'])
pred2=knn.predict(test_two[['accommodates']])
iteration_two_rmse=mean_squared_error(test_two['price'],pred2)**.5

avg_rmse=numpy.mean([iteration_one_rmse,iteration_two_rmse])

## 3. K-Fold Cross Validation ##

dc_listings.loc[dc_listings.index[:745],'fold']=1
dc_listings.loc[dc_listings.index[745:1490],'fold']=2
dc_listings.loc[dc_listings.index[1490:2234],'fold']=3
dc_listings.loc[dc_listings.index[2234:2978],'fold']=4
dc_listings.loc[dc_listings.index[2978:3723],'fold']=5
print(dc_listings.fold.value_counts())
print(dc_listings.fold.isnull())


## 4. First iteration ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
knn=KNeighborsRegressor()
knn.fit(dc_listings[dc_listings['fold']!=1][['accommodates']],dc_listings[dc_listings['fold']!=1]['price'])
labels=knn.predict(dc_listings[dc_listings['fold']==1][['accommodates']])
iteration_one_rmse=mean_squared_error(dc_listings[dc_listings['fold']==1]['price'],labels)**.5



## 5. Function for training models ##

# Use np.mean to calculate the mean.
import numpy as np
fold_ids = [1,2,3,4,5]
def train_and_validate(dc_listings,folds):
    rmses=[]
    from sklearn.neighbors import KNeighborsRegressor
    from sklearn.metrics import mean_squared_error
# Training
    model = KNeighborsRegressor()
    for k in folds:
        train_iteration_one = dc_listings[dc_listings["fold"] != k]
        test_iteration_one = dc_listings[dc_listings["fold"] == k].copy()
        model.fit(train_iteration_one[["accommodates"]],
                  train_iteration_one["price"])
        labels = model.predict(test_iteration_one[["accommodates"]])
        test_iteration_one["predicted_price"] = labels
        iteration_one_mse =mean_squared_error(test_iteration_one["price"],test_iteration_one["predicted_price"])
        iteration_one_rmse = iteration_one_mse ** (1/2)
        rmses.append(iteration_one_rmse)
    return rmses

rmses=train_and_validate(dc_listings,fold_ids)
avg_rmse=np.mean(rmses)




## 6. Performing K-Fold Cross Validation Using Scikit-Learn ##

from sklearn.model_selection import cross_val_score, KFold

kf = KFold(5, shuffle=True, random_state=1)

knn=KNeighborsRegressor()

mses=cross_val_score(knn, dc_listings[['accommodates']], dc_listings['price'], scoring="neg_mean_squared_error", cv=kf)

avg_rmse=np.mean(abs(mses)**.5)


## 7. Exploring Different K Values ##

from sklearn.model_selection import cross_val_score, KFold

num_folds = [3, 5, 7, 9, 10, 11, 13, 15, 17, 19, 21, 23]

for fold in num_folds:
    kf = KFold(fold, shuffle=True, random_state=1)
    model = KNeighborsRegressor()
    mses = cross_val_score(model, dc_listings[["accommodates"]], dc_listings["price"], scoring="neg_mean_squared_error", cv=kf)
    rmses = np.sqrt(np.absolute(mses))
    avg_rmse = np.mean(rmses)
    std_rmse = np.std(rmses)
    print(str(fold), "folds: ", "avg RMSE: ", str(avg_rmse), "std RMSE: ", str(std_rmse))
