import numpy as np
from functools import reduce

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
    transition={ '0':('1',params[2]),'1':('0',params[1]),
                 '00':(None,0),'11':(None,0),
                 '10':('11',params[0]*params[3]),'01':(None,0) }
    avg=np.zeros(steps)
    for k in range(steps):
        current=update(current,transition,params);
        avg[k]= average(current)*1.0/N
    return ( avg , current)
#==================================================
def update(configs,transition,params):
    final={}
    for config in configs:
        val=configs[config]
        new_configs=apply_transition_matrix(config,transition,params)
        for new_config in new_configs:
            if new_config not in final:
                final[new_config]=0
            final[new_config]+=new_configs[new_config]*val
    return final
#==================================================
def apply_transition_matrix(config,transition,params):
    N=len(config)
    new={}
    for k in range(N):
        change=  transition[config[k]]
        #
        # create new config
        #
        word  = config[:k]+change[0]+config[k:][1:]
        #
        # check whether the word exists in new
        #
        if word not in new:
            new[word]=0
        new[word]+=change[1] # adds new contribution
    for i in range(N):
        for j in range(N):        
            pair=config[i]+config[j]
            change=transition[pair]
            if change[0] is not None:
                tmp  = config[:i]+change[0][0]+config[i:][1:]
                word = tmp[:j]+change[0][1]+tmp[j:][1:]
                if word not in new:
                    new[word]=0
                new[word]+=change[1] # adds new contribution
    num_infected = config.count('1')
    #
    # params = (alpha,gamma,gamma_bar)
    #
    new[config]= 1.0 - (N-num_infected)*(num_infected*params[0]+params[2])-num_infected*params[1]                 
    return new
#==================================================        
def map_str2int(string):
    n   = len(string)
    vec = [ int(string[k])*(2**k) for k in range(n) ]
    return reduce(lambda x,y: x+y, vec)        
#==================================================        
def average(configs):
    output=0
    for config in configs:
        output+= config.count('1') * configs[config]
    return output
#==================================================        



if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from timeit import default_timer as timer
    #
    # parameter definition
    #
    N = 12


    current={'1'*N:1} # initial conf == everyone infected
    
    start   = timer()
    avg,p   = markov(current)
    elapsed = timer() - start
    print('elapsed time :: %f' % elapsed)
    plt.plot(avg) ; plt.show()



    
    # gamma = 0.3/N
    # alpha = 1.0/(N*N)
    # gamma_bar = 0#0.1/(N*N)    
    # params=(alpha,gamma,gamma_bar)
    # transition={ '0':('1',gamma_bar),'1':('0',gamma),
    #              '00':(None,0),'11':(None,0),
    #              '10':('11',alpha),'01':(None,0) }        
    # current={'1'*N:1}    
    # kmax= N*20
    # for k in range(kmax):
    #     print(average(current)*1.0/N)
    #     current=update(current,transition,params); 


        


