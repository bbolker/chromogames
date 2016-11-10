## A function that creates an array of all 'neu' or 'mor' neighbours of a focal for an arbitrary nsize. 

def findnei(m=10,n=10,ntype='neu',nsize=1,w=100): 
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
				
	print(neighbours) 
	return neighbours

findnei() 
