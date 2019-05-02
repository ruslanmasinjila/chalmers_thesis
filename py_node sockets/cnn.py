# CNN-LTSM Neural Network
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, TimeDistributed, LSTM
import numpy as np
import os
from tensorflow.keras.models import load_model

frame_rate=16
num_doppler_bins=16
num_range_bins=64

DATADIR=r"C:\training_data"

# Load the features set
x=np.load(os.path.join(DATADIR,"features.npy"))

print(np.shape(x))
x=np.array(x).reshape(-1,frame_rate,num_doppler_bins,num_range_bins,1)
print(x.shape[:])

# Load the labels set
y=np.load(os.path.join(DATADIR,"labels.npy"))



#Start building the model
model = Sequential()
####################### TIME DISTRIBUTED CONVOLUTIONAL LAYER #######################
model.add(TimeDistributed(Conv2D(8, (3,3), input_shape=x.shape[1:])))
model.add(TimeDistributed(MaxPooling2D(pool_size=(2,2))))
model.add(TimeDistributed(Flatten()))


####################### LSTM LAYER #######################

model.add(LSTM(128,activation="relu",return_sequences="True"))
model.add(Dropout(0.2))

model.add(LSTM(128,activation="relu"))
model.add(Dropout(0.2))

model.add(Dense(64,activation="relu"))
model.add(Dropout(0.2))

model.add(Dense(4,activation="softmax"))

opt=tf.keras.optimizers.Adam(lr=1e-3,decay=1e-5)
model.compile(loss="sparse_categorical_crossentropy",optimizer=opt,metrics=["accuracy"])
model.fit(x,y, validation_split=0.2, epochs=10)


#model.save('model.h5')  # creates a HDF5 file 'my_model.h5'
#del model  # deletes the existing model
#
## returns a compiled model
## identical to the previous one
#model = load_model('model.h5')