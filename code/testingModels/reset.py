## Testing if python has one of the same argument function featuress as R. 

def g(x=1,y=9):            ## Valid  
	print(x,y) 



def f(x, y):               ## Valid 
	print(x,y) 


#def h(x=1,y=x):            This is not allowed
#	print(x,y)          


#def h(x=1,y):             This is now allowed either.
#	print(x,y)         


def h(x,z=1) :            ## This is allowed
	print(x) 

def k(x,z=None):
	if (z==None):
		z=x
	print(x,z) 


f(1,1) 
g()
h()   
k(2,)   


