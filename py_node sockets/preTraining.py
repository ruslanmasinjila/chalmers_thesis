import numpy as np
import matplotlib.pyplot as plt
import os
import random
import seaborn as sns



# Directory where the data fro training is stored
DATADIR=r"C:\training_data"

# Categories of gestures
CATEGORIES=["hand_waving","come_towards_me","turn_around","stop"]

# Initialize empty list of training data
training_data=[]

# Put all data in the list along with their corresponding labels
for category in CATEGORIES:
    path=os.path.join(DATADIR,category)
    class_num = CATEGORIES.index(category)
    for frame in os.listdir(path):
        training_data.append([np.load(os.path.join(path,frame)),class_num])

# Shuffle the training data
random.shuffle(training_data)


# Manual separation of features and labels

# Features
x = []

# labels
y = []

for features, label in training_data:
    x.append(features)
    y.append(label)

# Now save the features and labels in compact form
np.save(DATADIR+"\\features",x)
np.save(DATADIR+"\\labels",y)