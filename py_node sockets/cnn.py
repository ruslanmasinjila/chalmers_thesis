# Convolution Neural Network
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import numpy as np
import os


DATADIR=r"C:\training_data"


# Load the features set
x=np.load(os.path.join(DATADIR,"features.npy"))



# Load the labels set
y=np.load(os.path.join(DATADIR,"labels.npy"))


#Start building the model
model= Sequential()

model.add(Conv2D(8, (3,3), input_shape=x.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Conv2D(8, (3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Flatten())
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(loss="binary_crossentropy",optimizer="adam",metrics=["accuracy"])

model.fit(x,y,batch_size=64, validation_split=0.2, epochs=10)
