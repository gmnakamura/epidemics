import numpy as np
import time
import matplotlib.pyplot as plt

def update(current,transition,alpha,gamma):
    """
    Update the current configuration using
    the standard transition matrix.
    """
    # transition[conf]=(newconf,0 or 1)
    trial = np.random.rand()
    n=len(current)
    val=0
    new = [current[k] for k in range(n)]
    
    for k in range(n):
        change=transition[current[k]]
        val+= gamma*change[1]
        if trial < val: 

            if val> 1 : print(val)
            new[k]=change[0]
            return ''.join(new)
    for i in range(n):
        for j in range(n):
            change=transition[current[i]+current[j]]
            val+= alpha*change[1]
            if trial < val:                 

                if val> 1 : print(val)
                new[i]=change[0][0]
                new[j]=change[0][1]
                return ''.join(new)
    return current
            
def count(current):
    return np.sum([int(current[k]) for k in range(len(current)) ])



if __name__== '__main__':
    t0=time.time()
    n=100
    num_averages=10
    #
    #it is convenient to hold alpha fixed and change gamma as desired
    #
    alpha=1.0/(n*n) #alpha maximo < 4/n*n para gamma=0
    gamma=0.3/n       #gamma maximo < 2/n   para alpha=0
    transition={'0':('0',0),'1':('0',1),
                '00':('00',0),'01':('01',0),
                '10':('11',1),'11':('11',0)}

    # OBS: for alpha=0, gamma=1/n and initial conf = everyone infected,
    #      we obtain an exponential decay with exponent gamma
    #
    #      for gamma=0 and alpha = 1/n^2, then 1/mag-1 = exp(-alpha*n*t)
    #      using any initial config with n/2 infected


    kmax=n*10
    mag=np.zeros(kmax)

    run=0
    while run < num_averages:
        run+=1
        k=0
        #
        # initial config
        #
        #current='1'*int(n/2)+'0'*int(n/2)
        current='1'*int(n) 
        while k < kmax:
            mag[k]+=count(current)*1.0/n
            current=update(current,transition,alpha,gamma)        
            k+=1
            #print(current)
    mag=mag*1.0/num_averages

    print('elapsed time:: %f' %(time.time()-t0))

    plt.plot(mag);plt.show()
    
    
    with open('data_normal.dat','w') as f:
        for x in mag:
            f.write('%f \n' % x)
    


