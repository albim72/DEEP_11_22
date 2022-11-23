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

#regresja liniowa
horsepower = np.array(train_features['horsepower'])

horsepower_normalizer = layers.Normalization(input_shape=[1,], axis=None)
horsepower_normalizer.adapt(horsepower)
horsepower_model = tf.keras.Sequential([
horsepower_normalizer,
layers.Dense(units=1)
])

horsepower_model.summary()

horsepower_model.predict(horsepower[:10])

horsepower_model.compile(
    optimizer = tf.optimizers.Adam(learning_rate=0.1),
    loss = 'mean_absolute_error'
)

%%time
history = horsepower_model.fit(
    train_features['horsepower'],
    train_labels,
    epochs=100,
    verbose=0,
    validation_split = 0.2
)
hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()
