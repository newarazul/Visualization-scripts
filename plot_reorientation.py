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

x,y,y2,y3=[],[],[],[]
x2, x3 = [], []
y4, y5, y6=[], [], []
x4, x5, x6=[], [], []


for line in open("L1.dat", "r"):
    values=[float(s) for s in line.split()]
    x.append(values[0])
    y.append(values[1])


for line in open("L2.dat", "r"):
    values=[float(s) for s in line.split()]
    y2.append(values[1])
    x2.append(values[0])

for line in open("L3.dat", "r"):
    values=[float(s) for s in line.split()]
    print(values[1])
    y3.append(values[1])
    x3.append(values[0])


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







#plt.style.use('seaborn') # I personally prefer seaborn for the graph style, but you may choose whichever you want.
#params = {"ytick.color" : "black",
#          "xtick.color" : "black",
#          "axes.labelcolor" : "black",
#          "axes.edgecolor" : "black",
#          "text.usetex" : True,
#          "font.family" : "serif",
##          "font.serif" : ["Computer Modern Serif"]}
#plt.rcParams.update(params)





plt.rc("font", family="serif")
#rcParams['font.family'] = 'Computer Modern Roman'
rcParams['mathtext.fontset']= "cm"
#rcParams['mathtext.it'] = 'Arial:italic'
#rcParams['mathtext.rm'] = 'Arial'
rcParams.update({'font.size': 22})
rcParams["figure.figsize"]= (9.5,7)
rcParams['xtick.major.width']=2
rcParams['ytick.major.width']=2
rcParams['xtick.minor.width']=2
rcParams['ytick.minor.width']=2
rc("axes", linewidth=2)




plt.plot(x4,y4, color="lightgrey")
plt.plot(x5,y5,color="lightgrey")
plt.plot(x6,y6,color="lightgrey")
plt.plot(x,y, label="Layer 1", color="blue", linewidth=2)
plt.plot(x2,y2, label="Layer 2",color="red",linewidth=2)
plt.plot(x3,y3, label="Bulk",color="green",linewidth=2)
#plt.axhline(y=0.0,color="gray",linestyle="--")
axes=plt.gca()
#axes.set_xlim(2500,4000)


#plt.title("Layer SFG Response")
plt.legend(loc="upper right")
plt.ylabel(r'$P_{2}~(\tau)$', weight="bold")
plt.xlabel(r'$\tau~[ps]$', weight="bold")


#plt.show()

plt.savefig("reorientation2.png", format="png", bbox_inches="tight")


