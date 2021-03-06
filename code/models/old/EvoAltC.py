#Evolution of group-focused altruism
#Robert White - 001309486
#Dr. Ben Bolker

import random,sys,time,math
from random import randint
import numpy

def runsim(roundnum=10000,CHECK=False,
           a_range_init=(-4.0,4.0),
           colour_init=(0,5.0),
           b_range_init=(-4.0,4.0),
           game_type='PD',
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
    
    
    ## This is the logistic function. It will be used to calculate a cell's probability of cooperating.
        
    def logistic(x):
        return 1.0/(1.0+math.exp(-x))
    
    
    x = 1
    #The game loop is started.
    
    counter=0
    while x <= roundnum: 
        #A cell on the lattice is chosen at random. 
        rc1 = numpy.random.randint(0,w-1)                         
        rc2 = numpy.random.randint(0,w-1)
        ## print((rc1,rc2))
        
        #These following statements find a neighbour cell.
    
        A1= range(rc1-nsize,rc1+1+nsize)
        A2= range(rc2-nsize,rc2+1+nsize)
	
	if ntype == 'mor':
        	c1=numpy.random.randint(0,len(A1)-1)
        	c2=numpy.random.randint(0,len(A2)-1)
        	rnc1=A1[c1]%w
        	rnc2=A2[c2]%w

        	while (rnc1==rc1 and rnc2==rc2):
              	        c1= numpy.random.randint(0,len(A1)-1)
            		c2= numpy.random.randint(0,len(A2)-1)
            	        rnc1 = A1[c1]%w
            	        rnc2 = A2[c2]%w
			
	elif ntype == 'neu':
		c1=numpy.random.randint(0,len(A1)-1) 
		rnc1=A1[c1]%w
		v=len(a1)/2 
		d=abs(c1-v) 
		c2=numpy.random.randint(d,len(A1)-1-d) 
		rnc2=A2[c2]%w 
		
		while (rnc1==rc1 and rnc2==rc2):
			c1=numpy.random.randint(0,len(A1)-1) 
			rnc1=A1[c1]%w 
			v=len(a1)/2
			d=abs(c1-v) 
			c2=numpy.random.randint(d,len(A1)-d-1) 
			rnc2=A2[c2]%w			 		
		
        ## print((rnc1,rnc2))        
        if CHECK:
            print('************************ROUND ',x,'************************************')
            print("The cell choosen at random was","(",rc1,rc2,")")
            print("The neighbour cell was","(",rnc1,rnc2,")")
            print("The probability that the choosen cell was going to cooperate was" , logistic(parAlst[rc1][rc2]+parBlst[rc1][rc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])))
            print("The probability that the neighbour cell was going to cooperate was" , logistic(parAlst[rnc1][rnc2]+parBlst[rnc1][rnc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])))      
            print("The fitness of the choosen cell was:", Fitlst[rc1][rc2])
            print("The fitness of the neighbour was:", Fitlst[rnc1][rnc2])
            print("Standby for results...")
        
        R=3
	S=1
	T=4
	P=2
        
        
        #The neighbour and choosen cell are asked if they want to cooperate with each other. 
        
        det = float(numpy.random.uniform(0,1.0))
        if CHECK:
            print('!!!!!!!!!',det)
        
        if game_type=='PD':    
            if det < logistic(parAlst[rnc1][rnc2]+parBlst[rnc1][rnc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])) and det < logistic(parAlst[rc1][rc2]+parBlst[rc1][rc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])):
                Fitlst[rnc1][rnc2] = Fitlst[rnc1][rnc2] + R
                Fitlst[rc1][rc2] = Fitlst[rc1][rc2] + R
                counter+=2
                if CHECK:
                    print("The neighbour cell and the choosen cell cooperated!")
                
            
            elif det < logistic(parAlst[rnc1][rnc2]+parBlst[rnc1][rnc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])) and det > logistic(parAlst[rc1][rc2]+parBlst[rc1][rc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])):
                Fitlst[rnc1][rnc2] = Fitlst[rnc1][rnc2] S
                Fitlst[rc1][rc2] = Fitlst[rc1][rc2] + T
                counter+=1
                if CHECK:
                    print("The neighbour cell cooperated and the choosen cell did not cooperate!")
                
           
            elif det > logistic(parAlst[rnc1][rnc2]+parBlst[rnc1][rnc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])) and det < logistic(parAlst[rc1][rc2]+parBlst[rc1][rc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])):
                Fitlst[rnc1][rnc2] = Fitlst[rnc1][rnc2] + T
                Fitlst[rc1][rc2] = Fitlst[rc1][rc2] + S
                counter+=1
                if CHECK:
                    print("The neighbour cell did not cooperate and the choosen cell did cooperate!")
                
            else:
                Fitlst[rnc1][rnc2] = Fitlst[rnc1][rnc2] + P 
                Fitlst[rc1][rc2] = Fitlst[rc1][rc2] + P
                if CHECK:
                    print("The neighbour and choosen cell did not cooperate!")

        elif game_type=="SD":
            if det < logistic(parAlst[rnc1][rnc2]+parBlst[rnc1][rnc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])) and det < logistic(parAlst[rc1][rc2]+parBlst[rc1][rc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])):
                Fitlst[rnc1][rnc2]=Fitlst[rnc1][rnc2] + R
                Fitlst[rc1][rc2]=Fitlst[rc1][rc2] + R
            elif det < logistic(parAlst[rnc1][rnc2]+parBlst[rnc1][rnc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])) and det > logistic(parAlst[rc1][rc2]+parBlst[rc1][rc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])):
                Fitlst[rnc1][rnc2]=Fitlst[rnc1][rnc2] + S
                Fitlst[rc1][rc2]=Fitlst[rc1][rc2] + T
            elif det > logistic(parAlst[rnc1][rnc2]+parBlst[rnc1][rnc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])) and det < logistic(parAlst[rc1][rc2]+parBlst[rc1][rc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])):
                Fitlst[rnc1][rnc2]=Fitlst[rnc1][rnc2] + T
                Fitlst[rc1][rc2]=Fitlst[rc1][rc2] + S
            else:
                Fitlst[rnc1][rnc2]=Fitlst[rnc1][rnc2] + P
                Fitlst[rc1][rc2]=Fitlst[rc1][rc2] + P
        else:
            raise ValueError("unknown game type: "+game_type)
                
        if CHECK:
            print("The new fitness of the choosen cell after the round was:", Fitlst[rc1][rc2])
            print("The new fitness of the neighbour cell after the round was: ", Fitlst[rnc1][rnc2])
        
    
        #Randomly selects a cell to die. A death is simulated by removing all of the information from the cell and making it zero.
        
        dc1 = numpy.random.randint(0,w-1)                             
        dc2 = numpy.random.randint(0,w-1)
	
	D1=range(dc1-nsize,dc1+1+nsize)
	D2=range(dc2-nsize,dc2+1+nsize) 
	EX=[]
	dCC=
	dCD=
	d=
	dDD=
	
	if ntype=='mor':
		for i in D1:
			for j in D2:
				EX.append([i,j])  
	
        Fitlst[dc1][dc2] = 0              
        parAlst[dc1][dc2] = 0
        parBlst[dc1][dc2] = 0
        if CHECK:
            print("The cell that died this round was","(",dc1,dc2,")","It had fitness,A,B and colour:",Fitlst[dc1][dc2],parAlst[dc1][dc2],parBlst[dc1][dc2],colourlst[dc1][dc2])
        
        ## The dead cell is replaced by one of the two cells who had just competed. 
    
        det2 = numpy.random.uniform(0.0,1.0)
        ## print(det2)
            
        FIT = (math.exp(Fitlst[rc1][rc2]))/(math.exp(Fitlst[rnc1][rnc2]) + math.exp(Fitlst[rc1][rc2])) 
        ## print(FIT)
        if det2 < FIT:          
            parAlst[dc1][dc2] = parAlst[rc1][rc2]
            parBlst[dc1][dc2] = parBlst[rc1][rc2]
            colourlst[dc1][dc2] = colourlst[rc1][rc2]
        else:
            parAlst[dc1][dc2] = parAlst[rnc1][rnc2]
            parBlst[dc1][dc2] = parBlst[rnc1][rnc2]
            colourlst[dc1][dc2] = colourlst[rnc1][rnc2]

        ## save old values (for reporting only)
        y1=parAlst[dc1][dc2]
        y2=parBlst[dc1][dc2]
        y3=colourlst[dc1][dc2]

        #Mutation occurs each round.
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
 
