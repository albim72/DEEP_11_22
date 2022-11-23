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

