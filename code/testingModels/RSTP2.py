import sys
sys.path.insert(0, '../models/')
import numpy
import EvoAlt2

rn=2000
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
ww=20

def main():
        print('testing..... standby')
        x = EvoAlt2.runsim(a_range_init=(al,au),w=ww,R=RR,P=PP,T=TT,S=SS,roundnum=rn,seed=sd[0],rpt_freq=freq,CHECK=False,result_type='fullstate',mut_sd=(m1,m2,m3),ntype=nntype,mut_type=mtp,nsize=ns,switch='off') 
	for i in range(int(rn/freq)):
                for j in range(ww):
                        for k in range(ww): 
				coop_ctr = EvoAlt2.logistic(x[i][0][j][k]) 
				for i2 in range(int(rn/freq)):
					for j2 in range(ww): 
						for k2 in range(ww): 
							coop_nbr = EvoAlt2.logistic(x[i2][0][j2][k2]) 
							t_ctr=coop_ctr*coop_nbr*RR + coop_ctr*(1-coop_nbr)*SS + (1-coop_ctr)*coop_nbr*TT + (1-coop_ctr)*(1-coop_nbr)*PP
							if (t_ctr<=(RR+SS+TT+PP)):
                                       				 print(True)
                               				else:
                                       				 print("FALE --------------------")
                                       				 sys.exit()
        print('test complete')

if __name__ == "__main__":
        main()



