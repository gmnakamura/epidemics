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
            new[k]=change[0]
            return ''.join(new)
    for i in range(n):
        for j in range(n):
            change=transition[current[i]+current[j]]
            val+= alpha*change[1]
            if trial < val:                 
                new[i]=change[0][0]
                new[j]=change[0][1]
                return ''.join(new)
    return current
            
def count(current):
    return np.sum([int(current[k]) for k in range(len(current)) ])



if __name__== '__main__':
    num_averages=100
    N_list=[10,20,40,80,160]#,320,640,1280,2560,5120]
    avgtime=np.zeros(len(N_list))
    stdtime=np.zeros(len(N_list))
    for i in range(len(N_list)): 
        t0=time.time()
        N=N_list[i]
        #
        #it is convenient to hold alpha fixed and change gamma as desired
        #
        alpha=1.0/(N*N) #alpha maximo < 4/n*n para gamma=0
        gamma=0.3/N       #gamma maximo < 2/n   para alpha=0
        transition={'0':('0',0),'1':('0',1),
                    '00':('00',0),'01':('01',0),
                    '10':('11',1),'11':('11',0)}

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
            #current='1'*int(n/2)+'0'*int(n/2)
            current='1'*int(N) 
            while k < kmax:
                mag[k]+= count(current)*1.0/N
                std[k]+=(count(current)*1.0/N)**2
                current=update(current,transition,alpha,gamma)        
                k+=1
                #print(current)

        y=time.time()-t0
        avgtime[i]+=y
        stdtime[i]+=y*y        

        mag=mag*1.0/num_averages
        std=np.sqrt((std*1.0/num_averages) - mag*mag)
        avgtime=avgtime*1.0/num_averages
        stdtime=np.sqrt(stdtime*1.0/num_averages - avgtime*avgtime)

        with open('data_regular_N%d_gamma%f_runs%d.dat' % (N,gamma*N,num_averages),'w') as f:
            for x,y,z in zip(np.arange(kmax),mag,std):
                f.write('%d %f %f\n' % (x,y,z))
    with open('time_regular_gamma%f_runs%d.dat' % (gamma*N,num_averages),'w') as f:
        for x,y,z in zip(N_list,avgtime,stdtime):
            f.write('%f %f %f \n' % (x,y,z))    


