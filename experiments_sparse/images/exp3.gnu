#!/usr/bin/gnuplot

set terminal epslatex standalone color 12
set output 'exp3.tex'

set style fill  transparent solid 1 #noborder

f1='../output_exp3_markov.dat'
f2='../output_exp3_montecarlo.dat'

N=16



set key Left


set xlabel '$t/N$'
set ylabel '$n(t)/N$'

set ytics (0.5,0.6,0.7,0.8,0.9,1.0)

#plot f2 u ($1/N):($2-$3/N):($2+$3/N) with filledcurves lc 'gray'  notitle, f1 u (($1+1)/N):2 with lines lc 1 title 'Markov    ', f1 u (($1+1)/N):3 with linespoints lc 2 pt 7 pi 10 title 'Markov-sym', f2 u ($1/N):2 w lines lc 0 title 'MC    ', f2 u ($1/N):4 w linespoints lc 7 pt 4 pi 10 title 'MC-sym'

plot f2 u ($1/N):($2-$3/N):($2+$3/N) with filledcurves lc 'gray'  notitle, f1 u (($1+1)/N):2 with lines lc 1 lw 3 title 'Markov    ', f1 u (($1+1)/N):3 with linespoints lc 2 pt 7 pi 25 ps 1.5 lw 3 title 'Markov-sym', f2 u ($1/N):2 w linespoints lc 0 pt 2 ps 1.5 pi 20 lw 3  title 'MC    ', f2 u ($1/N):4 w linespoints lc 7 pt 4 ps 1.5 pi 20 title 'MC-sym'
