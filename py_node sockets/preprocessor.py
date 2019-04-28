import json
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt


# Hand waving
raw_data_folder=r"C:\chalmers_thesis\data\HandWaving_2019428102740"
destination_data_folder=r"C:\chalmers_thesis\training_data\stop"

frames=[]
prefix="\\frame"
frame_rate=8
start_index=50
end_index=1250+start_index+frame_rate


for i in range(start_index,end_index):
    frames.append(np.array((json.load(open(raw_data_folder+prefix+str(i)+".txt")))))
    temp=frames[-1]
    
    # Remove range bins out of range
    frames[-1]=temp[:,0:128]
    
    #standardize data to [0,1]
    frames[-1]=(frames[-1]-np.min(frames[-1]))/(np.max(frames[-1])-np.min(frames[-1]))




conc_frames=[]
for i in range(len(frames)-frame_rate):
    conc_frames.append(np.vstack((frames[i],frames[i+1],frames[i+2],frames[i+3],frames[i+4],frames[i+5],frames[i+6],frames[i+7])))
    
ax = sns.heatmap(conc_frames[750],cmap="cool")
plt.show()




#for i in range(len(conc_frames)):
#    np.save(destination_data_folder+ "\\frame" + str(i),conc_frames[i])