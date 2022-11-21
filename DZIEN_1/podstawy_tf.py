import tensorflow as tf
print(f"wersja tf: {tf.__version__}")

#ładowanie zbioru danych zewnętrznych -> mnist -> obrazki 28x28
mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test) = mnist.load_data()
#normalizacja danych
x_train,x_test = x_train/255.0, x_test/255.0
