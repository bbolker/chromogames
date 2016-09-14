import numpy as np
import EvoAlt3 as ev
roundnumb=30000000 ## was 100000
frq=1000
var=0 #a=0,b=1,col=2
time = 100 
r = ev.runsim(roundnum=roundnumb,rpt_freq=frq,nsize=1,a_range_init=(-4.6,-4.5),b_range_init=(0,0),spatial='on',CHECK=False,result_type='fullstate',mut_sd=(0.02,0.02,0.02),ntype='neu',mut_type='add',T=1.16,S=-0.16)

import matplotlib as mp
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig=plt.figure() 
ims=[] 
for i in range(int(roundnumb/frq)):
    im=plt.imshow(r[i,var,],interpolation="none",animated=True,clim=(-4.6,4.0))
    ims.append([im])

ani = animation.ArtistAnimation(fig,ims,interval=50,blit=True,repeat_delay=1000)

#mp.rcParams['animation.bitrate'] = 100
ani.save('spatial4.mp4',writer='ffmpeg')
plt.show()

plt.close() 
 




