import sys
sys.path.append("..")
from timeit import default_timer as timer
import numpy as np
import markov
import markov_sym

num_samples=30
nmin=4
nmax=8

print(u"""experiment 1:: performance evaluation of markov implementations

""")
print(u""" average calculated using %d samples
""" %num_samples)
print(u""" non-symmetric implementation""")
for N in range(nmin,nmax+1,2):
    print('   ... N=%d'%N)
    perf = np.zeros(num_samples)
    for sample in range(num_samples):
        start=timer()
        n,p  =markov.markov({'1'*N:1})
        end  =timer()
        perf[sample]=end-start
    avg=np.mean(perf)
    std=np.sqrt(np.var(perf))    
print(u"""... done. Elapsed time =%f +- %f
""" %(avg,1.96*std))
print(u"""     symmetric implementation""")
for N in range(nmin,nmax+1,2):
    print('   ... N=%d'%N)
    perf = np.zeros(num_samples)
    for sample in range(num_samples):
        start=timer()
        n,p  =markov_sym.markov({'1'*N:1})
        end  =timer()
        perf[sample]=end-start
    avg=np.mean(perf)
    std=np.sqrt(np.var(perf))    
print(u"""... done. Elapsed time =%f +- %f
""" %(avg,1.96*std))
