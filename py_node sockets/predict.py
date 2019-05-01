# Loads preTRained CNN-LSTM Neural Network
# Performs prediction
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import model_from_json


class Predict():
    
    def __init__(self):
        self.frame_rate=16
        self.num_doppler_bins=16
        self.um_range_bins=64
        
        ####################### LOAD PRETRAINED CNN-LSTM MODEL #######################
        self.json_file = open('model.json', 'r')
        self.loaded_model_json = self.json_file.read()
        self.json_file.close()
        self.loaded_model = model_from_json(self.loaded_model_json)
        # load weights into new model
        self.loaded_model.load_weights("model.h5")
        print("Loaded model from disk")
        
        self.opt=tf.keras.optimizers.Adam(lr=1e-3,decay=1e-5)
        self.loaded_model.compile(loss="sparse_categorical_crossentropy",optimizer=self.opt,metrics=["accuracy"])
        
    def predictGesture(self,frame_sequence):
        pass
