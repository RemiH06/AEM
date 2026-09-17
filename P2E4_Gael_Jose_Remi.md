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

La distribución normal o gaussiana es una de las herramientas fundamentales en la teoría de la probabilidad y la estadística inferencial debido a su recurrencia en fenómenos naturales, cuantitativos y sociales. Cuando una variable aleatoria continua $X$ sigue una distribución normal, sus propiedades probabilísticas quedan completamente determinadas por su media ($\mu$) y su varianza ($\sigma^2$). Además, bajo transformaciones lineales de la forma $Y = aX + b$, la variable resultante mantiene un comportamiento normal con parámetros transformados $\mu_Y = a\mu + b$ y $\sigma_Y^2 = a^2\sigma^2$.

En el ámbito multivariable, la distribución normal se generaliza a la distribución normal $n$-dimensional o multinormal. En el caso bivariado ($n=2$), la variable conjunta viene definida por un vector de medias $\boldsymbol{\mu}$ y una matriz de varianzas y covarianzas $\boldsymbol{\Sigma}$, la cual captura no solo las variabilidades individuales de cada variable, sino también el grado de asociación lineal existente entre ellas a través del coeficiente de correlación ($\rho$). 

El propósito de esta práctica es aplicar los conceptos de estandarización, propiedades de transformaciones lineales en variables univariadas y la formulación explícita de la función de densidad de probabilidad para distribuciones normales bivariadas mediante la resolución de problemas aplicados.

------------------------------------------------------------------------

## Desarrollo y Resultados

### Problema 1: Temperatura en la Ciudad

En una ciudad, la temperatura ambiente $X$ (en °C) se distribuye normalmente con media 20°C y desviación estándar 5°C.

**1. Calcula la probabilidad de que la temperatura en Fahrenheit se encuentre entre 68°F y 86°F, dado que** $F=1.8X+32$. 
- Convertimos a Celcius:
$$
X = \frac{68-32}{1.8} = 20°C
$$
$$
X = \frac{86-32}{1.8} = 30°C
$$
- Convertimos a $Z$ Y luego buscamos valor en la tabla de $Z$:
$$
Z_1 = \frac{20-20}{5} = 0
$$
$$
Z_2 = \frac{30-20}{5} = 2
$$
- Por lo tanto nuestra $Z$ que buscamos quedaria:
$$
(0<Z<2)≈0.4772
$$

**2. ¿Cuál es la probabilidad de que la temperatura no exceda los 25°C?** 
- Convertimos a $Z$: 
$$
Z = \frac{25-20}{5}=1
$$
- Por lo tanto la $Z$ que buscamos quedaria:
$$
(Z\leq 1)≈0.3413
$$
- Pero como buscamos una probabilidad menor que un numero positivo sumamos 0.5000:
$$
(Z\leq 1) ≈ 0.3413 + 0.5000 ≈ 0.8413
$$

**3. ¿Cuál es la probabilidad de que la temperatura no baje de los 90°F?** 
- Cobertimos a Clecius:
$$
X = \frac{90-32}{1.8} ≈ 32.22
$$
- Convertimos a valores de $Z$:
$$
Z = \frac{32.22 - 20}{5} ≈ 2.4
$$
- Por lo tanto la $Z$ que buscamos quedaria:
$$
(Z\geq2.4) ≈ 0.4918
$$
- Pero como buscamos una probabilidad en la cola superior se resta:
$$
(Z\geq2.4) ≈ 0.4918 - 0.5000 ≈ 0.0082
$$

------------------------------------------------------------------------

### Problema 2: Calibración de un Dispositivo de Medición

Un instrumento de medición registra la magnitud de una señal eléctrica $X$ que sigue una distribución normal con media 100 y desviación estándar 4. Para calibrar el dispositivo se aplica la transformación lineal $Y=0.95X+2$.

**1. Determina la probabilidad de que la señal calibrada supere 102.** 
- Aplicamos nuestra transformacion lineal:
$$
X = \frac{102-2}{0.95} ≈ 105.26
$$
- Convertimos a $Z$:
$$
Z = \frac{105.26-100}{4} ≈ 1.32
$$
- Por lo tant  o la $Z$ que buscamos seria:
$$
(Z > 1.32) ≈ 0.4066
$$
- Cola superior se resta:
$$
(Z > 1.32) ≈ 0.4066 - 0.5000 ≈ 0.0934
$$

**2. Calcula la probabilidad de que la señal original se encuentre entre 98 y 104.** 
- Convertimos a $Z$:
$$
Z_1 = \frac{98-100}{4} ≈-0.5
$$
$$
Z_2 = \frac{104-100}{4} ≈ 1
$$
- La $Z$ que buscamos seria:
$$
(0.5 \leq Z \leq 1) ≈ 0.1915 + 0.3413 ≈ 0.5328
$$

**3. ¿Cuál es la probabilidad de que la señal calibrada se sitúe entre 95 y 105?** 
- Calculamos las $X$
$$
X_1 = \frac{95-2}{0.95} ≈ 97.89
$$
$$
X_2 = \frac{105-2}{0.95} ≈ 108.42
$$
- Caluclamos las Z:
$$
Z_1 = \frac{95-97}{3.8} \approx -0.52
$$
$$
Z_2 = \frac{105-97}{3.8} \approx 2.1
$$
- La $Z$ que buscamos seria:
$$
(0.52 \leq Z \leq 2.1) \approx 0.1985 + 0.4821 \approx 0.6806
$$
------------------------------------------------------------------------

### Problema 3: Retornos de Inversión

El rendimiento diario de un activo financiero se modela mediante la variable $X$ que sigue una distribución normal con media 0.15% y desviación estándar 0.8%. Se ajusta el rendimiento mediante la transformación $Y=1.2X-0.05\%$.

**1. Calcula la probabilidad de que el rendimiento ajustado sea mayor a 0.2%.** 
 
- Aplicamos nuestra transformación lineal para despejar $X$:
$$
X = \frac{0.2 - (-0.05)}{1.2} = \frac{0.25}{1.2} \approx 0.2083
$$
- Convertimos a $Z$:
$$
Z = \frac{0.2083 - 0.15}{0.8} \approx 0.07
$$
- La $Z$ que buscamos seria:
$$
(Z > 0.07) \approx 0.0279
$$
- Cola superior se resta:
$$
(Z > 0.07) \approx 0.5000 - 0.0279 \approx 0.4721
$$

**2. ¿Cuál es la probabilidad de que el rendimiento original sea inferior a 0.1%.** 
- Convertimos a $Z$:
$$
Z = \frac{0.1 - 0.15}{0.8} \approx -0.06
$$
- La $Z$ que buscamos seria:
$$
(Z < -0.06) \approx 0.0239
$$
- Cola inferior se resta:
$$
(Z < -0.06) \approx 0.5000 - 0.0239 \approx 0.4761
$$

**3. Determina la probabilidad de que el rendimiento ajustado se encuentre entre 0% y 0.3%.** 
- Calculamos las $X$:
$$
X_1 = \frac{0 - (-0.05)}{1.2} \approx 0.0417
$$
$$
X_2 = \frac{0.3 - (-0.05)}{1.2} \approx 0.2917
$$
- Convertimos a $Z$:
$$
Z_1 = \frac{0.0417 - 0.15}{0.8} \approx -0.14
$$
$$
Z_2 = \frac{0.2917 - 0.15}{0.8} \approx 0.18
$$
- La $Z$ que buscamos seria:
$$
(-0.14 \le Z \le 0.18) \approx 0.0557 + 0.0714 \approx 0.1271
$$

------------------------------------------------------------------------

### Problema 4: Evaluación de Examen

Las calificaciones de un examen $X$ se distribuyen normalmente con media 70 y desviación estándar 12. Se implementa un bono que suma 5 puntos a cada calificación, de modo que la calificación final es $Y=X+5$.

**1. Calcula la probabilidad de que un estudiante obtenga una calificación inferior a 75 sin el bono.** 
- Convertimos a $Z$:
$$
Z = \frac{75 - 70}{12} \approx 0.42
$$
- La $Z$ que buscamos seria:
$$
(Z \le 0.42) \approx 0.1628
$$
- Sumamos 0.5000 para la probabilidad inferior:
$$
(Z \le 0.42) \approx 0.5000 + 0.1628 \approx 0.6628
$$

**2. ¿Cuál es la probabilidad de que, con el bono, el estudiante obtenga al menos 80?**
- Convertimos a $X$:
$$
X = 80 - 5 = 75
$$
- Convertimos a $Z$:
$$
Z = \frac{75 - 70}{12} \approx 0.42
$$
- La $Z$ que buscamos seria:
$$
(Z \ge 0.42) \approx 0.1628
$$
- Cola superior se resta:
$$
(Z \ge 0.42) \approx 0.5000 - 0.1628 \approx 0.3372
$$

**3. Determina la probabilidad de que la calificación final se ubique entre 70 y 85.** 
- Calculamos las $X$:
$$
X_1 = 70 - 5 = 65
$$
$$
X_2 = 85 - 5 = 80
$$
- Convertimos a $Z$:
$$
Z_1 = \frac{65 - 70}{12} \approx -0.42
$$
$$
Z_2 = \frac{80 - 70}{12} \approx 0.83
$$
- La $Z$ que buscamos seria:
$$
(-0.42 \le Z \le 0.83) \approx 0.1628 + 0.2967 \approx 0.4595
$$

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
