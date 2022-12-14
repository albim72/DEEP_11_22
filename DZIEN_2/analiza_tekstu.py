import matplotlib.pyplot as plt
import os
import re
import shutil
import string
import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import losses


url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
dataset = tf.keras.utils.get_file("aclImdb_v1",url,untar=True,cache_dir='.',
                                  cache_subdir='')

dataset_dir = os.path.join(os.path.dirname(dataset),'aclImdb')

os.listdir(dataset_dir)

train_dir = os.path.join(dataset_dir,'train')
os.listdir(train_dir)

sample_file = os.path.join(train_dir,'pos/1181_9.txt')
with open(sample_file) as f:
    print(f.read())
    
#ładowanie zbioru danych
remove_dir = os.path.join(train_dir,'unsup')
shutil.rmtree(remove_dir)
batch_size = 32
seed = 42
raw_train_ds = tf.keras.utils.text_dataset_from_directory(
    'aclImdb/train',
    batch_size=batch_size,
    validation_split=0.2,
    subset='training',
    seed=seed

)
for text_batch, label_batch in raw_train_ds.take(1):
  for i in range(3):
    print(f"recenzja: {text_batch.numpy()[i]}")
    print(f"etykieta: {label_batch.numpy()[i]}")
print(f"etykieta 0 to recenzja: {raw_train_ds.class_names[0]}")
print(f"etykieta 1 to recenzja: {raw_train_ds.class_names[1]}")

#dane walidacyjne i testowe
raw_val_ds = tf.keras.utils.text_dataset_from_directory(
    'aclImdb/train',
    batch_size=batch_size,
    validation_split=0.2,
    subset='validation',
    seed=seed

)

raw_test_ds = tf.keras.utils.text_dataset_from_directory(
    'aclImdb/test',
    batch_size=batch_size
    
)

#przygotowanie zbioru danych do szkolenia....
def custom_standarization(input_data):
  lowercase = tf.strings.lower(input_data)
  stripped_html = tf.strings.regex_replace(lowercase,'<br />',' ')
  return tf.strings.regex_replace(stripped_html,'[%s]' %re.escape(string.punctuation),'')

max_features = 10000
sequence_length = 250

vectorize_layer = layers.TextVectorization(
    standardize = custom_standarization,
    max_tokens = max_features,
    output_mode = 'int',
    output_sequence_length = sequence_length
)

train_text = raw_train_ds.map(lambda x,y:x)
vectorize_layer.adapt(train_text)


text_batch,label_batch = next(iter(raw_train_ds))
first_review, first_label = text_batch[0], label_batch[0]
print(f"recenzja: {first_review}")
print(f"etykieta: {raw_train_ds.class_names[first_label]}")
print(f"Zwektoryzowana recenzja: {vectorize_text(first_review,first_label)}")

print(f"1287 --> {vectorize_layer.get_vocabulary()[1287]}")
print(f"313 --> {vectorize_layer.get_vocabulary()[313]}")
