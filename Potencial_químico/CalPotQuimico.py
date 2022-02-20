"""DEMON ALGORITHM MOVEMENT OF PARTICLES"""
import matplotlib.pyplot as plt
import math as mt
import numpy as np
import random as rm
from scipy.optimize import curve_fit 


def flinear(x,m,b):
    return m*x +b

L = 1000
N = 200
E = 2*N
t = 500000
Ed = 2
Nd = 0
suma = 0

En = 0
Nl = []
El = []
Pl = []
Ndlist = []
Edlist = []

Et = 0

for i in range (L):
    Nl.append(0)
    El.append(0)
    Pl.append(0)
    

#Dar energia y momentum a cada partícula
while Et < E :
    j = rm.randint(0,L-1)
    if Nl[j] == 0:
        Nl[j] = 1
        El[j] = rm.randint(0,5)
        Pl[j] =np.sqrt(El[j])
        Et += El[j]



for i in Nl:
    suma = suma + i
    
while suma < N: 
    i = rm.randint(0,L-1)
    if Nl[i] == 0:
        Nl[i] = 1
        suma += 1

print(suma)


#Demon algoritmo

for i in range (t):
    u = rm.randint(0, L-1)
    if Nl[u] == 1:
        dE = El[u]    
        if dE  <= Ed:
            Nl[u] = 0
            El[u] = 0 
            Pl[u] = 0
            Ed =+ dE
            Edlist.append(dE)
            Nd += 1
        Ndlist.append(Nd)
    elif Nl[u] ==0:
        if Ed ==0:
            dE = 0
            if dE <= Ed and Nd > 0:
                Nl[u] = 1
                Ed -= dE
                Nd -=1
        else:  #Edemonio esta definida diferente de cero
            dP = (2*np.random.rand()-1)*2
            Pt = dP       
            dE = pow(Pt,2)
            if dE <= Ed and Nd > 0:
                Nl[u] = 1
                Pl[u] = Pt
                El[u]= dE
                Ed -= dE
                Nd -=1
        Ndlist.append(Nd)
        
        
        

ceros = 0
unos = 0
dos = 0
tres = 0
cuatros = 0
cincos = 0
for a in Ndlist:
    if a == 0:
        ceros += 1
    elif a == 1:
        unos +=1
    elif a ==2:
        dos +=1
    elif a ==3:
        tres +=1
    elif a ==4:
        cuatros+=1
    elif a==5:
        cincos+=1

listaA = [ceros, unos, dos, tres, cuatros]
Xval = [0,1,2,3,4]
print(listaA)

listaB =[]


plt.title("Distribución")
plt.xlabel("Nd")
plt.ylabel("Conteo")
ns, bins, patches = plt.hist(Ndlist, bins =10, rwidth=0.85)




for i in listaA:
    a = mt.log(i)
    listaB.append(a)

res, cov = curve_fit(flinear, Xval, listaB)


print(listaB)
print("Beta*Nu ", 4*res[0])
plt.figure(num=0, dpi=120)
plt.plot(listaB, label = "Ideal") 
plt.xlabel("Nd con una densidad de p = 0.2")
plt.ylabel("log(n) ")

