import numpy as np
import matplotlib.pyplot as plt
v0 = 5                  # Velocidade inicial 
g = 10                  # Aceleração da gravidade
t = np.linspace(0,1,1001)# Tempo
y = v0 * t - 0.5 * g * t ** 2        # Posição vertial 
plt.plot(t,y) # plotar o grafico yxt
plt.xlabel('t (s)')    # eixo x com t(s)
plt.ylabel('y (m)')    # eixo y como y (m)
plt.show() # mostrar a figura 