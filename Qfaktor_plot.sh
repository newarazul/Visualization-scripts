set view map
#set term png
#set terminal postscript landscape enhanced color "Helvetica" 20
set terminal postscript eps enhanced color
set palette defined ( 0 '#000090',\
    1 '#000fff',\
    2 '#0090ff',\
    3 '#0fffee',\
    4 '#90ff70',\
    5 '#ffee00',\
    6 '#ff7000',\
    7 '#ee0000',\
    8 '#7f0000')
#set palette color


#set xrange[0:180]
#set yrange[0:180]
#set title "Orientation of OH groups at the interface of a Pore"
set xlabel "Q4"
#set xlabel "OH1 [degrees]"
#set xtics 0,60,180 nomirror
#set ytics 0,60,180 nomirror
#set samples 101
#set isosamples 2
#set cbrange [800:1400]
#unset colorbox
#set datafile separator "\t"
unset cbtics
set xrange [1:-0.2]
set yrange [0:4.9]
set ylabel "Radius [A]"
set key off
set output "cfa.eps"
unset border
set title "Water structure at the hydrophilic surface"
#set pm3d map interpolate 20,20
#set view map
#set dgrid3d
#set pm3d map
#set pm3d interpolate 100,100
splot "CFa.out" using 2:1:3 with image 
#palette pt 5
