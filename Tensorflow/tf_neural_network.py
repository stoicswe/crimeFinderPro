import tensorflow as tf
from tensorflow import keras
import numpy as np

class TFNN():

    def __init__(self, hidden = 2, units = 2, activation = 'sigmoid', outputs = 1):
        self.model = self.build_model(hidden, units, activation, outputs)

    def build_model(self, hidden, units, activation, outputs):
        model = keras.Sequential()
        for i in range(hidden):
            model.add(keras.layers.Dense(units, activation=activation))
        model.add(keras.layers.Dense(units, activation='softmax'))
        return model

    # model.fit(data, labels, epochs=10, batch_size=32, validation_data=(val_data, val_labels))

    def train_gradient_descent_model(self, data, labels, epochs, batch, loss_rate=0.5):
        self.model.compile(optimizer=tf.train.GradientDescentOptimizer(0.01), metrics=['accuracy'], loss=loss_rate)
        self.model.fit(data, labels, epochs=epochs, batch_size=batch)

    def train_mean_square_error_reg(self, data, labels, epochs, batch):
        self.model.compile(optimizer=tf.train.AdamOptimizer(0.01), loss='mse', metrics=['mae'])
        self.model.fit(data, labels, epochs=epochs, batch_size=batch)

    def train_categorial_classification(self, data, labels, epochs, batch):
        self.model.compile(optimizer=tf.train.RMSPropOptimizer(0.01), loss=keras.losses.categorical_crossentropy, metrics=[keras.metrics.categorical_accuracy])
        self.model.fit(data, labels, epochs=epochs, batch_size=batch)

    def evaluate(self, x, y, batch):
        return self.model.evaluate(x, y, batch_size=batch)

    def predict_batch(self, x, batch):
        return self.model.predict(x, batch_size=batch)
    
    def save_model(self):
        self.model.save('my_model.h5')