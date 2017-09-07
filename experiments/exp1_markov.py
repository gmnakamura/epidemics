import sys
sys.path.append("..")
from timeit import default_timer as timer
import numpy as np
import markov
import markov_sym

num_samples=30
nmin=4
nmax=8
nlist=range(nmin,nmax+1,2)
ns=len(nlist)

print(u"""
===============================================================
experiment 1:: performance evaluation of markov implementations
""")
print(u""" average calculated using %d samples
""" %num_samples)
print(u"""non-symmetric implementation""")
avg={}
std={}
for N in nlist:
    print('N=%d'%N)
    perf = np.zeros(num_samples)
    for sample in range(num_samples):
        start=timer()
        n,p  =markov.markov({'1'*N:1})
        end  =timer()
        perf[sample]=end-start
    avg[N]=np.mean(perf)
    std[N]=np.sqrt(np.var(perf))    
    print(u"""... done. Elapsed time =%f +- %f""" %(avg[N],1.96*std[N]))
print(u"""symmetric implementation""")
avg1={}
std1={}
for N in nlist:
    print('N=%d'%N)
    perf = np.zeros(num_samples)
    for sample in range(num_samples):
        start=timer()
        n,p  =markov_sym.markov({'1'*N:1})
        end  =timer()
        perf[sample]=end-start
    avg1[N]=np.mean(perf)
    std1[N]=np.sqrt(np.var(perf))    
    print(u"""... done. Elapsed time =%f +- %f""" %(avg1[N],1.96*std1[N]))

with open('output_exp1_markov.dat','w') as f:
    for N in nlist:
        f.write('%d %f %f %f %f\n' % (N,avg[N],std[N],avg1[N],std1[N]))
