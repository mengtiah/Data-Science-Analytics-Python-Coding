## 2. Calculating expected values ##

males_over50k=32561*.241*.67
males_under50k=32561*.759*.67
females_over50k=32561*.241*.33
females_under50k=32561*.759*.33

## 3. Calculating chi-squared ##

observed=[6662,1179,15128,9592]
expected=[5249.8,2597.4,16533.5,8180.3]
value=[]
for  i, item in enumerate(observed):
    diff=item-expected[i]
    value.append((diff**2)/expected[i])
chisq_gender_income=sum(value)

## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare

observed=[6662,1179,15128,9592]
expected=[5249.8,2597.4,16533.5,8180.3]
chisquare_value, pvalue_gender_income = chisquare(observed, expected)


## 5. Cross tables ##

import pandas

table = pandas.crosstab(income["sex"], [income["race"]])
print(table)

## 6. Finding expected values ##

import numpy as np
from scipy.stats import chi2_contingency
observed = np.array([[119,346,1555,109,8642], [192,693,1569,162,19174]])

chisq_value, pvalue_gender_race, df, expected = chi2_contingency(observed)