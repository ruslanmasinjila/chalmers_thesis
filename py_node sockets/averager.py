import json
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

directory=r"C:\chalmers_thesis\data\Stop_2019427233636"

frames=[]
prefix="\\frame"

aFrame1=np.array(json.load(open(directory+prefix+str(1)+".txt")))
aFrame2=np.array(json.load(open(directory+prefix+str(2)+".txt")))
aFrame3=np.array(json.load(open(directory+prefix+str(3)+".txt")))
aFrame4=np.array(json.load(open(directory+prefix+str(4)+".txt")))
aFrame5=np.array(json.load(open(directory+prefix+str(5)+".txt")))
aFrame6=np.array(json.load(open(directory+prefix+str(6)+".txt")))
aFrame7=np.array(json.load(open(directory+prefix+str(7)+".txt")))
aFrame8=np.array(json.load(open(directory+prefix+str(8)+".txt")))

aFrame1=aFrame1[:,0:60]
aFrame2=aFrame2[:,0:60]
aFrame3=aFrame3[:,0:60]
aFrame4=aFrame4[:,0:60]
aFrame5=aFrame5[:,0:60]
aFrame6=aFrame6[:,0:60]
aFrame7=aFrame7[:,0:60]
aFrame8=aFrame8[:,0:60]






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

ax = sns.heatmap(megaDupa)
plt.show()





#
#for i in range(15):
#    print(i+1)
#    frames.append(json.load(open(directory+prefix+str(i+1)+".txt")))
#    
#print(frames[0])
