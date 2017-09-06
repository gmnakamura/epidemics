import numpy as np




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



if __name__ == '__main__':
    #
    # parameter definition
    #
    N = 4
    gamma = 0.3/N
    alpha = 1.0/(N*N)
    gamma_bar = 0.1/(N*N)
    
    params=(alpha,gamma,gamma_bar)
    transition={ '0':('1',gamma_bar),'1':('0',gamma),
                 '00':(None,0),'11':(None,0),
                 '10':('11',alpha),'01':(None,0) }
    
    
    current={'1111':1}
    current=update(current,transition,params); print(sum(current.values()))
