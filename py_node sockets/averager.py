import json
import numpy as np

directory=r"C:\Users\ruslan\Desktop\ComeTowardsMe_2019411789"

frames=[]

prefix="\\frame"

for i in range(15):
    print(i+1)
    frames.append(json.load(open(directory+prefix+str(i+1)+".txt")))
    
print(frames[0])

