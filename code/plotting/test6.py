import EvoAlt6

import importlib 
reload(EvoAlt6) 

rn=10000
sd=[7,108,18,33] 
freq=1000
TT=1.7
SS=0.3
PP=0
RR=1
al=-8
au=9
bl=0 
bu=0
m1=0.02
m2=0.02
m3=0.02 
ns=1
nntype='neu'
mtp='add'
ww=30	 

x = EvoAlt6.runsim(a_range_init=(al,au),w=ww,R=RR,P=PP,T=TT,S=SS,roundnum=rn,seed=sd[0],rpt_freq=freq,CHECK=False,result_type='timeseries',mut_sd=(m1,m2,m3),ntype=nntype,mut_type=mtp,nsize=ns,switch='off',init_type='stripe')
print('yes')
x1 = EvoAlt6.runsim(a_range_init=(al,au),w=ww,P=PP,R=RR,T=TT,S=SS,roundnum=rn,seed=sd[1],rpt_freq=freq,CHECK=False,result_type='timeseries',mut_sd=(m1,m2,m3),ntype=nntype,mut_type=mtp,nsize=ns,switch='off',init_type='stripe')
print('yes')

import matplotlib.pyplot as plt
 
plt.title('SD R=1 S=0.3 T=1.7 P=0 spatial switch=off w=20 stripe')
plt.plot(x[:,0],label='mean A(1)', color='blue')
#plt.plot(x[:,1],label='mean B', color='red')
#plt.plot(x[:,2],label='mean colour',color='black')
#plt.plot(x[:,3],label='mean fitness',color='green')
plt.plot(x[:,4],label='std A(1)',color='yellow')
#plt.plot(x[:,5],label='std B',color='cyan')
#plt.plot(x[:,6],label='std Colour',color='orange')
#plt.plot(x[:,7],label='std fitness',color='magenta')

plt.plot(x1[:,0],linestyle='dashed',color='blue')
#plt.plot(x1[:,1],linestyle='dashed',color='red')
#plt.plot(x1[:,2],linestyle='dashed',color='black')
#plt.plot(x1[:,3],linestyle='dashed',color='green')
plt.plot(x1[:,4],linestyle='dashed',color='yellow')
#plt.plot(x1[:,5],linestyle='dashed',color='cyan')
#plt.plot(x1[:,6],linestyle='dashed',color='orange')
#plt.plot(x1[:,7],linestyle='dashed',color='magenta')

plt.legend(bbox_to_anchor=(-0.03,0.5),prop={'size':11})
plt.ylim([-8,8]) 
plt.xlabel('round number (fqt=1000)') 
plt.show() 

