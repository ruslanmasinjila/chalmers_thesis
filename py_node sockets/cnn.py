# Convolution Neural Network
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D, TimeDistributed, LSTM
import numpy as np
import os

frame_rate=16
num_doppler_bins=16
num_range_bins=64

DATADIR=r"C:\training_data"

# Load the features set
x=np.load(os.path.join(DATADIR,"features.npy"))

print(np.shape(x))
x=np.array(x).reshape(-1,frame_rate,num_doppler_bins,num_range_bins,1)
print(x.shape[1:])

# Load the labels set
y=np.load(os.path.join(DATADIR,"labels.npy"))



#Start building the model
model = Sequential()
####################### TIME DISTRIBUTED CONVOLUTIONAL LAYER #######################
model.add(TimeDistributed(Conv2D(8, (3,3), input_shape=x.shape[1:])))
model.add(TimeDistributed(MaxPooling2D(pool_size=(2,2))))
model.add(TimeDistributed(Flatten()))


####################### LSTM LAYER #######################

model.add(LSTM(64,activation="relu",return_sequences="True"))
model.add(Dropout(0.2))

model.add(LSTM(64,activation="relu"))
model.add(Dropout(0.2))

model.add(Dense(32,activation="relu"))
model.add(Dropout(0.2))

model.add(Dense(4,activation="softmax"))

model.compile(loss="sparse_categorical_crossentropy",optimizer="adam",metrics=["accuracy"])
model.fit(x,y, validation_split=0.2, epochs=3)