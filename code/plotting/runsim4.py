import sys
sys.path.insert(0, './../models/')  # safer to do sys.path.append instead of insert.  
import EvoAlt2
import numpy as np
import importlib 
reload(EvoAlt2) 

outfiletest1 = open('SD_ns1_a00_c025_b01_mutadd00-3-1.npy','w')

x = EvoAlt2.runsim(roundnum=1000000000, a_range_init=(0,0),colour_init=(0,25),R=1,S=0.3,T=1.7,P=0,w=60,seed=10,rpt_freq=1000,CHECK=False,result_type='timeseries', mut_sd=(0,0.02,0.02), ntype='neu', mut_type='add',nsize=1,switch='off',b_range_init=(1,1))   

np.save(outfiletest1,x) 
 
#plt.title('SDagain nsize=1 test2 w=60 mut=1% mutstd=0.02+')
#plt.plot(x[:,0],label='mean A(2)', color='blue')
#plt.plot(x[:,1],label='mean B', color='red')
#plt.plot(x[:,2],label='mean colour',color='black')
#plt.plot(x[:,3],label='mean fitness',color='green')
#plt.plot(x[:,4],label='std A(2)',color='yellow')
#plt.plot(x[:,5],label='std B',color='cyan')
#plt.plot(x[:,6],label='std Colour',color='orange')
#plt.plot(x[:,7],label='std fitness',color='magenta')


#plt.legend(bbox_to_anchor=(-0.03,0.5),prop={'size':11})
#plt.ylim([-8,8]) 
#plt.xlabel('round number (fqt=1000)') 
#plt.show() 

