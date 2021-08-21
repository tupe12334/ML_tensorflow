from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
from keras.optimizer_v1 import Adam
from keras.optimizer_v2 import adam
import pandas as pd
import os

x_data_path = os.path.join(os.getcwd(), "VXX", "vxx_data.csv")
x_data = pd.read_csv(x_data_path)
x_data.pop("Date")
x_data.pop("Time")
x_data.pop("open")
x_data.pop("close")
x_data.pop("high")
x_data.pop("low")
y_data_path = os.path.join(os.getcwd(), "VXX", "vxx_y.csv")
y_data = pd.read_csv(y_data_path)
y_data.pop("Date")
y_data.pop("Time")


print(y_data)
print(x_data)

# model = Sequential(
#     layers=[
#         Dense(10, input_shape=(10,), activation="sigmoid"),
#         Dense(8, activation="sigmoid"),
#         Dense(5, activation="sigmoid"),
#         Dense(1),
#     ]
# )
# # model.summary()
# model.compile(
#     optimizer="adam",
#     loss="sparse_categorical_crossentropy",
#     metrics=["accuracy"],
# )
# model.fit(x=x_data, y=y_data, batch_size=40, epochs=30, shuffle=True, verbose=2)
