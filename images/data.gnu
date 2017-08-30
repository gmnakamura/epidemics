set terminal epslatex standalone 12 color


set style fill  transparent solid 0.75 noborder


N=40
N2=5120
set output 'data_angular_gammafixed.tex'

set xlabel('$t / N$')
set ylabel('$n(t)/N$')
plot 'symmetry/data_angular_N40.000000_gamma0.300000_runs100.000000.dat' using ($1/N):($2-2*$3):($2+2*$3) with filledcurves lc rgb "dark-gray" notitle , '' using ($1/N):2 with points pt 7 ps 0.5 lc rgb "dark-violet" title  '$N=40$', \
      'symmetry/data_angular_N5120.000000_gamma0.300000_runs100.000000.dat' using ($1/N2):($2-2*$3):($2+2*$3) with filledcurves lc rgb "#009e73" notitle , '' using ($1/N2):2 with lines lt 1 lw 2 lc rgb "#009e73" title  '$N=5120$'

