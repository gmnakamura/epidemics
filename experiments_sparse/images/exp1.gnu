#!/usr/bin/gnuplot

set terminal epslatex standalone color 12
set output 'exp1.tex'

set style fill  transparent solid 0.65 noborder

f1='../output_exp1_markov.dat'



set key Left



set multiplot

set xlabel '$N$'
set ylabel '$\tau$ (s)'
set ytics (0,25,50,75,100,125,150)

plot f1  u 1:($2-$3):($2+$3) w filledcurves lc 'gray' notitle , '' u 1:($4-$5):($4+$5) w filledcurves lc 'gray' notitle , '' u 1:2 with linespoints lc 1  pt 4 ps 2  title 'Markov','' u 1:4 with linespoints pt 7 ps 2 lc 2 title 'Markov-sym' 


set origin 0.17,0.25
set size 0.6,0.6


unset xlabel
unset ylabel

set logscale y

set xtics (4,8,12,16)
set ytics (0.01,1,100)


plot f1  u 1:($2-$3):($2+$3) w filledcurves lc 'gray' notitle , '' u 1:($4-$5):($4+$5) w filledcurves lc 'gray' notitle , '' u 1:2 with linespoints lc 1  pt 4 ps 1.5 notitle,'' u 1:4 with linespoints pt 7 ps 1.5 lc 2 notitle 




