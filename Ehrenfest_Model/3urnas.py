import random as rm
import matplotlib.pyplot as plt
import pandas as pd
import math as mt


np = 600
L_a = []
for i in range(1,np+1):
    L_a.append(i)

L_b = []
L_c = []
tlist = []
numa = []
numb = []
numc = []

numa2 = []
numb2 = []
numc2 = []
entropia = []
p = 0
p_c = 0
p_b = 0


for t in range(10*np):
    tlist.append(t)
    Nrandom = rm.randint(1, np)
    Prandom = rm.random()
    a = Nrandom in L_a
    b = Nrandom in L_b
    c = Nrandom in L_c
          
    if  a == True:        
        p = 1 - len(L_b)/(len(L_a) + len(L_b)/2)
        if Prandom <= p:
            L_a.remove(Nrandom)
            L_b.append(Nrandom)
  
        
    elif  c == True:        
        p = 1 - len(L_b)/(len(L_c) + len(L_b)/2)
        if Prandom <= p:
            L_c.remove(Nrandom)
            L_b.append(Nrandom)            
 
        
    elif b == True:
        p_a = (np - len(L_a))/(2*np)
        p_c = (np - len(L_c))/(2*np)
        if Prandom <= p_a:
            L_b.remove(Nrandom)
            L_a.append(Nrandom)
        elif Prandom >= p_a and Prandom <= p_c + p_a:
            L_b.remove(Nrandom)
            L_c.append(Nrandom)
                     
    if t>5000:
        numa2.append(len(L_a))
            
    numa.append(len(L_a))
    numb.append(len(L_b))
    numc.append(len(L_c))
    entropia.append(mt.log(mt.factorial(np)/(mt.factorial(len(L_a))*mt.factorial(len(L_b))*mt.factorial(len(L_c)))))
    
"""
plt.figure(num=0, dpi=120)
plt.plot(tlist,numa, tlist, numb, tlist,numc)
plt.xlabel("Número de pasos")
plt.ylabel("Partículas en cada contenedor")
plt.legend(['A','B','C'],loc="upper right")


plt.hist(numa2, bins = 19, edgecolor = 'black')
plt.xlabel("Partículas en el contenedor A")
plt.ylabel("Frecuencia")"""

plt.figure(num=0, dpi=120)
plt.plot(tlist,entropia)
plt.xlabel("Número de pasos")
plt.ylabel("Entropia/kb")



