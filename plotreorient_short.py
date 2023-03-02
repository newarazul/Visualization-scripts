import matplotlib.pyplot as plt
import csv
import pandas as pd
from matplotlib.pyplot import *
from matplotlib.ticker import *


#data=pd.read_csv("L1.dat",sep=" ",header=None)
#data=pd.DataFrame(data)
#x=data[0]
#y=data[1]

#data=pd.read_csv("L2.dat",sep=" ",header=None)
#data=pd.DataFrame(data)
#z=data[1]

#data=pd.read_csv("L3.dat",sep=" ",header=None)
#data=pd.DataFrame(data)
#f=data[1]

#x,y,y2,y3=[],[],[],[]
#x2, x3 = [], []
y4, y5, y6=[], [], []
x4, x5, x6=[], [], []


#for line in open("L1.dat", "r"):
#    values=[float(s) for s in line.split()]
#    x.append(values[0])
#    y.append(values[1])


#for line in open("L2.dat", "r"):
#    values=[float(s) for s in line.split()]
#    y2.append(values[1])
#    x2.append(values[0])

#for line in open("L3.dat", "r"):
#    values=[float(s) for s in line.split()]
#    print(values[1])
#    y3.append(values[1])
#    x3.append(values[0])


for line in open("raw1.dat", "r"):
    values=[float(s) for s in line.split()]
    x4.append(values[0])
    y4.append(values[1])


for line in open("raw2.dat", "r"):
    values=[float(s) for s in line.split()]
    y5.append(values[1])
    x5.append(values[0])

for line in open("raw3.dat", "r"):
    values=[float(s) for s in line.split()]
    print(values[1])
    y6.append(values[1])
    x6.append(values[0])













plt.rc("font", family="serif")
rcParams['mathtext.fontset'] = 'cm'
#rcParams['mathtext.it'] = 'Arial:italic'
#rcParams['mathtext.rm'] = 'Arial'
rcParams.update({'font.size': 22})
rcParams["figure.figsize"]= (9.5,7)
rcParams['xtick.major.width']=2
rcParams['ytick.major.width']=2
rcParams['xtick.minor.width']=2
rcParams['ytick.minor.width']=2
rc("axes", linewidth=2)

#plt.plot(x4,y4, color="lightgrey")
#plt.plot(x5,y5,color="lightgrey")
#plt.plot(x6,y6,color="lightgrey")
plt.plot(x4,y4, label="Layer 1", color="blue",linewidth=2)
plt.plot(x5,y5, label="Layer 2",color="red",linewidth=2)
plt.plot(x6,y6, label="Bulk",color="green",linewidth=2)
#plt.axhline(y=0.0,color="gray",linestyle="--")
axes=plt.gca()
axes.set_xlim(0,0.1)
axes.set_ylim(0.8,1.0)

plt.axhline(y=0.824,xmax=0.305,color="blue",linestyle="--")
plt.axhline(y=0.8392,xmax=0.285,color="red",linestyle="--")
plt.axhline(y=0.84470,xmax=0.2850,color="green",linestyle="--")

#plt.title("Layer SFG Response")
plt.legend(loc="upper right")
plt.ylabel(r"$P_{2}~(\tau)$")
plt.xlabel(r"$\tau~[ps]$")


#plt.show()

plt.savefig("reorient_short.png", format="png", bbox_inches="tight")


