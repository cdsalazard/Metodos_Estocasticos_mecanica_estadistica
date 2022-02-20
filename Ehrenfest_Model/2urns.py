import random as rm
import matplotlib.pyplot as plt
import pandas as pd
import math as mt


np = 600
L_a = []
for i in range(1,np+1):
    L_a.append(i)

L_b = []
tlist = []
numa = []
numb = []
entropia = []

numa2 = []
p = 0


for t in range(5*np):
    tlist.append(t)
    Nrandom = rm.randint(1, np)
    Prandom = rm.random()
    a = Nrandom in L_a
    b = Nrandom in L_b
    if a == True and len(L_a) == np:
        L_a.remove(Nrandom)
        L_b.append(Nrandom)
        
    elif  a == True and len(L_a) != np:        
        p = len(L_a)/np
        if Prandom <= p:
            L_a.remove(Nrandom)
            L_b.append(Nrandom)
            
    elif b == True and len(L_b) == np:
        L_b.remove(Nrandom)
        L_a.append(Nrandom)
        
    elif b == True and len(L_b) != np:
        p = len(L_b)/np
        if Prandom <= p:
            L_b.remove(Nrandom)
            L_a.append(Nrandom)
            
    if t>5000:
        numa2.append(len(L_a))
        
    numa.append(len(L_a))
    numb.append(len(L_b))
    entropia.append(mt.log(mt.factorial(np)/(mt.factorial(len(L_a))*mt.factorial(len(L_b)))))
    
    
"""   
plt.figure(num=0, dpi=120)
plt.plot(tlist,numa, numb)
plt.xlabel("Número de pasos")
plt.ylabel("Partículas en cada contenedor")
plt.legend(['A','B'],loc="upper right")

plt.hist(numa2, bins = 20, edgecolor = 'black')
plt.xlabel("Partículas en el contenedor A")
plt.ylabel("Frecuencia")"""


plt.figure(num=0, dpi=120)
plt.plot(tlist,entropia)
plt.xlabel("Número de pasos")
plt.ylabel("Entropia/kb")

