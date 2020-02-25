## 3. Bias-variance tradeoff ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

def train_and_test(cols):
    for i in cols:
        lr=LinearRegression()
        model=lr.fit(filtered_cars[[i]],filtered_cars['mpg'])
        predictions=model.predict(filtered_cars[[i]])
        variance=np.var(predictions)
        mse=mean_squared_error(filtered_cars['mpg'],predictions)
        return(mse, variance)
cyl_mse,cyl_var=train_and_test(['cylinders'])
weight_mse,weight_var=train_and_test(['weight'])


## 4. Multivariate models ##

# Our implementation for train_and_test, takes in a list of strings.
def train_and_test(cols):
    # Split into features & target.
    features = filtered_cars[cols]
    target = filtered_cars["mpg"]
    # Fit model.
    lr = LinearRegression()
    lr.fit(features, target)
    # Make predictions on training set.
    predictions = lr.predict(features)
    # Compute MSE and Variance.
    mse = mean_squared_error(filtered_cars["mpg"], predictions)
    variance = np.var(predictions)
    return(mse, variance)

one_mse, one_var = train_and_test(["cylinders"])
two_mse, two_var = train_and_test(["cylinders", "displacement"])
three_mse, three_var = train_and_test(["cylinders", "displacement", "horsepower"])
four_mse, four_var = train_and_test(["cylinders", "displacement", "horsepower", "weight"])
five_mse, five_var = train_and_test(["cylinders", "displacement", "horsepower", "weight", "acceleration"])
six_mse, six_var = train_and_test(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year"])
seven_mse, seven_var = train_and_test(["cylinders", "displacement", "horsepower", "weight", "acceleration","model year", "origin"])

## 5. Cross validation ##

from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
import numpy as np

def train_and_cross_val(cols):
    features=filtered_cars[cols]
    target=filtered_cars['mpg']
    kf=KFold(n_splits=10, random_state=3, shuffle=True)
    variance_values=[]
    mse_values=[]
    for train_index,test_index in kf.split(features):
        X_train,X_test=features.iloc[train_index],features.iloc[test_index]
        y_train,y_test=target.iloc[train_index],target.iloc[test_index]
        lr=LinearRegression()
        model=lr.fit(X_train,y_train)
        predictions=model.predict(X_test)
        variance=np.var(predictions)
        mse=mean_squared_error(y_test,predictions)
        variance_values.append(variance)
        mse_values.append(mse)
    avg_mse=np.mean(mse_values)
    avg_var=np.mean(variance_values)
    return(avg_mse,avg_var)

two_mse,two_var=train_and_cross_val(['cylinders','displacement'])

three_mse,three_var=train_and_cross_val(['cylinders','displacement','horsepower'])
four_mse,four_var=train_and_cross_val(['cylinders','displacement','horsepower','weight'])
five_mse,five_var=train_and_cross_val(['cylinders','displacement','horsepower','weight','acceleration'])
six_mse,six_var=train_and_cross_val(['cylinders','displacement','horsepower','weight','acceleration','model year'])
seven_mse,seven_var=train_and_cross_val(['cylinders','displacement','horsepower','weight','acceleration','model year','origin'])

## 6. Plotting cross-validation error vs. cross-validation variance ##

# We've hidden the `train_and_cross_val` function to save space but you can still call the function!
import matplotlib.pyplot as plt
        
two_mse, two_var = train_and_cross_val(["cylinders", "displacement"])
three_mse, three_var = train_and_cross_val(["cylinders", "displacement", "horsepower"])
four_mse, four_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight"])
five_mse, five_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration"])
six_mse, six_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year"])
seven_mse, seven_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration","model year", "origin"])

plt.scatter([2,3,4,5,6,7], [two_mse, three_mse, four_mse, five_mse, six_mse, seven_mse], c='red')
plt.scatter([2,3,4,5,6,7], [two_var, three_var, four_var, five_var, six_var, seven_var], c='blue')
plt.show()