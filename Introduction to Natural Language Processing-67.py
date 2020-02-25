## 2. Overview of the Data ##

import pandas as pd
submissions = pd.read_csv("sel_hn_stories.csv")
submissions.columns = ["submission_time", "upvotes", "url", "headline"]
submissions = submissions.dropna()

## 3. Tokenizing the Headlines ##

tokenized_headlines = []
for i in submissions.headline:
    words=i.split()
    tokenized_headlines.append(words)

## 4. Preprocessing Tokens to Increase Accuracy ##

punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
clean_tokenized = []

for item in tokenized_headlines:
    new = []
    for i in item:
        for p in punctuation:
            i = i.lower().replace(p,'')
        new.append(i)
    clean_tokenized.append(new)

    

## 5. Assembling a Matrix of Unique Words ##

import numpy as np
unique_tokens = []
single_tokens = []

for item in clean_tokenized:
    for i in item:
        if i not in single_tokens:
            single_tokens.append(i)
        elif i not in unique_tokens:
            unique_tokens.append(i)
        
counts = pd.DataFrame(0, index=np.arange(len(clean_tokenized)),columns=unique_tokens)

## 6. Counting Token Occurrences ##

# We've already loaded in clean_tokenized and counts
for idx, item in enumerate(clean_tokenized):
    for i in item:
        if i in unique_tokens:
            counts.loc[idx,i]+=1

## 7. Removing Columns to Increase Accuracy ##

# We've already loaded in clean_tokenized and counts
word_counts = counts.sum()
counts=counts.loc[:, (5<=word_counts) & (word_counts <=100)]

## 8. Splitting the Data Into Train and Test Sets ##

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(counts, submissions["upvotes"], test_size=0.2, random_state=1)

## 9. Making Predictions With fit() ##

from sklearn.linear_model import LinearRegression

clf = LinearRegression()
clf.fit(X_train,y_train)
predictions = clf.predict(X_test)

## 10. Calculating Prediction Error ##

mse=sum((y_test-predictions)**2)/len(predictions)