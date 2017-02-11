import numpy as np
import votermodel as vm 

roundnumb=3000 ## was 100000
time = 0.1
r = vm.runvoter(roundnum=roundnumb,w=6, n_rpt=100, rng=[0,3],)

import matplotlib as mp
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors

fig=plt.figure() 
ims=[] 
cmap = colors.ListedColormap(['red','green','blue']) 
bounds=[0,1,2,4] 
norm = colors.BoundaryNorm(bounds, cmap.N) 
 
for i in range(int(roundnumb)):
    im=plt.imshow(r[i],interpolation="nearest",animated=True,cmap=cmap,norm=norm)
    ims.append([im])

ani = animation.ArtistAnimation(fig,ims,interval=50,blit=True,repeat_delay=1000)

#mp.rcParams['animation.bitrate'] = 100
ani.save('new123.mp4',writer='ffmpeg')
plt.show()

plt.close() 
 




