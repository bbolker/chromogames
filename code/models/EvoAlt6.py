#Evolution of group-focused altruism
#Robert White - 001309486
#Dr. Ben Bolker

import random,sys,time,math
from random import randint
import numpy

## This is the logistic function. It will be used to calculate a cell's probability of cooperating.
        
def logistic(x):
        return 1.0/(1.0+math.exp(-x))

def init_sim_stripe(a_range_init,b_range_init,colour_init,w):
          
    parAlst = numpy.zeros((w,w))
	
    parBlst = numpy.zeros((w,w)) 
    colourlst = numpy.zeros((w,w)) 
    for i in range(w): 
	 	 for j in range(w): 
			 if i%2==0: 
				parAlst[i][j]=a_range_init[0]
                                parBlst[i][j]=b_range_init[0]
                                colourlst[i][j]=colour_init[0]
                         else:
                                parAlst[i][j]=a_range_init[1]
                                parBlst[i][j]=b_range_init[1]
                                colourlst[i][j]=colour_init[1]
    return(parAlst,parBlst,colourlst)
    
def init_sim_block(a_range_init,b_range_init,colour_init,w):
	parAlst=numpy.zeros((w,w))
	parBlst=numpy.zeros((w,w)) 
	colourlst=numpy.zeros((w,w))
	z=w/2 
	for i in range(w): 
		for j in range(w): 
			if j < z: 
				parAlst[i][j]=a_range_init[0]
				parBlst[i][j]=b_range_init[0] 
				colourlst[i][j]=colour_init[0] 
			else: 
				parAlst[i][j]=a_range_init[1] 
				parBlst[i][j]=b_range_init[1]
				colourlst[i][j]=colour_init[1]	
        return(parAlst,parBlst,colourlst)

def init_sim_random(a_range_init,b_range_init,colour_init,w):
    """
    
    """
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
    elif (init_type=='block'):
        parAlst,parBlst,colourlst = init_sim_block(a_range_init,b_range_init,colour_init,w) 	
    elif (init_type=="stripe"): 
	parAlst,parBlst,colourlst = init_sim_stripe(a_range_init,b_range_init,colour_init,w)

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
	dCD=S-T
	dDC=T-S
	
	if ntype=='mor':
		for i in D1:
			for j in D2:
				if switch=='on':
					t=logistic(parAlst[i%w][j%w]+parBlst[i%w][j%w]*abs(colourlst[i%w][j%w]-colourlst[dc1][dc2]))*(1-logistic(parAlst[dc1][dc2]+parBlst[dc1][dc2]*abs(colourlst[dc1][dc2]-colourlst[i%w][j%w])))*dCD
					t1=(1-logistic(parAlst[i%w][j%w]+parBlst[i%w][i%w]*abs(colourlst[i%w][j%w]-colourlst[dc1][dc2])))*logistic(parAlst[dc1][dc2]+parBlst[dc1][dc2]*abs(colourlst[dc1][dc2]-colourlst[i%w][j%w]))*dDC 	
					EX.append([i%w,j%w,t+t1])
				
	
	if ntype=='neu':
		PX=0
		for i in range(len(D1)):
			v=len(D1)/2
                        d=abs(i-v) 
			for j in range(d,len(D1)-d):
				I1=D1[i]%w
				I2=D2[j]%w
				if switch=='on': 
					t=logistic(parAlst[I1][I2]+parBlst[I1][I2]*abs(colourlst[I1][I2]-colourlst[dc1][dc2]))*(1-logistic(parAlst[dc1][dc2]+parBlst[dc1][dc2]*abs(colourlst[dc1][dc2]-colourlst[I1][I2])))*dCD
                                	t1=(1-logistic(parAlst[I1][I2]+parBlst[I1][I2]*abs(colourlst[I1][I2]-colourlst[dc1][dc2])))*logistic(parAlst[dc1][dc2]+parBlst[dc1][dc2]*abs(colourlst[dc1][dc2]-colourlst[I1][I2]))*dDC
                                	EX.append([I1,I2,t+t1])
				elif switch=='off':
                                        coop_ctr = logistic(parAlst[dc1][dc2])
                                        coop_nbr = logistic(parAlst[I1][I2])
					t_ctr=coop_ctr*coop_nbr*R + coop_ctr*(1-coop_nbr)*S + (1-coop_ctr)*coop_nbr*T + (1-coop_ctr)*(1-coop_nbr)*P 
					t_nbr=coop_ctr*coop_nbr*R + coop_ctr*(1-coop_nbr)*T + (1-coop_ctr)*coop_nbr*S + (1-coop_ctr)*(1-coop_nbr)*P
					if (dc1==I1 and dc2==I2):
						pass
					else:
						PX+=t_ctr 
					EX.append([I1,I2,t_nbr])
	for i in EX:
		r=1/(1.0+math.exp((i[2]-(PX/4))/0.1)) 
		i.append(r) 

	counter=0 
	for i in EX:
		if (i[0]==dc1 and i[1]==dc2):
			pass
		else:
			  counter+=i[3] 
	
	for i in EX:
		if (i[0]==dc1 and i[1]==dc2):
			pass 
		else:
			i.append(i[3]/counter)
	W=1
	for i in EX:
		if (i[0]==dc1 and i[1]==dc2):
                        pass
		else:
			W*=(1-i[3])  
	det5=float(numpy.random.uniform(0,1.0)) 
	if det5 < W: 
		pass 
	else: 
		det6=float(numpy.random.uniform(0,1.0)) 
		F=0 
		for i in EX:
			if (i[0]==dc1 and i[1]==dc2):
				pass
			else:
				if (F<det6<(F+i[4])):
					parAlst[dc1][dc2]=parAlst[i[0]][i[1]] 
					parBlst[dc1][dc2]=parBlst[i[0]][i[1]]
					colourlst[dc1][dc2]=colourlst[i[0]][i[1]] 
					Fitlst[dc1][dc2]=Fitlst[i[0]][i[1]]
					if CHECK:
						print(F,'<',det6,'<',(F+i[4]))
				else: 
					pass  				  
				F+=i[4]
	if CHECK: 		
		print('*'*10)
		print(dc1,dc2) 
        	print(EX)
        	print('*'*10)
				
		
        if CHECK:
            print("The cell that died this round was","(",dc1,dc2,")","It had fitness,A,B and colour:",Fitlst[dc1][dc2],parAlst[dc1][dc2],parBlst[dc1][dc2],colourlst[dc1][dc2])
            

        ## save old values (for reporting only)
        y1=parAlst[dc1][dc2]
        y2=parBlst[dc1][dc2]
        y3=colourlst[dc1][dc2]

        #Mutation occurs each round.
	DET=float(numpy.random.uniform(0,1.0)) 
	if DET < -1:
        	if mut_type=="mult":
            	   parAlst[dc1][dc2] *= numpy.random.lognormal(0,mut_sd[0])
            	   parBlst[dc1][dc2] *= numpy.random.lognormal(0,mut_sd[1])
            	   colourlst[dc1][dc2] *= numpy.random.lognormal(0,mut_sd[2])
        	elif mut_type=="add":
            	   parAlst[dc1][dc2] += numpy.random.normal(0,mut_sd[0])
            	  #parBlst[dc1][dc2] += numpy.random.normal(0,mut_sd[1])
            	  #colourlst[dc1][dc2] += numpy.random.normal(0,mut_sd[2])
         	else:
         	   raise ValueError("unknown mutation type")
        if CHECK:    
            print("The cell's old fitness and constants were: 0:", y1, y2,y3)
            print("The cell's new fitness and constants are:",Fitlst[dc1][dc2],parAlst[dc1][dc2],parBlst[dc1][dc2],colourlst[dc1][dc2])
            print('-'*50)
        
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
 
