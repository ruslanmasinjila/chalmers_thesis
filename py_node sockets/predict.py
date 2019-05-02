# Loads preTRained CNN-LSTM Neural Network
# Performs prediction
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model



class Predict():
    
    def __init__(self):
        self.frame_rate=16
        self.num_doppler_bins=16
        self.num_range_bins=64
        
        ####################### LOAD PRETRAINED CNN-LSTM MODEL #######################
        self.model = load_model('model.h5')
        
        self.opt=tf.keras.optimizers.Adam(lr=1e-3,decay=1e-5)
        self.loaded_model.compile(loss="sparse_categorical_crossentropy",optimizer=self.opt,metrics=["accuracy"])
        
        print(self.model.summary())
        
    def predictGesture(self,frame_sequence):
        frame_sequence=np.array(frame_sequence).reshape(self.frame_rate,self.num_doppler_bins,self.num_range_bins,1)
        print(np.shape(frame_sequence))
        #result = self.model.predict(frame_sequence)
        #print(result)
