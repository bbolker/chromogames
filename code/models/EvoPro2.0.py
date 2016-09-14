#Evolution of group-focused altruism
#Robert White - 001309486
#Dr. Ben Bolker

import random,sys,time,math
from random import randint
import numpy

def 
#plant a seed. 
numpy.random.seed(25)

#Let check=True if you want to print the results for every round. Set roundnum to the number of rounds you want to happen. 
CHECK = False
roundnum = 15000

#The list Fitlst is made into a 100x100 grid.
Fitlst = numpy.zeros((100,100))
     
#The three parameters a,b and colour are given to each cell in the 100x100 lattice.
parAlst = numpy.random.uniform(-4.0,4.0,size=(100,100))

parBlst = numpy.random.uniform(-4.0,4.0,size=(100,100))

colourlst = numpy.random.uniform(0.0,5.0,size=(100,100))

#This is the logistics function. It will be used to calculate a cell's probability of cooperating.
    
def logistic(x):
    return float(1/(1+math.exp(-x)))


x = 1
#The game loop is started.

counter=0
while x <= roundnum:             
    #A cell on the lattice is chosen at random. 
    rc1 = numpy.random.randint(0,99)                         
    rc2 = numpy.random.randint(0,99)
    #These following statements find a neighbour cell.

    if rc1==0 and rc2==0:
        s = numpy.random.randint(0,2)
        if s==0:
            rnc1=1
            rnc2=0
        if s==1:
            rnc1=1
            rnc2=1
        if s==2:
            rnc1=0
            rnc2=1
    elif rc1==0 and rc2==99:
        s1=numpy.random.randint(0,2)
        if s1==0:
            rnc1=0
            rnc2=98
        if s1==1:
            rnc1=1
            rnc2=98
        if s1==2:
            rnc1=1
            rnc2=99
    elif rc1==99 and rc2 ==0:
        s2=numpy.random.randint(0,2)
        if s2==0:
            rnc1=98
            rnc2=0
        if s2==1:
            rnc1=98
            rnc2=1
        if s2==2:
            rnc1=99
            rnc2=1
    elif rc1==99 and rc2 ==99:
        s3=numpy.random.randint(0,2)
        if s3==0:
            rnc1=98
            rnc2=99
        if s3==1:
            rnc1=98
            rnc2=98
        if s3==2:
            rnc1=99
            rnc2=98
    elif rc1==0 and (rc2!=0 or rc2!=99):
        q=numpy.random.randint(0,4)
        if q==0:
            rnc1=rc1
            rnc2=rc2 - 1
        if q==1:    
            rnc1= rc1 + 1
            rnc2= rc2 - 1
        if q==2:
            rnc1= rc1 + 1
            rnc2= rc2
        if q==3:
            rnc1= rc1 + 1
            rnc2= rc2 + 1
        if q==4:
            rnc1= rc1 
            rnc2= rc2 + 1
    elif rc1==99 and (rc2!=0 or rc2!=99):
        q1=numpy.random.randint(0,4)
        if q1==0:
            rnc1=rc1
            rnc2=rc2 - 1
        if q1==1:    
            rnc1= rc1 - 1
            rnc2= rc2 - 1
        if q1==2:
            rnc1= rc1 - 1
            rnc2= rc2
        if q1==3:
            rnc1= rc1 - 1
            rnc2= rc2 + 1
        if q1==4:
            rnc1= rc1 
            rnc2= rc2 + 1
    elif rc2==99 and (rc1!=0 or rc1!=99):
        q2=numpy.random.randint(0,4)
        if q2==0:
            rnc1=rc1 + 1
            rnc2=rc2 
        if q2==1:    
            rnc1= rc1 + 1
            rnc2= rc2 - 1
        if q2==2:
            rnc1= rc1 
            rnc2= rc2 - 1
        if q2==3:
            rnc1= rc1 - 1
            rnc2= rc2 - 1
        if q2==4:
            rnc1= rc1 - 1
            rnc2= rc2
    elif rc2==0 and (rc1!=0 or rc1!=99):
        q3=numpy.random.randint(0,4)
        if q3==0:
            rnc1=rc1 + 1
            rnc2=rc2 
        if q3==1:    
            rnc1= rc1 + 1
            rnc2= rc2 + 1
        if q3==2:
            rnc1= rc1 
            rnc2= rc2 + 1
        if q3==3:
            rnc1= rc1 - 1
            rnc2= rc2 + 1
        if q3==4:
            rnc1= rc1 - 1
            rnc2= rc2
    else:
        q4 = numpy.random.randint(0,7)
        if q4==0:
            rnc1=rc1 + 1
            rnc2=rc2 + 1
        if q4==1:    
            rnc1= rc1 
            rnc2= rc2 + 1
        if q4==2:
            rnc1= rc1 - 1
            rnc2= rc2 + 1
        if q4==3:
            rnc1= rc1 + 1
            rnc2= rc2 
        if q4==4:
            rnc1= rc1 - 1
            rnc2= rc2
        if q4==5:
            rnc1= rc1 - 1
            rnc2= rc2 - 1
        if q4==6:
            rnc1= rc1 
            rnc2= rc2 - 1
        if q4==7:
            rnc1= rc1 + 1
            rnc2= rc2 - 1
    
    if CHECK:
        print('************************ROUND ',x,'************************************')
        print("The cell choosen at random was","(",rc1,rc2,")")
        print("The neighbour cell was","(",rnc1,rnc2,")")
        print("The probability that the choosen cell was going to cooperate was" , logistic(parAlst[rc1][rc2]+parBlst[rc1][rc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])))
        print("The probability that the neighbour cell was going to cooperate was" , logistic(parAlst[rnc1][rnc2]+parBlst[rnc1][rnc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])))      
        print("The fitness of the choosen cell was:", Fitlst[rc1][rc2])
        print("The fitness of the neighbour was:", Fitlst[rnc1][rnc2])
        print("Standby for results...")
    
    ben=2
    cost=1
    
    #The neighbour and choosen cell are asked if they want to cooperate with each other. 
    
    det = float(numpy.random.uniform(0,1.0))
    if CHECK:
        print('!!!!!!!!!',det)
    
        
    if det < logistic(parAlst[rnc1][rnc2]+parBlst[rnc1][rnc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])) and det < logistic(parAlst[rc1][rc2]+parBlst[rc1][rc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])):
        Fitlst[rnc1][rnc2] = Fitlst[rnc1][rnc2] + (ben - cost)
        Fitlst[rc1][rc2] = Fitlst[rc1][rc2] + (ben - cost)
        counter+=2
        if CHECK:
            print("The neighbour cell and the choosen cell cooperated!")
            
        
    elif det < logistic(parAlst[rnc1][rnc2]+parBlst[rnc1][rnc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])) and det > logistic(parAlst[rc1][rc2]+parBlst[rc1][rc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])):
        Fitlst[rnc1][rnc2] = Fitlst[rnc1][rnc2] - cost
        Fitlst[rc1][rc2] = Fitlst[rc1][rc2] + ben
        counter+=1
        if CHECK:
            print("The neighbour cell cooperated and the choosen cell did not cooperate!")
            
       
    elif det > logistic(parAlst[rnc1][rnc2]+parBlst[rnc1][rnc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])) and det < logistic(parAlst[rc1][rc2]+parBlst[rc1][rc2]*abs(colourlst[rnc1][rnc2]-colourlst[rc1][rc2])):
        Fitlst[rnc1][rnc2] = Fitlst[rnc1][rnc2] + ben
        Fitlst[rc1][rc2] = Fitlst[rc1][rc2] - cost
        counter+=1
        if CHECK:
            print("The neighbour cell did not cooperate and the choosen cell did cooperate!")
            
    else:
        Fitlst[rnc1][rnc2] = Fitlst[rnc1][rnc2] 
        Fitlst[rc1][rc2] = Fitlst[rc1][rc2]
        if CHECK:
            print("The neighbour and choosen cell did not cooperate!")
    if CHECK:
        print("The new fitness of the choosen cell after the round was:", Fitlst[rc1][rc2])
        print("The new fitness of the neighbour cell after the round was: ", Fitlst[rnc1][rnc2])
    

    #Randomly selects a cell to die. A death is simulated by removing all of the information from the cell and making it zero.
    
    dc1 = numpy.random.randint(0,99)                             
    dc2 = numpy.random.randint(0,99)
    Fitlst[dc1][dc2] = 0              
    parAlst[dc1][dc2] = 0
    parBlst[dc1][dc2] = 0
    if CHECK:
        print("The cell that died this round was","(",dc1,dc2,")","It had fitness,A,B and colour:",Fitlst[dc1][dc2],parAlst[dc1][dc2],parBlst[dc1][dc2],colourlst[dc1][dc2])
    
    #The dead cell is replaced by one of the two cells who had just competed. 

    det2 = numpy.random.uniform(0.0,1.0)
    FIT = (Fitlst[rc1][rc2]/(Fitlst[rnc1][rnc2] + Fitlst[rc1][rc2])) 
    if det2 < FIT:          
        parAlst[dc1][dc2] = parAlst[rc1][rc2]
        parBlst[dc1][dc2] = parBlst[rc1][rc2]
        colourlst[dc1][dc2] = colourlst[rc1][rc2]
    else:
        parAlst[dc1][dc2] = parAlst[rnc1][rnc2]
        parBlst[dc1][dc2] = parBlst[rnc1][rnc2]
        colourlst[dc1][dc2] = colourlst[rnc1][rnc2]
            
    #Mutation occurs each round.
    mut = numpy.random.lognormal(0,0.01,3) 

    y1=parAlst[dc1][dc2]
    y2=parBlst[dc1][dc2]
    y3=colourlst[dc1][dc2]
    parAlst[dc1][dc2] *= mut[0] 
    parBlst[dc1][dc2] *= mut[1] 
    colourlst[dc1][dc2] *= mut[2]
    
    if CHECK:    
        print("The cell's old fitness and constants were: 0:", y1, y2,y3)               
        print("The cell's new fitness and constants are:",Fitlst[dc1][dc2],parAlst[dc1][dc2],parBlst[dc1][dc2],colourlst[dc1][dc2])  
        print('--------------------------------------------------------------------------------------------')
    
    if x%1000==0:
        print('**************************ROUND ',x,' STATS***************************')
        mnA= numpy.mean(parAlst)
        mnB= numpy.mean(parBlst)
        mnCol= numpy.mean(colourlst)
        mnFt= numpy.mean(Fitlst) 
        stddevA= numpy.std(parAlst)
        stddevB= numpy.std(parBlst)
        stddevCol= numpy.std(colourlst)
        stddevFt= numpy.std(Fitlst)
        print('The mean of A is:',mnA,'The standard deviation of A is:',stddevA)
        print('The mean of B is:',mnB,'The standard deviation of B is:',stddevB)
        print('The mean of colour is:',mnCol,'The standard deviation of colour:',stddevCol)
        print('The mean of Fitness is:',mnFt,'The standard deviation of fitness:',stddevFt)
        print('The total amount of cooperations that occurred so far is:',counter) 
        print('***********************************************************************')
    x+=1



