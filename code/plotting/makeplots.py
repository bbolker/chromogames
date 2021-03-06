import sys
#sys.path.insert(0, './../models/')  # safer to do sys.path.append instead of insert.  
#import EvoAlt2
import numpy as np
import importlib 
import matplotlib.pyplot as plt 
#reload(EvoAlt2) 

# SD_ns1_a00_c05_b01_mutadd00.npy   ,  SD_ns1_a00_c05_b01_mutadd00-2.npy  ,   SD_ns1_a00_c05_b01_mutadd00-3.npy 

x = np.load('./SD_ns4_ic44.npy') 
plt.title('Mean A and B of colour (0,25)')
plt.plot(x[:,0],label='mean A(2)', color='blue')
plt.plot(x[:,1],label='mean B', color='red')
#plt.plot(x[:,2],label='mean colour',color='black')
#plt.plot(x[:,3],label='mean fitness',color='green')
#plt.plot(x[:,4],label='std A(2)',color='yellow')
#plt.plot(x[:,5],label='std B',color='cyan')
#plt.plot(pt,label='std Colour',color='orange')
#plt.plot(x[:,7],label='std fitness',color='magenta')


plt.legend(bbox_to_anchor=(-0.03,0.5),prop={'size':11})
plt.ylim([-6,6]) 
plt.xlabel('round number (fqt=1000)') 
plt.show() 



