## Wed Dec 7 2016. Creating runmean for checking equulibrium of hawk-dove given differnet payoffs. 

import sys
sys.path.insert(0, './../models/')  # safer to do sys.path.append instead of insert.  
import EvoAlt
import numpy as np
import importlib
reload(EvoAlt) 

from datetime import datetime
startTime = datetime.now() 

rn=200000000
sd=3
freq=1000
TT=1.7
SS=0.3
PP=0
RR=1
al=-2.1
au=-2.0
bl=0
bu=0
m1=0.02
m2=0.02
m3=0.02
ns=1
nntype='neu'
mtp='add'
ww=70

x = EvoAlt.runsim(a_range_init=(al,au),w=ww,R=RR,P=PP,T=TT,S=SS,roundnum=rn,seed=sd,rpt_freq=freq,CHECK=False,result_type='timeseries',mut_sd=(m1,m2,m3),ntype=nntype,mut_type=mtp,nsize=ns,switch='off')  

print(datetime.now() - startTime) 















