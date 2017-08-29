import numpy as np


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
    transition={'0':('0',0),'1':('0',1),
                '00':('00',0),'01':('01',0),
                '10':('11',1),'11':('11',0)}


    current='100000000000000000000000000000000000000000000000'
    n=len(current)
    mag=[]
    k=0
    kmax=1000
    while k < kmax:
        mag.append(count(current)*1.0/n)
        current=update(current,transition,0.01/n,0.00)        
        k+=1

        #print(current)

    with open('data.dat','w') as f:
        for x in mag:
            f.write('%f \n' % x)
    


