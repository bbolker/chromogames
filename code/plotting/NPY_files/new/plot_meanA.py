import sys
#sys.path.insert(0, './../models/')  # safer to do sys.path.append instead of insert.  
#import EvoAlt
import numpy as np
import importlib 
#reload(EvoAlt) 

x=np.load('SD_ns2_ic14.npy') 

import matplotlib.pyplot as plt
 
plt.title('SD neighbourhoodsize=1')
plt.plot(x[:,0],label='mean A(2)', color='blue')
#plt.plot(x[:,1],label='mean B', color='red')
#plt.plot(x[:,2],label='mean colour',color='black')
#plt.plot(x[:,3],label='mean fitness',color='green')
#plt.plot(x[:,4],label='std A(2)',color='yellow')
#plt.plot(x[:,5],label='std B',color='cyan')
#plt.plot(x[:,6],label='std Colour',color='orange')
#plt.plot(x[:,7],label='std fitness',color='magenta')


plt.legend(bbox_to_anchor=(-0.03,0.5),prop={'size':11})
plt.ylim([-8,8]) 
plt.xlabel('round number (fqt=1000)') 
plt.show() 

