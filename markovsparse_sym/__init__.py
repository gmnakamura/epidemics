import numpy as np
#==================================================
def markov(current,params=None,steps=None):
    N=len(list(current.keys())[0])
    if params is None:
        params=(1.0/(N*N),0.3/N,0.1/(N*N),1.0)
        #
        # params = (alpha,gamma,gamma_bar,prob_rand_network)
        #
    if steps is None:
        steps=20*N
    current={(entry.count('1')/2.0):current[entry] for entry in current}
    #current={N/2:1} # initial conf == everyone infected
    transmat=get_transition_matrix(params,N)
    p,basis=likelihood(current,N) # sum(p) == 1 !
    avg=np.zeros(steps)
    for k in range(steps):
        current=update(current,transmat);
        n,_=average(current,N,basis)
        avg[k]=np.sum(n)*1.0/N
    p,_=likelihood(current,N,basis)    
    return (avg,p)
#==================================================
def update(configs,transmat):
    final={}
    for config in configs:
        val=configs[config]
        new_configs=transmat[config]
        for new_config in new_configs:
            if new_config not in final:
                final[new_config]=0
            final[new_config]+=new_configs[new_config]*val
    return final
#==================================================
def get_transition_matrix(params,N):
    s=N/2.0
    transmat={}
    for m in np.arange(-s,s+1):
        transmat[m]=apply_transition_matrix(m,params,N)        
    return transmat
#==================================================
def apply_transition_matrix(m,params,N):
    #
    # we only consider sector N/2
    #
    s=N/2.0 
    out_configs={}
    out_configs[m]=1.0-params[0]*params[3]*(0.25*N*N-m*m)-(params[1]-params[2])*(m+0.5*N)-params[2]*N
    if m > -s:
        out_configs[m-1]=np.sqrt(s*(s+1)-m*(m-1))*params[1]
    if m < s:
        out_configs[m+1]=np.sqrt(s*(s+1)-m*(m+1))*(params[0]*params[3]*(N*0.5+m)+params[2])
    #
    # params = (alpha,gamma,gamma_bar)
    #                 
    return out_configs
#==================================================        
def compute_basis(N):
    #
    # we only consider sector N/2
    #
    def ladder_up(string,N):
        out={}
        for k in range(N):
            if string[k]=='0':
                new = string[:k]+'1'+string[k:][1:]
                out[new]=1
        return out
    s=0.5*N    
    out={}
    current={'0'*N:np.float64(1.0)}    
    out[-s]=current
    for m in (np.arange(N)-0.5*N):
        tmp={}
        for config in current:
            new = ladder_up(config,N)
            for entry in new:
                if entry not in tmp:
                    tmp[entry]=0
                tmp[entry]+=np.float64(current[config])
        r=np.float64(1.0)/np.sqrt(s*(s+1)-m*(m+1))
        current={s:tmp[s]*r for s in tmp}
        out[m+1]=current
    return out            
#==================================================        
def average(current,N,basis=None):
    if basis is None:
        basis=compute_basis(N)
    return (np.array([  current[m]*(m+0.5*N)*np.sum(list(basis[m].values()))  for m in current ]),basis)
#==================================================        
def likelihood(current,N,basis=None):
    if basis is None:
        basis=compute_basis(N)
    return ({config:basis[m][config]*current[m]  for m in current  for config in basis[m]},basis)
#==================================================        



if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from timeit import default_timer as timer
    #
    # parameter definition
    #
    N = 12


    current={'1'*N:1}
           

    start   = timer()
    avg,p   = markov(current)
    elapsed = timer() - start
    print('elapsed time :: %f' % elapsed)
    plt.plot(avg) ; plt.show()

    
    # kmax= N*20
    # for k in range(kmax):
    # #     print(average(current)*1.0/N)
    #     current=update(current,params,N); 
    #     p,_=likelihood(current,N,basis)
    #     #ptot=sum(list(p.values()))
    #     n,_ =average(current,N,basis)
    #     avg =np.sum(n)*1.0/N
    #     #print("probtot=%f , average=%f" %(ptot,avg))
        


