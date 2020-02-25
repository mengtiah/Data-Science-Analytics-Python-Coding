## 1. Recap ##

import pandas as pd
import numpy as np
np.random.seed(1)

dc_listings = pd.read_csv('dc_airbnb.csv')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

dc_listings.info()

## 2. Removing features ##

drop_columns=['room_type','city','state','latitude','longitude','zipcode','host_acceptance_rate','host_listings_count','host_response_rate']

dc_listings=dc_listings.drop(drop_columns,axis=1)

print(dc_listings.isnull().sum())

## 3. Handling missing values ##

dc_listings=dc_listings.drop(['cleaning_fee','security_deposit'],axis=1)
dc_listings=dc_listings.dropna(axis=0)
dc_listings.isnull().sum()

## 4. Normalize columns ##

normalized_listings = (dc_listings - dc_listings.mean()) / (dc_listings.std())
normalized_listings['price']=dc_listings['price']



normalized_listings.head(3)



## 5. Euclidean distance for multivariate case ##

from scipy.spatial import distance
first_fifth_distance=distance.euclidean(normalized_listings.iloc[0,:][['accommodates','bathrooms']],normalized_listings.iloc[4,:][['accommodates','bathrooms']])

## 7. Fitting a model and making predictions ##

from sklearn.neighbors import KNeighborsRegressor

train_df = normalized_listings.iloc[0:2792]
test_df = normalized_listings.iloc[2792:]
knn = KNeighborsRegressor(n_neighbors=5,algorithm='brute')

knn.fit(train_df[['accommodates','bathrooms']],train_df['price'])

predictions=knn.predict(test_df[['accommodates','bathrooms']])

## 8. Calculating MSE using Scikit-Learn ##

from sklearn.metrics import mean_squared_error

train_columns = ['accommodates', 'bathrooms']
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute', metric='euclidean')
knn.fit(train_df[train_columns], train_df['price'])
predictions = knn.predict(test_df[train_columns])

two_features_mse=mean_squared_error(predictions,test_df['price'])
two_features_rmse=two_features_mse**.5


## 9. Using more features ##

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')

knn.fit(train_df[features],train_df['price'])
four_predictions=knn.predict(test_df[features])

four_mse=mean_squared_error(four_predictions,test_df['price'])
four_rmse=four_mse**.5


## 10. Using all features ##


from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')

knn.fit(train_df.drop('price',axis=1),train_df['price'])
all_features_predictions=knn.predict(test_df.drop('price',axis=1))

all_features_mse=mean_squared_error(all_features_predictions,test_df['price'])
all_features_rmse=all_features_mse**.5
