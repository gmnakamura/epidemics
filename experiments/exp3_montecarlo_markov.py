import sys
sys.path.append("..")
import numpy as np
import montecarlo
import montecarlo_sym
import markov
import markov_sym


N=16
steps=20*N

print(u"""
===============================================================
experiment 3:: density of MC,MC-sym,Markov,Markov-sym
""")

avg={}
std={}
prob={}

print('... mc:')
avg['mc'],std['mc']=montecarlo.montecarlo('1'*N,steps=steps,num_averages=10000)
print('... mc-sym:')
avg['mc-sym'],std['mc-sym']=montecarlo_sym.montecarlo('1'*N,steps=steps,num_averages=10000)
print('... markov:')
avg['markov'],prob['markov']=markov.markov({'1'*N:1},steps=steps)
print('... markov-sym:')
avg['markov-sym'],prob['markov-sym']=markov_sym.markov({'1'*N:1},steps=steps)

with open('output_exp3_montecarlo.dat','w') as f:
    for k in range(steps):
        f.write('%d %f %f %f %f\n' % (k,avg['mc'][k],std['mc'][k],avg['mc-sym'][k],std['mc-sym'][k]))

with open('output_exp3_markov.dat','w') as g:
    for k in range(steps):
        g.write('%d %f %f\n' % (k,avg['markov'][k],avg['markov-sym'][k]))
