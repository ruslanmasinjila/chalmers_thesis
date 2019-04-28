import json
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

directory=r"C:\chalmers_thesis\data\TurnAround_2019428105659"

frames=[]
prefix="\\frame"

aFrame1=np.array(json.load(open(directory+prefix+str(50)+".txt")))
aFrame2=np.array(json.load(open(directory+prefix+str(51)+".txt")))
aFrame3=np.array(json.load(open(directory+prefix+str(52)+".txt")))
aFrame4=np.array(json.load(open(directory+prefix+str(53)+".txt")))
aFrame5=np.array(json.load(open(directory+prefix+str(54)+".txt")))
aFrame6=np.array(json.load(open(directory+prefix+str(55)+".txt")))
aFrame7=np.array(json.load(open(directory+prefix+str(56)+".txt")))
aFrame8=np.array(json.load(open(directory+prefix+str(57)+".txt")))

aFrame1=aFrame1[:,0:128]
aFrame2=aFrame2[:,0:128]
aFrame3=aFrame3[:,0:128]
aFrame4=aFrame4[:,0:128]
aFrame5=aFrame5[:,0:128]
aFrame6=aFrame6[:,0:128]
aFrame7=aFrame7[:,0:128]
aFrame8=aFrame8[:,0:128]






#ax = sns.heatmap(aFrame1)
#plt.show()
#
#ax = sns.heatmap(aFrame2)
#plt.show()
#
#ax = sns.heatmap(aFrame3)
#plt.show()
#
#ax = sns.heatmap(aFrame4)
#plt.show()
#
#ax = sns.heatmap(aFrame5)
#plt.show()
#
#ax = sns.heatmap(aFrame6)
#plt.show()

megaDupa=np.vstack((aFrame1,aFrame2,aFrame3,aFrame4,aFrame5,aFrame6,aFrame7,aFrame8))



ax = sns.heatmap(megaDupa,cmap="cool")
plt.show()
print(np.shape(megaDupa))




#
#for i in range(15):
#    print(i+1)
#    frames.append(json.load(open(directory+prefix+str(i+1)+".txt")))
#    
#print(frames[0])
