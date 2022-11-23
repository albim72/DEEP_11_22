import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

np.set_printoptions(precision=3,suppress=True)

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


#pobieranie danych
#url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'

#column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight','Acceleration','Model Year','Origin','Car name']
raw_dataset = pd.read_csv('auto-mpg.csv',na_values='?',comment='\t',sep=',',skipinitialspace=True) 

dataset = raw_dataset.copy()
dataset.tail()


dataset.isna().sum()

dataset = dataset.dropna()

dataset['origin'] = dataset['origin'].map({1:'USA',2:'Europa',3:'Japonia'})
dataset = pd.get_dummies(dataset,columns=['origin'],prefix='',prefix_sep='')
dataset.tail()

train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)


sns.pairplot(train_dataset[['mpg','cylinders','displacement','weight']],diag_kind='kde')

train_dataset.describe().transpose()

train_features = train_dataset.copy()
test_features = test_dataset.copy()

train_labels = train_features.pop('mpg')
test_labels = test_features.pop('mpg')

train_dataset.describe().transpose()[['mean','std']]

normalizer = tf.keras.layers.Normalization(axis = -1)

normalizer.adapt(np.array(train_features))
