import os
import json
import numpy as np


# Hand waving
raw_data_folder=r"C:\chalmers_thesis\data\HandWaving_2019428102740"
destination_data_folder=r"C:\chalmers_thesis\training_data\hand_waving"

frames=[]
prefix="\\frame"
frame_rate=8
start_index=50
end_index=1000+start_index+frame_rate


for i in range(start_index,end_index):
    frames.append(np.array((json.load(open(raw_data_folder+prefix+str(i)+".txt")))))
    temp=frames[-1]
    frames[-1]=temp[:,0:128]




conc_frames=[]
for i in range(len(frames)-frame_rate):
    conc_frames.append(np.vstack((frames[i],frames[i+1],frames[i+2],frames[i+3],frames[i+4],frames[i+5],frames[i+6],frames[i+7])))



for i in range(len(conc_frames)):
    np.save(destination_data_folder+ "\\frame" + str(i),conc_frames[i])