'''Importing libraries'''

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import sys

def solve(data):

    df = pd.read_csv('merged_attack_normal_data.csv')
    df.drop('DATETIME', inplace=True, axis='columns' )
    training_data = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    train_index = range(0,len(training_data))
    pca = PCA(n_components=20)
    X_train_PCA = pca.fit_transform(training_data)
    X_train_PCA = pd.DataFrame(data=X_train_PCA, index=train_index)
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X_train_PCA)
    output_labels =[]
    classes = ["Normal", "Attack"]
    data.drop('INDEX(TIME_IN_HOURS)', inplace=True, axis='columns')
    features =[] 
    for col in data.columns:
        features.append(col)
    scaled_pca = pca.fit_transform(data)
    label = kmeans.predict(scaled_pca)
    for l in label:
        if l == 0:
            output_labels.append(classes[0])
        elif l == 1:
            output_labels.append(classes[1])
    result = dict({"TIME" : range(1, len(output_labels)+1), "LABEL": output_labels})
    results = pd.DataFrame(result)
    output = results.set_index('TIME')
    return output 


given_df = pd.read_csv(sys.argv[1])
output = solve(given_df)
output.to_csv("./results.csv")