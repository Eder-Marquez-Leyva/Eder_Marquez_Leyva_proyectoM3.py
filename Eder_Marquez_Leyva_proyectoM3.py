import pip
import numpy as np
import matplotlib.pyplot as plt


# Configuración de la máquina de Galton
num_canicas = 3000 # Ingresamos el número total de canicas
num_niveles = 12    # Ingresamos el número total de niveles o en este 
                     # caso de clavos

# Realizamos la ejecucion para saber la trayectoria de cada canica
trayectorias = np.zeros(num_canicas, dtype=int)

for i in range(num_canicas):
    # Cada canica toma decisiones aleatorias en cada nivel
    decisiones = np.random.choice([0, 1], size=num_niveles)  # 0: izquierda, 1: derecha

# La suma determina la posición final de cada canica
    trayectorias[i] = np.sum(decisiones)  


# Ejecutamos el histograma para observar la distribución de las canicas

plt.hist(trayectorias, bins=num_niveles + 1, edgecolor='black', density=True)
# Colocamos los nombres a los ejes y el título del gráfico
plt.title("Máquina de Galton")
plt.xlabel("Posición final")
plt.ylabel("Frecuencia ")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()