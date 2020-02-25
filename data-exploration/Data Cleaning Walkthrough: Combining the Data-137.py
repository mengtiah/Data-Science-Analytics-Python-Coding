## 3. Condensing the Class Size Data Set ##

class_size=data['class_size']
class_size=class_size[class_size['PROGRAM TYPE']=='GEN ED']
class_size=class_size[class_size['GRADE ']=='09-12']

## 5. Computing Average Class Sizes ##

import numpy as py
class_size=class_size.groupby('DBN').agg(numpy.mean)
class_size.reset_index(inplace=True)
data['class_size']=class_size
data['class_size'].head()

## 7. Condensing the Demographics Data Set ##

data['demographics']=data['demographics'][data['demographics']['schoolyear']==20112012]
data['demographics'].head()

## 9. Condensing the Graduation Data Set ##

data['graduation']=data['graduation'][data['graduation']['Cohort']=='2006']
data['graduation']=data['graduation'][data['graduation']['Demographic']=='Total Cohort']
print(data['graduation'].head())

## 10. Converting AP Test Scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
for col in cols:
    data['ap_2010'][col]=pd.to_numeric(data['ap_2010'][col],errors="coerce")
print(data['ap_2010'].dtypes)

## 12. Performing the Left Joins ##

combined = data["sat_results"]
combined=combined.merge(data['ap_2010'],on='DBN',how='left')
combined=combined.merge(data['graduation'],on='DBN',how='left')
combined.head()
combined.shape

## 13. Performing the Inner Joins ##

cols=['class_size','demographics','survey','hs_directory']
for col in cols:
    combined=combined.merge(data[col],on='DBN',how='inner')
combined.head()
combined.shape

## 15. Filling in Missing Values ##

mean=combined.mean()
combined=combined.fillna(mean)
combined=combined.fillna(0)
combined.head()

## 16. Adding a School District Column for Mapping ##

def extract(col):
    return col[0:2]
combined['school_dist']=combined['DBN'].apply(extract)
combined['school_dist'].head()