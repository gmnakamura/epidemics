import sys
sys.path.append("..")
from timeit import default_timer as timer
import markov
import markov_sym


print(u"""experiment 0:: comparison between both markov implementations

""")
print(u"""markov (non-symmetric) initial conf. =| 11111111 > """)
N=8
t0   =timer()
n0,p0=markov.markov({'1'*N:1})
t0   =timer()-t0
print(u"""... done. Elapsed time =%f""" %t0)
print(u"""markov (    symmetric) initial conf. =| 11111111 > """)
ts   =timer()
ns,ps=markov_sym.markov({'1'*N:1})
ts   =timer()-ts
print(u"""... done. Elapsed time =%f""" %ts)
print(u"""probs:  regular   |  symmetric""")
for entry in p0:
    print(entry,p0[entry],ps[entry])
print(u"""
n(regular  )/N = %f
n(symmetryc)/N = %f""" % (n0,ns))
