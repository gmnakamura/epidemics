set terminal epslatex standalone color 12
set output "exp4.tex"


f1='../output_exp4_markov.dat'
set pm3d map
set contour
set xlabel '$N \gamma$'
set ylabel '$p$'
set cblabel '$P_{0}$'
#set cbtics (0,0.5,1.0)
set lmargin at screen 0.12
set rmargin at screen 0.83

splot f1 using 1:2:3 notitle

