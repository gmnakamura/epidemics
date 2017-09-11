set terminal epslatex standalone color 12
set output "exp5.tex"


f1='../output_exp5_markov.dat'
set pm3d map
set contour
set xlabel '$N \gamma$'
set ylabel '$p$'
set cblabel '$S_R$' offset 1,0
set lmargin at screen 0.12
set rmargin at screen 0.83

splot f1 using 1:2:(-log($3)) notitle

