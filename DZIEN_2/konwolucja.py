import tensorflow as tf
from tensorflow.keras import datasets,layers,models
import matplotlib.pyplot as plt

#przygotowanie dataset -> CIFAR10
(train_images,train_labels),(test_images,test_labels) = datasets.cifar10.load_data()
train_images,test_images = train_images/255.0, test_images/255.0
