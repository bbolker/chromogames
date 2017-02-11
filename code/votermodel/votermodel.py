
import random,sys,time,math
from random import randint
import numpy

def find_nei(m,n,ntype,nsize,w):
        D1=range(m-nsize,m+1+nsize)
        D2=range(n-nsize,n+1+nsize)
        neighbours=[]
        if ntype=='neu':
                for i in range(len(D1)):
                        v=len(D1)/2
                        d=abs(i-v)
                        for j in range(d,len(D1)-d):
                                I1=D1[i]%w
                                I2=D2[j]%w
                                neighbours.append([I1,I2])

        if ntype=='mor':
                for i in range(len(D1)):
                        for j in range(len(D2)):
                                I1=D1[i]%w
                                I2=D2[j]%w
                                neighbours.append([I1,I2])

        #print(neighbours) 
        return neighbours


def runvoter( roundnum=100000,w=4, n_rpt=10000, rng=[0,3], ):    
        results = numpy.zeros((roundnum+1,w,w))
        votelst = numpy.random.randint(rng[0],rng[1],size=(w,w)) 
		
	x = 0       
        #The game loop is started.
        while x <= roundnum:  
		dc1 = numpy.random.randint(0,w)
        	dc2 = numpy.random.randint(0,w) 
		neighbours = find_nei(dc1,dc2,'neu',1,w) 
			
		replace=randint(0,4)  
		while (replace==2): 
			replace=randint(0,4) 
		
		votelst[dc1][dc2] = votelst[neighbours[replace][0]][neighbours[replace][1]] 
		results[x]=votelst		
		x+=1 
	
	return results	 		
			
runvoter()   
 
