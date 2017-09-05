import numpy as np

def apply_transition_matrix(config,transition):
    n=len(config)
    new={}
    for k in range(n):
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
    for i in range(n):
        for j in range(n):        
            pair=config[i]+config[j]
            change=transition[pair]
            if change[0] is not None:
                tmp  = config[:i]+change[0][0]+config[i:][1:]
                word = tmp[:j]+change[0][1]+tmp[j:][1:]
                if word not in new:
                    new[word]=0
                new[word]+=change[1] # adds new contribution
    return new

def update(configs,transition):
    new={}
    for config in configs



if __name__ == '__main__':
    #
    # parameter definition
    #
    N = 4
    gamma = 0.3/N
    alpha = 1.0/(N*N)
    gamma_bar = 1.0/(N*N)
    transition={ '0':('1',gamma_bar),'1':('0',gamma),
                 '00':(None,0),'11':(None,0),
                 '10':('11',alpha),'01':(None,0) }
    
    
    
