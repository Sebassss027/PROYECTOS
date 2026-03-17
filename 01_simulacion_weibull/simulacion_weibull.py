import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# -----------------------------
# 1. Simular tiempos de falla
# -----------------------------

np.random.seed(42)

beta_real = 2.5
eta_real = 5000

fallas = weibull_min.rvs(beta_real, scale=eta_real, size=50)

print("Tiempos de falla simulados:")
print(fallas)

# -----------------------------
# 2. Ajustar distribución Weibull
# -----------------------------

parametros = weibull_min.fit(fallas, floc=0)

beta_estimado = parametros[0]
eta_estimado = parametros[2]

print("\nParametros estimados:")
print("Beta:", beta_estimado)
print("Eta:", eta_estimado)

# -----------------------------
# 3. Curva de confiabilidad
# -----------------------------

tiempo = np.linspace(0, 10000, 100)

confiabilidad = np.exp(-(tiempo/eta_estimado)**beta_estimado)

# -----------------------------
# 4. Graficar
# -----------------------------

plt.plot(tiempo, confiabilidad)
plt.title("Curva de Confiabilidad Weibull")
plt.xlabel("Tiempo")
plt.ylabel("Confiabilidad")
plt.grid()

plt.show()