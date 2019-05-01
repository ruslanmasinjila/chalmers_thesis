# Loads preTRained CNN-LSTM Neural Network
# Performs prediction
import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.models import model_from_json

frame_rate=16
num_doppler_bins=16
num_range_bins=64

####################### LOAD PRETRAINED CNN-LSTM MODEL #######################
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

opt=tf.keras.optimizers.Adam(lr=1e-3,decay=1e-5)
loaded_model.compile(loss="sparse_categorical_crossentropy",optimizer=opt,metrics=["accuracy"])


####################### LOAD AND FORMAT DATA #######################
DATADIR=r"C:\training_data"

# Load the features set
x=np.load(os.path.join(DATADIR,"features.npy"))
x=np.array(x).reshape(-1,frame_rate,num_doppler_bins,num_range_bins,1)

# Load the labels set
y=np.load(os.path.join(DATADIR,"labels.npy"))

#######################



score = loaded_model.predict_classes(x[0:5])
