def findnei2(m,n,ntype,nsize,w):
        D1=range(m-nsize,m+1+nsize)
        D2=range(n-nsize,n+1+nsize)
        if ntype=='mor':
               u1=numpy.random.randint(m-nsize,m+1+nsize)
               u2=numpy.random.randint(n-nsize,n+1+nsize)
        if ntype=='neu':
               u1=numpy.random.randint(m-nsize,m+1+nsize)
               v=len(D1)/2
               i=D1.index(u1)
               d=abs(i-v)
               j=numpy.random.randint(d,len(D1)-d)
               u2=D2[j]
        return([u1,u2]) 
