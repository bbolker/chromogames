#Evolution of group-focused altruism
#Robert White - 001309486
#Dr. Ben Bolker

import random,sys,time,math
from random import randint
import numpy

## Testing if reproductive success for all competing cells is equal if R=P=S=T=0.  


## This is the logistic function. It will be used to calculate a cell's probability of cooperating.
def logistic(x):
        return 1.0/(1.0+math.exp(-x))
def init_sim_random(a_range_init,b_range_init,colour_init,w):
    
    ## The three parameters a,b and colour are given to each cell in the 100x100 lattice.
    if a_range_init[0]==0 and a_range_init[1]==0:
        parAlst = numpy.zeros((w,w))
    else:
        parAlst = numpy.random.uniform(a_range_init[0],a_range_init[1],size=(w,w))
    if b_range_init[0]==0 and b_range_init[1]==0:
        parBlst = numpy.zeros((w,w))
    else:
        parBlst = numpy.random.uniform(b_range_init[0],b_range_init[1],size=(w,w))
    if colour_init[0]==0 and colour_init[1]==0:
        colourlst = numpy.zeros((w,w))
    else:
        colourlst = numpy.random.uniform(colour_init[0],colour_init[1],size=(w,w))
    return(parAlst,parBlst,colourlst)

#A function that returns an array with three elements. The first two elements are the position of the agent/organism in the lattice. The third element is the (m,n)'s average payoff with its neuman neighbourhood of size "nsize". 
def PY(m,n,nsize,ntype,w,parAlst,R,S,T,P):
	
	D1=range(m-nsize,m+1+nsize)
        D2=range(n-nsize,n+1+nsize)
	X=[]
	if ntype=='neu':
		count1=0
                py=0
                for i in range(len(D1)):
                        v=len(D1)/2
                        d=abs(i-v)
                        for j in range(d,len(D1)-d):
                                I1=D1[i]%w
                                I2=D2[j]%w
                                coop_ctr = logistic(parAlst[m][n])
				coop_nbr = logistic(parAlst[I1][I2])
                                t_ctr=coop_ctr*coop_nbr*R + coop_ctr*(1-coop_nbr)*S + (1-coop_ctr)*coop_nbr*T + (1-coop_ctr)*(1-coop_nbr)*P
				if (t_ctr<=(R+S+T+P)):
					pass 
					#print(True) 
				else: 
					print("FALSE---------- unexpected expected payoff --------------------")
					sys.exit()  
                                if (m==I1 and n==I2):
                                        pass
                                else:
                                        py+=t_ctr
					X.append([I1,I2])
					count1+=1
	Y=[m,n,py/count1]
	return(Y) 
def successful_mate(A,b,c,k):  
	win=[] 
        for i in A:
                r=1/(1.0+math.exp((A[4][2]-i[2])/k))
                i.append(r)
        counter=0
	num=0
        for i in A:
                if (i[0]==b and i[1]==c):
                        pass
                else:
                          counter+=i[3]
			  num+=1.0
	#print(num) 
        # Appending the propotion with respect to r of each cell participating in the game. 
        for i in A:
                if (i[0]==b and i[1]==c):
                        pass
                else:
                        i.append(i[3]/counter)
			if ((1/num) == i[3]/counter): 
				print(True, "all neighnours have equal reproducitive success prob") 
			else: 
				print('error; unexpected reproductive success probability') 
				sys.exit() 
        W=1
        #Finding the probability that the cell's outside do not populate the center cell. 
        for i in A:
                if (i[0]==b and i[1]==c):
                        pass
                else:
                        W*=(1-i[3]) 
        det5=float(numpy.random.uniform(0,1.0))
        if det5 < W:
                pass
        else:
                det6=float(numpy.random.uniform(0,1.0))
                F=0
                for i in A:
                        if (i[0]==b and i[1]==c):
                                pass
                        else:
                                if (F<det6<(F+i[4])):
                                        win=[i[0],i[1]]
                                else:
                                        pass
                                F+=i[4]
	return(win)


#A funtion that runs a game similar to that in the univie tutorial on spatial mixed strategies.
def runsim(roundnum=10000,CHECK=False,
	   switch='off',
           a_range_init=(0,1.0),
           colour_init=(0,5.0),
	   R=3,
	   S=1,
	   T=4,
	   P=0,
           init_type="random",
           b_range_init=(-4.0,4.0),
	   ntype='mor',              ## mor = moore, neu=neuman
           nsize=1,                  ## neighbourhood size
           w=100,                    ## world size
           result_type="fullstate",  ## 'timeseries', 'endstate'
           rpt_freq=1000,
           mut_sd = (0.01,)*3,  ## std dev of mutation (A,B,colour)
           mut_type = "add",   ## multiplicative ("mult") or additive ("add")
           seed=None):
    """
    docstring should go here describing parameters
    """
	# decide on how you would like the results of the game. 	
    n_rpt = roundnum // rpt_freq + 1
    if result_type=="timeseries":
       results = numpy.zeros((n_rpt,8))
    elif result_type=="fullstate":
       results = numpy.zeros((n_rpt,3,w,w))
    elif result_type=="endstate":
        results=numpy.zeros((1,3,w,w)) 
    else:
        raise ValueError("unknown result_type")
    
    ##plant a seed.
    if (seed != None):
        numpy.random.seed(seed)
    
    ## The list Fitlst is made into an appropriate-sized grid.
    Fitlst = numpy.zeros((w,w))

    if (init_type=="random"):
        parAlst,parBlst,colourlst = init_sim_random(a_range_init,b_range_init,colour_init,w)
    
    x = 1
    #The game loop is started.
    
    counter=0
    while x <= roundnum: 
        #Randomly selects a cell to die. A death is simulated by removing all of the information from the cell and making it zero.
        
        dc1 = numpy.random.randint(0,w)                             
        dc2 = numpy.random.randint(0,w)
	
	D1=range(dc1-nsize,dc1+1+nsize)
	D2=range(dc2-nsize,dc2+1+nsize) 
	EX=[]
	
	#The average payoff of each cell centered at (dc1,dc2) and radius nsize is calculated. EX stores the cells locations and corresponding average payoff with their respective neighbours. 
	if ntype=='neu':
		count2=0
		PX=0
		for i in range(len(D1)):
			v=len(D1)/2
                        d=abs(i-v) 
			for j in range(d,len(D1)-d):
				Z1=D1[i]%w
				Z2=D2[j]%w
				if switch=='off':
                                        coop_ctr = logistic(parAlst[dc1][dc2])
                                        coop_nbr = logistic(parAlst[Z1][Z2])
					t_ctr=coop_ctr*coop_nbr*R + coop_ctr*(1-coop_nbr)*S + (1-coop_ctr)*coop_nbr*T + (1-coop_ctr)*(1-coop_nbr)*P 
					if (t_ctr<=(R+S+T+P)): 
						#print(True)
						pass 
					else: 
						print("FALSE------------ unexpected expected payoff --------------------------") 
						sys.exit() 

					if (dc1==Z1 and dc2==Z2):
						pass
					else:
						PX+=t_ctr
						kd=PY(Z1,Z2,nsize,ntype,w,parAlst,R,S,T,P) 
						EX.append(kd)
						count2+=1 
		EX.append([dc1,dc2,PX/count2])
		# print(EX) 
	k=0.1  # Selection parameter. FIX ME (add to runsim) !!!! 
	B=successful_mate(EX,dc1,dc2,k)
	if (len(B)!=0):
		parAlst[dc1][dc2]=parAlst[B[0]][B[1]]
        	parBlst[dc1][dc2]=parBlst[B[0]][B[1]]
        	colourlst[dc1][dc2]=colourlst[B[0]][B[1]]
        	Fitlst[dc1][dc2]=Fitlst[B[0]][B[1]]
	else: 
		pass

        ## save old values (for reporting only)
        y1=parAlst[dc1][dc2]
        y2=parBlst[dc1][dc2]
        y3=colourlst[dc1][dc2]

        #Mutation occurs each round.
	DET=float(numpy.random.uniform(0,1.0)) 
	if DET < 0.01:
        	if mut_type=="add":
            	   parAlst[dc1][dc2] += numpy.random.normal(0,mut_sd[0])
            	  #parBlst[dc1][dc2] += numpy.random.normal(0,mut_sd[1])
            	  #colourlst[dc1][dc2] += numpy.random.normal(0,mut_sd[2])
         	else:
         	   raise ValueError("unknown mutation type")

        # Storing the results in an array. 
        if x%rpt_freq==0:
            if result_type=="timeseries":
                # compute summary statistics
                cur_vals = (numpy.mean(parAlst),numpy.mean(parBlst),numpy.mean(colourlst),numpy.mean(Fitlst),numpy.std(parAlst),numpy.std(parBlst),numpy.std(colourlst),numpy.std(Fitlst))
                results[x//rpt_freq,] = cur_vals
            elif result_type=="fullstate":
                results[x//rpt_freq,0,] = parAlst
                results[x//rpt_freq,1,] = parBlst
                results[x//rpt_freq,2,] = colourlst
        if result_type=="endstate":
            results[1,0,]=parAlst
            results[1,1,]=parBlst
            results[1,2,]=colourlst
                
        x+=1
    
    return(results)

# Running a simulation so that is can be profiled. 
rn=5000
sd=[6,14,18,33]
freq=1000
TT=0
SS=0
PP=0
RR=0
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


def main():
        print('testing..... standby')
        x = runsim(a_range_init=(al,au),w=ww,R=RR,P=PP,T=TT,S=SS,roundnum=rn,seed=sd[0],rpt_freq=freq,CHECK=False,result_type='timeseries',mut_sd=(m1,m2,m3),ntype=nntype,mut_type=mtp,nsize=ns,switch='off') 
	numpy.save('zeroGamecheck.npy',x)
        print('test complete')

if __name__ == "__main__":
        main()
 
