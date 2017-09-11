import sys
sys.path.append("..")
import numpy as np
from timeit import default_timer as timer
import markovsparse_sym as markov_sym


print(u"""experiment 4:: P_0(t) for increasing gamma and p
""")
N=8

output=[]

f=open('output_exp4_markov.dat','w')
for p in np.arange(0.0,1.01,0.05):
    for gamma in np.arange(0.0,1.01,0.05):
        params =(1.0/(N*N),gamma/N,0.1/(N*N),p)
        ts     =timer()
        ns,prob=markov_sym.markov({'1'*N:1},params=params)
        ts     =timer()-ts        
        #print(u""" Elapsed time =%f""" %ts)
        #print(u""" N g=%f , p =%f :: P0=%f""" % (gamma,p,prob['0'*N]))
        #output.append( (gamma,p,prob['0'*N]))
        f.write('%f %f %f \n' % (gamma,p,prob['0'*N]))
    f.write('\n')
f.close()
        
# with open('output_exp4_markov.dat','w') as f:
#     for entry in output:
#         f.write('%f %f %f\n' % entry )

