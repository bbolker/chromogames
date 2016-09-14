import EvoAltC 
import csv
import numpy as np
import matplotlib.pyplot as plt

## if edited and reloading
import importlib 
importlib.reload(EvoAltC)

## run the simulation
#x = runsim(roundnum=10000,rpt_freq=100,b_range_init=(0,0),CHECK=False,
         #  result_type="timeseries")

roundnumb = 100000000
rprt_freq = 10000
npars = 8
avals = (-2,-1,0,1,2)
seeds = (109,108)
colours=('blue','red','black','green','yellow') 
linetypes=('dotted','solid','dashed')
res = np.zeros(shape=(len(avals),len(seeds),roundnumb/rprt_freq+1,npars))
res.fill(np.nan)
## fill array with "not a number" values -- we know which ones are not done yet
for i in range(len(avals)):
   for j in range(len(seeds)):
      res[i,j,:,:] = EvoAltC.runsim(roundnum=roundnumb,rpt_freq=rprt_freq,seed=seeds[j],a_range_init=(avals[i],avals[i]),b_range_init=(0,0),colour_init=(0,10),game_type='chicken',mut_type='add',result_type='timeseries',nsize=2)
      ## save the output as a numpy binary file
      ## efficient, also works for multidim arrays
      np.save(file="test.npy",arr=res)
      print('yes') 
	

## save the output as a CSV file
## (only works conveniently for a 2D array)
## more convenient for loading into other programs (MATLAB, R, etc.)
if False:
     np.savetxt("test.csv", x, delimiter=",")

## read stuff back in
y = np.load("test.npy")

## figures
fig, ax = plt.subplots()
for i in range(len(avals)):
	for j in range(len(seeds)):
		x1=str(avals[i])
		ax.plot(res[i,j,:,0],label='mean A'+x1,color=colours[i],linestyle=linetypes[j])
#ax.plot(res[0,:,1,:])  ## plot parameter 1 across seeds

plt.title('b=0 col=0,10 sd=108,109 mutations=0.01+ nsize=2 chicken frq=10000')

plt.savefig("add-b0-an2-p2-c1-10-1E8r-2.png",figsize=(15,10))





## to run on collywobbles:
##   cd [Dropbox/ ... /code]
##   nohup python3 evotest.py &
