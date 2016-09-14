import EvoAlt3

import importlib 
reload(EvoAlt3) 

rn=100000000
sd=[21,14,18,33] 
freq=1000
TT=1.16
SS=-0.16
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
ww=70	 

x = EvoAlt3.runsim(w=ww,T=TT,S=SS,roundnum=rn,seed=sd[0],rpt_freq=freq,a_range_init=(al,au),b_range_init=(bl,bu),CHECK=False,result_type='timeseries',mut_sd=(m1,m2,m3),ntype=nntype,mut_type=mtp,nsize=1,spatial='on')
print('yes')
x1 = EvoAlt3.runsim(w=ww,T=TT,S=SS,roundnum=rn,seed=sd[1],rpt_freq=freq,a_range_init=(al,au),b_range_init=(bl,bu),CHECK=False,result_type='timeseries',mut_sd=(m1,m2,m3),ntype=nntype,mut_type=mtp,nsize=2,spatial='on')
print('yes')
x2 = EvoAlt3.runsim(w=ww,T=TT,S=SS,roundnum=rn,seed=sd[2],rpt_freq=freq,a_range_init=(al,au),b_range_init=(bl,bu),CHECK=False,result_type='timeseries',mut_sd=(m1,m2,m3),ntype=nntype,mut_type=mtp,nsize=5,spatial='on')
print('yes')
x3 = EvoAlt3.runsim(w=ww,T=TT,S=SS,roundnum=rn,seed=sd[3],rpt_freq=freq,a_range_init=(al,au),b_range_init=(bl,bu),CHECK=False,result_type='timeseries',mut_sd=(m1,m2,m3),mut_type=mtp,ntype=nntype,nsize=10,spatial='on') 
print('yes') 

import matplotlib.pyplot as plt
 
plt.title('70x70 seeds=21,14,18,33 a=-4,6,-4.5 b=0 colour=0,5 mut=0.02+ PD1E8 spatial')
plt.plot(x[:,0],label='mean A(1)', color='blue')
#plt.plot(x[:,1],label='mean B', color='red')
#plt.plot(x[:,2],label='mean colour',color='black')
#plt.plot(x[:,3],label='mean fitness',color='green')
plt.plot(x[:,4],label='std A(1)',color='yellow')
#plt.plot(x[:,5],label='std B',color='cyan')
#plt.plot(x[:,6],label='std Colour',color='orange')
#plt.plot(x[:,7],label='std fitness',color='magenta')

plt.plot(x1[:,0],label='mean A(2)',linestyle='dashed',color='blue')
#plt.plot(x1[:,1],linestyle='dashed',color='red')
#plt.plot(x1[:,2],linestyle='dashed',color='black')
#plt.plot(x1[:,3],linestyle='dashed',color='green')
plt.plot(x1[:,4],label='mean A(2)',linestyle='dashed',color='yellow')
#plt.plot(x1[:,5],linestyle='dashed',color='cyan')
#plt.plot(x1[:,6],linestyle='dashed',color='orange')
#plt.plot(x1[:,7],linestyle='dashed',color='magenta')

plt.plot(x2[:,0],label='mean A(5)',linestyle='dotted',color='blue')
#plt.plot(x2[:,1],linestyle='dotted',color='red')
#plt.plot(x2[:,2],linestyle='dotted',color='black')
#plt.plot(x2[:,3],linestyle='dotted',color='green')
plt.plot(x2[:,4],label='std A(5)',linestyle='dotted',color='yellow')
#plt.plot(x2[:,5],linestyle='dotted',color='cyan')
#plt.plot(x2[:,6],linestyle='dotted',color='orange')
#plt.plot(x2[:,7],linestyle='dotted',color='magenta')

plt.plot(x3[:,0],label='mean A(10)',linestyle='-.',color='blue',marker='+')
#plt.plot(x3[:,1],linestyle='-.',color='red',marker='+')
#plt.plot(x3[:,2],linestyle='-.',color='black',marker='+')
#plt.plot(x3[:,3],linestyle='-.',color='green',marker='+')
plt.plot(x3[:,4],label='mean A(10)',linestyle='-.',color='yellow',marker='+')
#plt.plot(x3[:,5],linestyle='-.',color='cyan',marker='+')
#plt.plot(x3[:,6],linestyle='-.',color='orange',marker='+')
#plt.plot(x3[:,7],linestyle='-.',color='magenta',marker='+')

plt.legend(bbox_to_anchor=(-0.03,0.5),prop={'size':11})
plt.ylim([-8,8]) 
plt.xlabel('round number (fqt=1000)') 
plt.show() 

