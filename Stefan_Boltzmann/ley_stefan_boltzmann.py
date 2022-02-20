import matplotlib.pyplot as plt
import math as mt



def stefan (eta, T):
  u = (eta**3)*(T**4)/(mt.exp(eta)-1)
  return u

Temp = 0.0
w_list = []
u_list = []


for a in range (50):    
    w_list.append(0)
    u_list.append(0)
    
eta_values = 50
T_values = 8

for i in range(T_values):
    Temp = Temp + 2*10    
    for j in range(eta_values):
        n = 0.1 + 0.2*j
        den_energy = stefan(n, Temp)
        
        w_list[j] = n
        u_list[j] = den_energy
    plt.savefig('filename.png', dpi=300)
    plt.plot(w_list, u_list,   label = Temp)
    plt.xlabel("Valor de ")
    plt.ylabel("Densidad de energía [       ]")
    plt.legend()