import json
import numpy as np

# Hand waving
raw_data_folder=r"C:\chalmers_thesis\data\TurnAround_2019428105659"
destination_data_folder=r"C:\training_data\turn_around"

num_range_bins=256
frames=[]
prefix="\\frame"
frame_rate=8
start_index=50
end_index=1250+start_index+frame_rate


for i in range(start_index,end_index):
    frames.append((json.load(open(raw_data_folder+prefix+str(i)+".txt"))))

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
    np.save(destination_data_folder+ "\\frame" + str(i),sequence)
