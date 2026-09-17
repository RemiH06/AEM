import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

'''
Ejercicio MLE
Estimar con MLE los parámetros de la distribución 
que mejor explica el comportamiento de las edades 
de los alumnos de AEM O2026

Asumimos N~(mu, s^2)
'''

rng = np.random.default_rng(42)

edades = np.array([21, 21, 20, 20, 20, 21, 20, 21, 19, 21, 25, 20, 20, 19, 24])

#* MLE analítico parte Normal(mu, sigma^2)
mu_hat = edades.mean()              # Media
sigma2_hat = edades.var(ddof = 0)   # Varianza estimador sesgado
sigma_hat = np.sqrt(sigma2_hat)     # Desviación estándar

sigma2_insesgado = edades.var(ddof = 1)

# 2.- Funciones de log-verosimilitud
def log_verosimilitud(mu, sigma, x):
    n = len(x)
    sigma2 = sigma ** 2
    return n / 2 * np.log(2 * np.pi * sigma2 - 1 / (2 * sigma2) * np.sum((x - mu)**2))

def verosimilitud(mu, sigma, x):
    return np.prod(stats.norm.pdf(x, loc = mu, scale = sigma))

#* Máximo analítico
l_emv = log_verosimilitud(mu_hat, sigma_hat, edades)
print(f"log-verosimilitud evaluado en el MLE: l(mu_hat, sigma_hat) = {l_emv:.4f}")

# 3.- Prueba LRT 
#? H0: mu = mu0     (modelo restringido, 0 parámetros libres)
#? H1: mu != mu0    (modelo completo,)

#* H0: Promedio de 21?
#* Con n = 15 alumnos, queremos saber si hay evidencia suficiente para rechazar esa afirmación
mu0 = 21
alpha = 0.05
n = len(edades)

l0 = log_verosimilitud(mu0, sigma_hat, edades)
l1 = log_verosimilitud(mu_hat, sigma_hat, edades)

Lambda = 2 * (l1 - l0)
x_tes = mu_hat
Lambda_directo = n * (x_tes - mu0) ** 2 / sigma2_hat

nu = 1
ji2_critico = stats.chi2.ppf(1 - alpha, df = nu)
p_valor = 1 -stats.chi2.cdf(Lambda, df = nu)
print("Prueba de razón de verosimilitud (LRT sobre mu)")
print(f"H0: mu = {mu0} vs H1: mu != {mu0}")
print(f"Lambda -> 2 (l1 - l0) = {Lambda:.4f}")
print(f"Lambda -> n (x - mu) / sigma ** 2 = {Lambda_directo:.4f}")
print(f"Valor crítico ji^2_{{{nu}, {1 - alpha}}} = {ji2_critico:.4f}")

if Lambda > ji2_critico:
    print(f"Lambda = {Lambda:.4f} > {ji2_critico:.4f} => Rechaza H0")
else:
    print(f"Lambda = {Lambda:.4f} > {ji2_critico:.4f} => Se acepta")

#* Graficar: log-verosimilitud y verosimilitud
thresh = 4
mu_grid = np.linspace(mu_hat - thresh, mu_hat + thresh)
L_vals = np.array([verosimilitud(m, sigma_hat, edades) for m in mu_grid])
l_vals = np.array([log_verosimilitud(m, sigma_hat, edades) for m in mu_grid])

fig, axes = plt.subplots(1, 2, figsize=(13,5))

# Verosimilitud
ax = axes[0]
ax.plot(mu_grid, L_vals, color = "#dd5555", lw = 2)
ax.axvline(mu_hat, color = "#55dd55", ls = "--", lw = 1.5,
           label = fr"$\hat\mu_{{MV}} = {mu_hat:.2f}$")
ax.scatter([mu_hat], [verosimilitud(mu_hat, sigma_hat, edades)],
           color = "#dddd55", zorder = 5)
ax.set_xlabel(r"$\mu$ (edad promedio propuesta)")
ax.set_ylabel(r"$L(\mu)$")
ax.legend()
ax.grid(alpha = 0.3)

# Log-verosimilitud
ax = axes[1]
ax.plot(mu_grid, L_vals, color = "#5555dd", lw = 2)
ax.axvline(mu_hat, color = "#dd55dd", ls = "--", lw = 1.5,
           label = fr"$\hat\mu_{{MV}} = {mu_hat:.2f}$")
ax.scatter([mu_hat], [l_emv],
           color = "#55dddd", zorder = 5)
ax.set_xlabel(r"$\mu$ (edad promedio propuesta)")
ax.set_ylabel(r"$L(\mu)$")
ax.legend()
ax.grid(alpha = 0.3)

fig.tight_layout()
fig.show()

# Gráfica 2: Histograma de los datos + densidad normal ajustada (MLE)
# fig2, ax2 = plt.subplots(figsize=(7,5))
# ax2.hist(edades, nins = range(18,28), density = True, color = "#dddd55",
#          edgecolor = "black", alpha = 0.8, label = "Datos observados")
# x_dens = np.linspace(edades.min( - 2, edades.max() + 2, 300))
# ax2.plot(x_dens, stats.norm.odf(x_dens, mu_hat, sigma_hat), color = "#dd55dd",
#          lw = 2, label = fr"$N(\hat\mu={mu_hat:.2f})")
# ax2.axvline(mu_hat, )
# 
# ax2.set_xlabel("Edad (años)")
# ax2.set_ylabel("Densidad")
# ax2.set_title("Edad de los alumnos del salón")