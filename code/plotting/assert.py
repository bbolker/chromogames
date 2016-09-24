import sys
sys.path.insert(0, './../models/')
import EvoAlt
import numpy as np
import importlib
reload(EvoAlt)


rn=100000
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

y = EvoAlt.runsim(a_range_init=(al,au),w=ww,R=RR,P=PP,T=TT,S=SS,roundnum=rn,seed=sd[0],rpt_freq=freq,CHECK=False,result_type='timeseries',mut_sd=(m1,m2,m3),ntype=nntype,mut_type=mtp,nsize=2,switch='off')
z=np.load('test.npy') 

l=np.array_equal(y,z) 
print(l) 
