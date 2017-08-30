import numpy as np
import time
#import matplotlib.pyplot as plt

def update(m,s,N,alpha,gamma):
    n=N*0.5+m
    up  =int(s*(s+1)-m*(m+1) > 0)
    down=int(s*(s+1)-m*(m-1) > 0)
    p_up=up*alpha*n*(N-n)
    p_down=down*gamma*n
    p_stay=1-alpha*(N-n)*n-gamma*n
    Z=p_up+p_down+p_stay
    intervals=np.array([p_down,p_stay+p_down, Z ])/Z
    trial = np.argmax(np.random.rand() < intervals)
    return int(trial-1)+m



    
if __name__== '__main__': 
    num_averages=100
    N_list=[10,20,40,80,160,320,640,1280,2560,5120]
    avgtime=np.zeros(len(N_list))
    stdtime=np.zeros(len(N_list))
    for i in range(len(N_list)):        
        t0=time.time()
        N=N_list[i]
        alpha=1/(N*N)
        gamma=0.3/N


        S = N/2.0
        kmax= N*20
        mag=np.zeros(kmax)    
        std=np.zeros(kmax)    
        run=0
        while run < num_averages:
            #t0=time.time()
            run+=1
            k=0
            #
            # initial configuration
            #
            current = N/2.0 
            while k < kmax:
                mag[k]+= current*1.0/N+0.5
                std[k]+=(current*1.0/N+0.5)**2.0
                current=update(current,S,N,alpha,gamma)
                k+=1
        y=time.time()-t0
        avgtime[i]+=y
        stdtime[i]+=y*y

        mag= mag*1.0/(num_averages)
        std=np.sqrt((std*1.0/num_averages) - mag*mag)
        avgtime=avgtime*1.0/num_averages
        stdtime=np.sqrt(stdtime*1.0/num_averages-avgtime*avgtime)
        # etime=time.time()-t0
        # print('elapsed time:: %f' %(etime))

        #plt.plot(mag); plt.show()
 
        with open('data_angular_N%d_gamma%f_runs%d.dat' % (N,gamma*N,num_averages),'w') as f:
            for x,y,z in zip(np.arange(kmax),mag,std):
                f.write('%d %f %f\n' % (x,y,z))

    with open('time_angular_gamma%f_runs%d.dat' % (gamma*N,num_averages),'w') as f:
        for x,y,z in zip(N_list,avgtime,stdtime):
            f.write('%f %f %f \n' % (x,y,z))    
    
