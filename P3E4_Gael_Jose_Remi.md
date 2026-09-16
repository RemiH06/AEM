# ITESO, Universidad Jesuita de Guadalajara

**Materia:** Análisis Estadístico Multivariable

**Profesor:** Prof. Luis Alvarado

**Actividad:** Práctica 03 Máxima Verosimilitud

**Equipo:** 4

**Integrantes:**

1\. José García Fernández Del Valle

2\. Gael

3\. Remiel

**Fecha:** 17 de septiembre de 2026

------------------------------------------------------------------------

## Introducción

[Escribe aquí una breve introducción sobre la estimación de parámetros, el método de máxima verosimilitud y el propósito general de esta práctica.]

------------------------------------------------------------------------

## Desarrollo y Resultados

### Máxima Verosimilitud para la distribución de Poisson

La variable aleatoria $X$ sigue una distribución de Poisson con parámetro desconocido $\lambda$, es decir, $X \sim \text{Poisson}(\lambda)$.

La función de densidad de probabilidad (PDF) de una distribución de Poisson está dada por:

$$
f(k; \lambda) = P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k=0,1,2,...
$$

Se tiene una muestra aleatoria independiente $X_1, X_2, ..., X_n$ extraída de una distribución de Poisson con parámetro $\lambda$.

**1. Investiga un poco de la distribución de Poisson, y da un ejemplo de un experimento o suceso en el que es común que sea utilizado.** \* 
Utilice la distribución de Poisson para describir el número de veces que un evento ocurre en un espacio finito de observación. Por ejemplo, una distribución de Poisson puede describir el número de defectos en el sistema mecánico de un avión o el número de llamadas a un centro de llamadas en una hora. La distribución de Poisson se utiliza con frecuencia en el control de calidad, los estudios de fiabilidad/supervivencia y los seguros.

Una variable sigue una distribución de Poisson si se cumplen las siguientes condiciones:
Los datos son conteos de eventos (enteros no negativos, sin límite superior).
Todos los eventos son independientes.
La tasa promedio no cambia durante el período de interés.

La distribución de Poisson se especifica por un parámetro: lambda (λ). Este parámetro es igual a la media y la varianza. Cuando lambda aumente a valores lo suficientemente grandes, la distribución normal (λ, λ) podría utilizarse para aproximar la distribución de Poisson.

Fuente: Minitab, LLC. (s.f.). Distribución de Poisson. Soporte de Minitab. Recuperado el 16 de septiembre de 2026, de https://support.minitab.com/es-mx/minitab/help-and-how-to/probability-distributions-random-data-and-resampling-analyses/supporting-topics/distributions/poisson-distribution/

**2. Encuentra el estimador de máxima verosimilitud (EMV) para** $\lambda$, es decir, el valor de $\lambda$ que maximiza la función de log-verosimilitud. \* [Tu desarrollo matemático aquí. Pasos sugeridos: 1. Plantea la función de verosimilitud conjunta $L(\lambda)$. 2. Aplica logaritmo natural para obtener la log-verosimilitud $l(\lambda)$. 3. Deriva $l(\lambda)$ respecto a $\lambda$. 4. Iguala la derivada a cero y despeja $\lambda$ para encontrar el estimador $\hat{\lambda}$].

**3. Interpreta el resultado obtenido en términos de la media muestral.** \* [Tu respuesta e interpretación aquí sobre cómo se relaciona el estimador que acabas de encontrar con el promedio de la muestra].

------------------------------------------------------------------------

## Conclusiones

[Escribe aquí tus conclusiones sobre lo aprendido en esta práctica, por qué el método de máxima verosimilitud es útil y qué nos dice sobre el parámetro $\lambda$ de la distribución de Poisson.]
