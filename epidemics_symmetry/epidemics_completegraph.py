import numpy as np
import time
import matplotlib.pyplot as plt

def update(m,s,N,alpha,gamma):
    p_up  =alpha*(m+N*0.5)*np.sqrt(s*(s+1)-m*(m+1))
    p_down=gamma*np.sqrt(s*(s+1)-m*(m-1))
    p_stay=1-alpha*(N*N*0.25-m*m)-gamma*(N*0.5+m)
    Z=p_up+p_down+p_stay
    intervals=np.array([p_down,p_stay+p_down, Z ])/Z
    trial = np.argmax(np.random.rand() < intervals)
    return int(trial-1)+m
    
if __name__== '__main__':    
    t0=time.time()
    N = 100
    alpha=0.5/(N*N)
    gamma=1.0/N
    num_averages=10

    S = N/2.0
    kmax=N*10
    mag=np.zeros(kmax)
    
    run=0
    while run < num_averages:
        run+=1
        k=0
        #
        # initial configuration
        #
        current = N/2.0 
        while k < kmax:
            mag[k]+=(current*1.0/N)+0.5
            current=update(current,S,N,alpha,gamma)
            k+=1
    mag=mag*1.0/num_averages
    
    print('elapsed time:: %f' %(time.time()-t0))

    plt.plot(mag); plt.show()
 
    with open('data_angular.dat','w') as f:
        for x in mag:
            f.write('%f \n' % x)    
    
