# ITESO, Universidad Jesuita de Guadalajara

**Materia:** Análisis Estadístico Multivariable

**Profesor:** Prof. Luis Alvarado

**Actividad:** Práctica 02 - Distribución normal y multinormal

**Equipo:** [Número o Nombre de tu equipo]

**Integrantes:**

1\. José García Fernández Del Valle

2\. Gael

3\. Remiel

**Fecha:** 17 de septiembre de 2026

------------------------------------------------------------------------

## Introducción

[Escribe aquí una breve introducción sobre los conceptos de distribución normal univariada y multivariada, y el propósito de esta práctica.]

------------------------------------------------------------------------

## Desarrollo y Resultados

### Problema 1: Temperatura en la Ciudad

En una ciudad, la temperatura ambiente $X$ (en °C) se distribuye normalmente con media 20°C y desviación estándar 5°C.

**1. Calcula la probabilidad de que la temperatura en Fahrenheit se encuentre entre 68°F y 86°F, dado que** $F=1.8X+32$. \* [Tu desarrollo y respuesta aquí. Puedes usar ecuaciones así: $P(68 < F < 86) = ...$]

**2. ¿Cuál es la probabilidad de que la temperatura no exceda los 25°C?** \* [Tu desarrollo y respuesta aquí.]

**3. ¿Cuál es la probabilidad de que la temperatura no baje de los 90°F?** \* [Tu desarrollo y respuesta aquí.]

------------------------------------------------------------------------

### Problema 2: Calibración de un Dispositivo de Medición

Un instrumento de medición registra la magnitud de una señal eléctrica $X$ que sigue una distribución normal con media 100 y desviación estándar 4. Para calibrar el dispositivo se aplica la transformación lineal $Y=0.95X+2$.

**1. Determina la probabilidad de que la señal calibrada supere 102.** \* [Tu desarrollo y respuesta aquí.]

**2. Calcula la probabilidad de que la señal original se encuentre entre 98 y 104.** \* [Tu desarrollo y respuesta aquí.]

**3. ¿Cuál es la probabilidad de que la señal calibrada se sitúe entre 95 y 105?** \* [Tu desarrollo y respuesta aquí.]

------------------------------------------------------------------------

### Problema 3: Retornos de Inversión

El rendimiento diario de un activo financiero se modela mediante la variable $X$ que sigue una distribución normal con media 0.15% y desviación estándar 0.8%. Se ajusta el rendimiento mediante la transformación $Y=1.2X-0.05\%$.

**1. Calcula la probabilidad de que el rendimiento ajustado sea mayor a 0.2%.** \* [Tu desarrollo y respuesta aquí.]

**2. ¿Cuál es la probabilidad de que el rendimiento original sea inferior a 0.1%.** \* [Tu desarrollo y respuesta aquí.]

**3. Determina la probabilidad de que el rendimiento ajustado se encuentre entre 0% y 0.3%.** \* [Tu desarrollo y respuesta aquí.]

------------------------------------------------------------------------

### Problema 4: Evaluación de Examen

Las calificaciones de un examen $X$ se distribuyen normalmente con media 70 y desviación estándar 12. Se implementa un bono que suma 5 puntos a cada calificación, de modo que la calificación final es $Y=X+5$.

**1. Calcula la probabilidad de que un estudiante obtenga una calificación inferior a 75 sin el bono.** \* [Tu desarrollo y respuesta aquí.]

**2. ¿Cuál es la probabilidad de que, con el bono, el estudiante obtenga al menos 80?** \* [Tu desarrollo y respuesta aquí.]

**3. Determina la probabilidad de que la calificación final se ubique entre 70 y 85.** \* [Tu desarrollo y respuesta aquí.]

------------------------------------------------------------------------

### Problema 5: Distribución Multinormal

Dados los siguientes valores: $X$ sigue una distribución normal bivariante con:

$$
X = \begin{pmatrix} X_1 \\ X_2 \end{pmatrix}, \quad \mu = \begin{pmatrix} 45 \\ 120 \end{pmatrix}, \quad \Sigma = \begin{pmatrix} 16 & 4 \\ 4 & 25 \end{pmatrix}
$$

**1. Determina la función de densidad de probabilidad de la variable multinormal** $X$. *PISTA: Función de Densidad de la Distribución Normal Bivariada*

$$
f_{X_1,X_2}(x_1,x_2) = \frac{1}{2\pi\sigma_1\sigma_2\sqrt{1-\rho^2}} \exp\left\{ -\frac{1}{2(1-\rho^2)} \left[ \frac{(x_1-\mu_1)^2}{\sigma_1^2} - 2\rho\frac{(x_1-\mu_1)(x_2-\mu_2)}{\sigma_1\sigma_2} + \frac{(x_2-\mu_2)^2}{\sigma_2^2} \right] \right\}
$$

-   [Tu desarrollo y respuesta aquí. Desglosa las varianzas, covarianzas y calcula $\rho$ para sustituirlos en la fórmula general].

------------------------------------------------------------------------

## Conclusiones

[Escribe aquí tus conclusiones sobre lo aprendido en esta práctica, cómo las transformaciones lineales afectan la media y la varianza en una distribución normal, y la interpretación de la matriz de varianzas y covarianzas en el caso bivariado.]
