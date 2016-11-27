#	for i in range(w): 
#		for j in range(w): 
#			if (0.0<=parAlst[i][j]<=1.0):
#				print(True,'A in initial range') 
#			else:
#				print('failure') 
#				sys.exit()           
#       x+=1
#    
#    return(results)

# Running a simulation so that is can be profiled. 
import sys
sys.path.insert(0, '../models/') 

import EvoAlt2

rn=5000
sd=[6,14,18,33]
freq=1000
TT=1
SS=2
PP=0
RR=3
al=0.0
au=1.0
bl=0
bu=0
m1=0.02
m2=0.02
m3=0.02
ns=1
nntype='neu'
mtp='add'
ww=10

def main():
        print('testing..... standby')
        x = EvoAlt2.runsim(a_range_init=(al,au),w=ww,R=RR,P=PP,T=TT,S=SS,roundnum=rn,seed=sd[0],rpt_freq=freq,CHECK=False,result_type='fullstate',mut_sd=(m1,m2,m3),ntype=nntype,mut_type=mtp,nsize=ns,switch='off')
        for i in range(int(rn/freq)): 
		for j in range(ww): 
			for k in range(ww): 
				if (0.0<=x[i][0][j][k]<=1.0):	  
					print(True,'A in initial range') 
				else: 
					print('failure') 
	                                sys.exit()
        print('test complete')

if __name__ == "__main__":
        main()
 
