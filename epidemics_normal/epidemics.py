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
        val+= change[1]
        if trial < val: 
            new[k]=change[0]
            return ''.join(new)
    for i in range(n):
        for j in range(n):
            change=transition[current[i]+current[j]]
            val+= change[1]
            if trial < val:                 
                new[i]=change[0][0]
                new[j]=change[0][1]
                return ''.join(new)
    return current
            
def count(current):
    return np.sum([int(current[k]) for k in range(len(current)) ])



if __name__== '__main__':
    num_averages=100

    t0=time.time()
    N=20
    #
    #it is convenient to hold alpha fixed and change gamma as desired
    #
    alpha=1.0/(N*N) #alpha maximo < 4/n*n para gamma=0
    gamma=0.3/N       #gamma maximo < 2/n   para alpha=0
    gamma_bar=1.0/(N*N)
    transition={'0':('1',gamma_bar),'1':('0',gamma),
                '00':('00',0),'01':('01',0),
                '10':('11',alpha),'11':('11',0)}

    # OBS: for alpha=0, gamma=1/n and 
    #      initial conf = everyone infected,
    #      we obtain an exponential decay with exponent gamma
    #
    #      for gamma=0 and alpha = 1/n^2, then 
    #      1/mag-1 = exp(-alpha*n*t)
    #      using any initial config with n/2 infected


    kmax=N*20
    mag=np.zeros(kmax)
    std=np.zeros(kmax)    
    run=0
    while run < num_averages:
        #t0=time.time()
        run+=1
        k=0
        #
        # initial config
        #
        current='1'*int(N) 
        while k < kmax:
            mag[k]+= count(current)*1.0/N
            std[k]+=(count(current)*1.0/N)**2
            current=update(current,transition,alpha,gamma)        
            k+=1
            #print(current)

    y=time.time()-t0

    mag=mag*1.0/num_averages
    std=np.sqrt((std*1.0/num_averages) - mag*mag)


    with open('data_regular_N%d_gamma%f_runs%d.dat' % (N,gamma*N,num_averages),'w') as f:
        for x,y,z in zip(np.arange(kmax),mag,std):
            f.write('%d %f %f\n' % (x,y,z))

    import matplotlib.pyplot as plt
    t_per_N=np.arange(kmax)*1.0/N
    plt.rc('text', usetex=True)
    plt.plot(t_per_N,mag)
    plt.xlabel('$t/N$')
    plt.ylabel('$n(t)/N$')
    plt.fill_between(t_per_N, mag-std, mag+std, facecolor='gray',alpha=0.5, interpolate=True)
    plt.show()

