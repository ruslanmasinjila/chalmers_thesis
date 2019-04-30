import json
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt


# Hand waving
raw_data_folder=r"C:\chalmers_thesis\data\TurnAround_2019428105659"
destination_data_folder=r"C:\training_data\turn_around"

frames=[]
prefix="\\frame"
frame_rate=16
start_index=50
end_index=1250+start_index+frame_rate




for i in range(start_index,end_index):
    frames.append(np.array(json.load(open(raw_data_folder+prefix+str(i)+".txt"))))
    temp=(frames[-1])/(np.max(frames[-1]))
    frames[-1]=temp[:,0:64].flatten()
    frames[-1]=frames[-1].tolist()



for i in range(len(frames)-frame_rate):
    sequence=[]
    sequence.append(frames[i])
    sequence.append(frames[i+1])
    sequence.append(frames[i+2])
    sequence.append(frames[i+3])
    sequence.append(frames[i+4])
    sequence.append(frames[i+5])
    sequence.append(frames[i+6])
    sequence.append(frames[i+7])
    sequence.append(frames[i+8])
    sequence.append(frames[i+9])
    sequence.append(frames[i+10])
    sequence.append(frames[i+11])
    sequence.append(frames[i+12])
    sequence.append(frames[i+13])
    sequence.append(frames[i+14])
    sequence.append(frames[i+15])
    sequence=(np.array(sequence).flatten()).tolist()
    np.save(destination_data_folder+ "\\frame" + str(i),sequence)