import matplotlib.pyplot as plt
import math as mt
import random as rm



numero_fotones = 200
longitud = 200
energia_total = 3*numero_fotones
iteraciones = 200000
numero_ocupacion = []
segundo_no = []
temperatura = 30

total_particulas = 0     


for i in range(longitud):
    numero_ocupacion.append(0)
    segundo_no.append(0)


#Damos energias discretas para la energia de los fotones
for j in range(longitud):
    numero_ocupacion[j] = rm.randint(0,10)
        

#Una vez establecidas las condiciones iniciales, dejamos que el sistema se organice
# a través del algoritmo Metropolis

for k in range(iteraciones):
    a = rm.randint(0, longitud-1)
    b = rm.randint(0,1)
    if b == 0:
        b = -1
    if b == 1: #Quiere decir que anadimos una particula
        delta_E = a+1
    if b == -1: #Quiere decir que quitamos una particula
        delta_E =-(a+1)
    #Escribimos el criterio de actualizacion
    c = mt.exp(delta_E/temperatura)
    if c >=1 and numero_ocupacion[a] != 0:
        numero_ocupacion[a] -=1
    
    if c <1:
        r = rm.random()
        if r < c:
            numero_ocupacion[a] +=1
    if k > 50000 and k%500 == 0:
        for i in range(longitud): 
            segundo_no[i] += numero_ocupacion[i]
        
 
for i in range(longitud):    
    segundo_no[i] = int(segundo_no[i]/299)
                
                
y = []          
x_l = []  
for i in range(60):
    x = i+1
    x_l.append(x)
    a = 1/(mt.exp(x/temperatura)-1)
    y.append(int(a))
  
ocupacion2 =[]
for g in range(60):
    ocupacion2.append(segundo_no[g])
    
plt.plot(x_l, ocupacion2, "o",  label = "Simulado")
plt.plot(x_l,y,  label = "Teórico")
plt.xlabel("Energía del estado")
plt.ylabel("Número de partículas")
plt.legend()


