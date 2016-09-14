import sys
sys.path.insert(0, './../models/')

import EvoAlt8

import importlib 
reload(EvoAlt8) 

rn=50000
sd=[6,14,18,33] 
freq=1000
TT=1.1
SS=-0.1
PP=0
RR=1
al=-4.6
au=-4.5
bl=0 
bu=0
m1=0.02
m2=0.02
m3=0.02 
ns=1
nntype='neu'
mtp='add'
ww=60

x = EvoAlt8.runsim(a_range_init=(al,au),w=ww,R=RR,P=PP,T=TT,S=SS,roundnum=rn,seed=sd[0],rpt_freq=freq,CHECK=False,result_type='timeseries',mut_sd=(m1,m2,m3),ntype=nntype,mut_type=mtp,nsize=2,switch='off')
print('yes')
#x1 = EvoAlt8.runsim(a_range_init=(al,au),w=ww,P=PP,R=RR,T=TT,S=SS,roundnum=rn,seed=sd[1],rpt_freq=freq,CHECK=False,result_type='timeseries',mut_sd=(m1,m2,m3),ntype=nntype,mut_type=mtp,nsize=10,switch='off')
print('yes')

import matplotlib.pyplot as plt
 
plt.title('PD R=1 S=-0.1 T=1.1 P=0 spatial switch=off w=60 mut=1% mutstd=0.02+')
plt.plot(x[:,0],label='mean A(2)', color='blue')
#plt.plot(x[:,1],label='mean B', color='red')
#plt.plot(x[:,2],label='mean colour',color='black')
#plt.plot(x[:,3],label='mean fitness',color='green')
plt.plot(x[:,4],label='std A(2)',color='yellow')
#plt.plot(x[:,5],label='std B',color='cyan')
#plt.plot(x[:,6],label='std Colour',color='orange')
#plt.plot(x[:,7],label='std fitness',color='magenta')

#plt.plot(x1[:,0],label='mean(10)',linestyle='dashed',color='blue')
#plt.plot(x1[:,1],linestyle='dashed',color='red')
#plt.plot(x1[:,2],linestyle='dashed',color='black')
#plt.plot(x1[:,3],linestyle='dashed',color='green')
#plt.plot(x1[:,4],linestyle='dashed',color='yellow')
#plt.plot(x1[:,5],linestyle='dashed',color='cyan')
#plt.plot(x1[:,6],linestyle='dashed',color='orange')
#plt.plot(x1[:,7],linestyle='dashed',color='magenta')

plt.legend(bbox_to_anchor=(-0.03,0.5),prop={'size':11})
plt.ylim([-8,8]) 
plt.xlabel('round number (fqt=1000)') 
plt.show() 

