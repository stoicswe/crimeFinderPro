import tensorflow as tf
from tensorflow import keras
import numpy as np

def build_model(hidden, units, activation, outputs):
    model = keras.Sequential()
    for i in range(hidden):
        model.add(keras.layers.Dense(units, activation=activation))
    model.add(keras.layers.Dense(units, activation='softmax'))
    return model

# model.fit(data, labels, epochs=10, batch_size=32, validation_data=(val_data, val_labels))

def train_gradient_descent_model(model, data, labels, epochs, batch):
    model.compile(optimizer=tf.train.GradientDescentOptimizer(0.01), metrics=['accuracy'])
    model.fit(data, labels, epochs=epochs, batch_size=batch)

def train_mean_square_error_reg(model, data, labels, epochs, batch):
    model.compile(optimizer=tf.train.AdamOptimizer(0.01), loss='mse', metrics=['mae'])
    model.fit(data, labels, epochs=epochs, batch_size=batch)

def train_categorial_classification(model, data, labels, epochs, batch):
    model.compile(optimizer=tf.train.RMSPropOptimizer(0.01), loss=keras.losses.categorical_crossentropy, metrics=[keras.metrics.categorical_accuracy])
    model.fit(data, labels, epochs=epochs, batch_size=batch)

def evaluate_batch(model, x, y, batch_size):
    return model.evaluate(x, y, batch_size=batch_size)

def evaluate_steps(model, x, y, steps):
    return model.evaluate(x, y, steps=steps)

def predict_batch(model, x, y, batch_size):
    return model.predict(x, y, batch_size=batch_size)

def predict_steps(model, x, y, steps):
    return model.predict(x, y, steps=steps)

"""X = [[0.0,0.0,1.0],[0.0,1.0,1.0],[1.0,0.0,1.0],[1.0,1.0,1.0]]
y = [[0.0, 1.0, 1.0, 0.0]]
data = np.array(X)
labels = np.array(y).T
syn0 = tf.random_uniform([3,4]) - 1 # 4 is arbitrary, 3 is for inputs
syn1 = tf.random_uniform([4,1]) - 1 # 4 is arbitrary, 1 is for outputs

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for j in range(600):
        l1 = 1 / (1 + tf.exp(-1*(tf.matmul(X,syn0))))
        l2 = 1 / (1 + tf.exp(-1*(tf.matmul(l1,syn1))))
        l2_delta = (y - l2) * (l2 * (1-l2))
        l1_delta = tf.matmul(l2_delta, (tf.transpose(syn1) * (l1 * (1 - 1*l1))))
        syn1 += tf.matmul(tf.transpose(l1), l2_delta)
        syn0 += tf.matmul(tf.transpose(X), l1_delta)
    pl2 = l2.eval()
pl2 = np.array(pl2)[0]
print("PL2")
print(pl2)
print()
print("X    y    y_pred")
print("----------------")
for i in range(len(labels)):
    print(data[i], labels[i], [pl2[i]])"""