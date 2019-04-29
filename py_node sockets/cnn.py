# Convolution Neural Network
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D, TimeDistributed, LSTM
import numpy as np
import os
import random

DATADIR=r"C:\training_data"

# Load the features set
x=np.load(os.path.join(DATADIR,"features.npy"))

# Reshape x using numpy
x=np.array(x).reshape(-1,8,16,256)
print(x.shape[:])

# Load the labels set
y=np.load(os.path.join(DATADIR,"labels.npy"))

# Shuffle the training data
random.shuffle(x)


#Start building the model
model= Sequential()
