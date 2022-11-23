import tensorflow as tf

tf.keras.optimizers.Adam(
    learning_rate=0.001,
    beta_1 = 0.9,
    beta_2 = 0.999, #wydajność i szybkość uczenia się
    epsilon = 1e-7, #stabilność numeryczna
    amsgrad = False,#włączenie wariantu algorytmu ADAM -> AMSGradient
    name="Adam", #dodawanie nazwy dla operacji za pomocą Adam.
    #**kwargs -> słownik potencjalnych dodatkowych argumwntów clipvalue, clipnorm...
)


opt = tf.keras.optimizers.Adam(learning_rate=0.1)
var1 = tf.Variable(10.0)
loss = lambda: (var1**2)/2.0
step_count = opt.minimize(loss,[var1]).numpy()
var1.numpy()
