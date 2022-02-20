"""DEMON ALGORITHM ENERGY: Gas ideal, calculo de Beta"""
import matplotlib.pyplot as plt
import numpy as np
import random as rm
from scipy.optimize import curve_fit



def flinear(x,m,b):
    return m*x +b



L = 1000
N = 200
E = 2*N
t = 400000
Ed = 0
Nd = 0
suma = 0


En = 0
Nl = []
El = []
Pl = []
Edlist = []

Et = 0

for i in range (L):
    Nl.append(0)
    El.append(0)
    Pl.append(0)


#Dar energia y momentum a cada partícula
suma = 1
while suma < N:
    j = rm.randint(0,L-1)
    if Nl[j] == 0:
        Nl[j] = 1
        El[j] = 2
        Pl[j] = np.sqrt(El[j])
        Et += El[j]
        suma = suma + 1


print(suma)


#Calculo del cambio de energia del demonio
for i in range (t):
    u = rm.randint(0, L-1)
    if Nl[u] == 1:
        dP = (2*np.random.rand()-1)*2
        Pt = Pl[u] + dP       
        dE = pow(Pt,2) - El[u]
        if dE < 0:
            Pl[u] = Pt
            El[u] = pow(Pt,2)
            Ed = Ed - dE            
            Edlist.append(Ed)
    
        elif dE > 0:
            if Ed > dE:
                Ed = Ed - dE
                El[u] = El[u] + dE
                Pl[u] = Pt
                Edlist.append(Ed)
            else:
                Edlist.append(Ed)




plt.title("Distribución")
plt.xlabel("Energias")
plt.ylabel("Conteo")
ns, bins, patches = plt.hist(Edlist, bins =30)

#Hacemos el ajuste al logaritmo de los datos
energies = (bins[:-1]+bins[1:])/2.0
xvals = np.array(energies)
yvals = np.log(np.array(ns))
sig = 1.0/np.sqrt(np.array(ns))

m0 = (yvals[-1]-yvals[0])/(xvals[-1]-xvals[0])
b0 = yvals[0]-  m0*xvals[0]

popt, pcov = curve_fit(flinear, xvals, yvals, p0 =(m0,b0), sigma =sig)

m =popt[0]
dm=np.sqrt(pcov[0,0])
b=popt[1]
db =np.sqrt(pcov[1,1])

#El parámetro beta es la pendiente
print("Pendiente", m , "+/-", np.sqrt(pcov[0,0]))



