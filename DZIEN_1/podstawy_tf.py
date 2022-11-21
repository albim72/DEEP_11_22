import tensorflow as tf
print(f"wersja tf: {tf.__version__}")

#ładowanie zbioru danych zewnętrznych -> mnist -> obrazki 28x28
mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test) = mnist.load_data()
#normalizacja danych
x_train,x_test = x_train/255.0, x_test/255.0

#budowa modelu
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])


#logit -> wektor wyników /log-odds -> zawsze jeden dla każdej klasy!

predictions = model(x_train[:1]).numpy()
predictions

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1],predictions).numpy()
