import keras
import pandas as pd
import os
from keras import Sequential, layers, activations, optimizers
import tensorflow as tf

y_train_path = os.path.join(os.getcwd(), "Titanic", "Data", "gender_submission.csv")
y_train = pd.read_csv(y_train_path)

x_train_path = os.path.join(os.getcwd(), "Titanic", "Data", "train.csv")
x_train = pd.read_csv(x_train_path)

x_test_path = os.path.join(os.getcwd(), "Titanic", "Data", "test.csv")
x_test = pd.read_csv(x_train_path)

model = Sequential(
    [layers.Dense(32, activation=tf.nn.relu, input_shape=[1]), layers.Dense(2)]
)

optimaizer = optimizers.rmsprop_v2(0.999)

