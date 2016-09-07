#Evolution of group-focused altruism
#Robert White - 001309486
#Dr. Ben Bolker

import random,sys,time,math
from random import randint
import numpy

def runsim(roundnum=10000,CHECK=False,
           a_range_init=(-4.0,4.0),
           colour_init=(0,5.0),
	   spatial='off',
	   R=3,
	   S=1,
	   T=4,
	   P=0,
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
        #Randomly selects a cell to die. A death is simulated by removing all of the information from the cell and making it zero.
        
        dc1 = numpy.random.randint(0,w-1)                             
        dc2 = numpy.random.randint(0,w-1)
	
	if spatial=='on':
		D1=range(dc1-nsize,dc1+1+nsize)
		D2=range(dc2-nsize,dc2+1+nsize) 
		EX=[]
		dCD=S-T
		dDC=T-S
	
		if ntype=='mor':
			for i in D1:
				for j in D2:
					t=logistic(parAlst[i%w][j%w]+parBlst[i%w][j%w]*abs(colourlst[i%w][j%w]-colourlst[dc1][dc2]))*(1-logistic(parAlst[dc1][dc2]+parBlst[dc1][dc2]*abs(colourlst[dc1][dc2]-colourlst[i%w][j%w])))*dCD
					t1=(1-logistic(parAlst[i%w][j%w]+parBlst[i%w][i%w]*abs(colourlst[i%w][j%w]-colourlst[dc1][dc2])))*logistic(parAlst[dc1][dc2]+parBlst[dc1][dc2]*abs(colourlst[dc1][dc2]-colourlst[i%w][j%w]))*dDC 	
					EX.append([i%w,j%w,t+t1])
				
	
		if ntype=='neu':
			for i in range(len(D1)):
				v=len(D1)/2
                        	d=abs(i-v) 
				for j in range(d,len(D1)-d):
					I1=D1[i]%w
					I2=D2[j]%w 
					t=logistic(parAlst[I1][I2]+parBlst[I1][I2]*abs(colourlst[I1][I2]-colourlst[dc1][dc2]))*(1-logistic(parAlst[dc1][dc2]+parBlst[dc1][dc2]*abs(colourlst[dc1][dc2]-colourlst[I1][I2])))*dCD
                                	t1=(1-logistic(parAlst[I1][I2]+parBlst[I1][I2]*abs(colourlst[I1][I2]-colourlst[dc1][dc2])))*logistic(parAlst[dc1][dc2]+parBlst[dc1][dc2]*abs(colourlst[dc1][dc2]-colourlst[I1][I2]))*dDC
                                	EX.append([I1,I2,t+t1]) 
	
		for i in EX:
			r=1/(1.0+math.exp(i[2]/0.1)) 
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
				
	elif spatial=='off':
		dc11=numpy.random.randint(0,w-1) 
		dc22=numpy.random.randint(0,w-1)
		while (dc11==dc1 and dc22==dc2): 
			dc11=numpy.random.randint(0,w-1)
                	dc22=numpy.random.randint(0,w-1)
		AA=parAlst[dc11][dc22] + numpy.random.normal(0,mut_sd[0]) 
		dCD=S-T
                dDC=T-S
        	t=logistic(AA)*(1-logistic(parAlst[dc11][dc22]))*dCD
                t1=(1-logistic(AA))*logistic(parAlst[dc11][dc22])*dDC
		W=t+t1
		r=1/(1.0+math.exp(W/0.001))
		prob=r
		det7=float(numpy.random.uniform(0,1.0))
		#print(r) 
		#print(parAlst[dc11][dc22]) 
		#print(AA)
		#print('*****')   		 
		if det7 > prob: 
			parAlst[dc11][dc22]=AA 
			parBlst[dc11][dc22]=parBlst[dc11][dc22]
			colourlst[dc11][dc22]=colourlst[dc11][dc22]
			Fitlst[dc11][dc22]=Fitlst[dc11][dc22] 
		else:
 			pass 
			
        if CHECK:
            print("The cell that died this round was","(",dc1,dc2,")","It had fitness,A,B and colour:",Fitlst[dc1][dc2],parAlst[dc1][dc2],parBlst[dc1][dc2],colourlst[dc1][dc2])
            

        ## save old values (for reporting only)
        y1=parAlst[dc1][dc2]
        y2=parBlst[dc1][dc2]
        y3=colourlst[dc1][dc2]

        #Mutation occurs each round.
	if spatial=='on':
		DET=float(numpy.random.uniform(0,1.0)) 
		if DET < 0.1:
        		if mut_type=="mult":
            	  		 parAlst[dci1][dc2] *= numpy.random.lognormal(0,mut_sd[0])
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
 
