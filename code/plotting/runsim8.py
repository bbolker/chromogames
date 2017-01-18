import sys
sys.path.insert(0, './../models/')  # safer to do sys.path.append instead of insert.  
import EvoAlt
import numpy as np
import importlib 
reload(EvoAlt) 

outfiletest1 = open('SD_ns1_ic4.npy','w')

rn=250000000
sd=[6,14,18,33] 
freq=1000
TT=1.7
SS=0.3
PP=0
RR=1
al=-4.4
au=-4.3
bl=0 
bu=0
m1=0.02
m2=0.02
m3=0.02 
ns=1
nntype='neu'
mtp='add'
ww=60

x = EvoAlt.runsim(a_range_init=(al,au),w=ww,R=RR,P=PP,T=TT,S=SS,roundnum=rn,seed=sd[0],rpt_freq=freq,CHECK=False,result_type='timeseries',mut_sd=(m1,m2,m3),ntype=nntype,mut_type=mtp,nsize=1,switch='off')

np.save(outfiletest1,x) 

#import matplotlib.pyplot as plt
 
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

