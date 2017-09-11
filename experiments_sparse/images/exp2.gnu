#!/usr/bin/gnuplot

set terminal epslatex standalone color 12
set output 'exp2.tex'

set style fill  transparent solid 0.65 noborder

f1='../output_exp2_montecarlo.dat'



set key Left


set multiplot

set xlabel '$N$'
set ylabel '$\tau$  (s)'


#set logscale y


plot f1  u 1:($2-$3):($2+$3) w filledcurves lc 'gray' notitle , '' u 1:($4-$5):($4+$5) w filledcurves lc 'gray' notitle , '' u 1:2 with linespoints lc 1  pt 5 title 'MC','' u 1:4 with linespoints pt 7 lc 2 title 'MC-sym' 


set origin 0.1,0.4
set size 0.5,0.5


unset xlabel
unset ylabel
set logscale y
set xtics (10,20)


plot f1  u 1:($2-$3):($2+$3) w filledcurves lc 'gray' notitle , '' u 1:($4-$5):($4+$5) w filledcurves lc 'gray' notitle , '' u 1:2 with linespoints lc 1  pt 5 notitle,'' u 1:4 with linespoints pt 7 lc 2 notitle 

