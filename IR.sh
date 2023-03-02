set terminal postscript eps enhanced color size 4in,3in
set output 'IR.eps'


#set encoding iso_8859_1
set title 'Power Spectra Hydrophobic vs Hydrophilic' 
set xlabel 'Frequency {/Symbol w} (cm^{-1})'
set ylabel 'Intensity (arb. unit)'
#'D_{r} / D_{bulk}'

set key left
#set key top right
set key box lw 2
set key spacing 2
#set key reverse
#set key font "20"
#set key samplen 8
set termoption dashed 

set xzeroaxis
set ytics 0.5
set xrange [3000:4200] 
set xtics 400
#set yrange [0:1]
#unset ytics
set tics nomirror
#set linetype 1 lw 2 lc rgb "red"
#set linetype 2 lw 2 lc rgb "orange"
#set linetype 3 lw 2 lc rgb "yellow"
#set linetype 4 lw 2 lc rgb "blue"
set style line 1 lt 1 lw 2 
#set style line 2 lt 1 lw 3 lc rgb "green"
#set style line 3 lt 1 lw 3 lc rgb "blue"
#set style line 4 lt 1 lw 3 lc rgb "red"
#set style line 5 lt 1 lw 2 lc rgb "green"

#set linetype 4 lw 3 lc rgb "blue"
#set linetype 5 lw 3 lc rgb "green"

plot "18Apower.csv" with lines title "1.8 nm hydrophilic", "18ACFpower.csv" with lines title "1.8 nm hydrophobic", "8Apower.csv" with lines title "0.8 nm hydrophilic", "8ACFpower.csv" with lines title "0.8 nm hydrophobic"

#, "pore8_3.SFG" using 1:2 ls 4 with lines title "0.8 nm Low Pressure", "pore5.SFG" using 1:2 ls 5 with lines title "0.5 nm"
