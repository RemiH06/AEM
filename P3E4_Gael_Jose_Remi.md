# ITESO, Universidad Jesuita de Guadalajara

**Materia:** Análisis Estadístico Multivariable

**Profesor:** Prof. Luis Alvarado

**Actividad:** Práctica 03 Máxima Verosimilitud

**Equipo:** 4

**Integrantes:**

1\. José García Fernández Del Valle

2\. Gael

3\. Lambda Remiel Heredia Pérez

**Fecha:** 17 de septiembre de 2026

------------------------------------------------------------------------

## Introducción
En la estadística, la estimación de parámetros es una herramienta fundamental que nos permite entender el comportamiento de una población a partir de una muestra de datos. Para lograr esto, uno de los enfoques más utilizados es el método de Máxima Verosimilitud (EMV). Este método opera bajo un principio lógico: busca encontrar el valor del parámetro que haga que los datos que ya observamos sean los más probables de ocurrir. El propósito de esta práctica es aplicar este método a la distribución de Poisson —un modelo utilizado para analizar el conteo de eventos en un tiempo determinado— y desarrollar matemáticamente el proceso para encontrar su estimador óptimo.
------------------------------------------------------------------------

## Desarrollo y Resultados

### Máxima Verosimilitud para la distribución de Poisson

La variable aleatoria $X$ sigue una distribución de Poisson con parámetro desconocido $\lambda$, es decir, $X \sim \text{Poisson}(\lambda)$.

La función de densidad de probabilidad (PDF) de una distribución de Poisson está dada por:

$$
f(k; \lambda) = P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k=0,1,2,...
$$

Se tiene una muestra aleatoria independiente $X_1, X_2, ..., X_n$ extraída de una distribución de Poisson con parámetro $\lambda$.

**1. Investiga un poco de la distribución de Poisson, y da un ejemplo de un experimento o suceso en el que es común que sea utilizado.**

Utilice la distribución de Poisson para describir el número de veces que un evento ocurre en un espacio finito de observación. Por ejemplo, una distribución de Poisson puede describir el número de defectos en el sistema mecánico de un avión o el número de llamadas a un centro de llamadas en una hora. La distribución de Poisson se utiliza con frecuencia en el control de calidad, los estudios de fiabilidad/supervivencia y los seguros.

Una variable sigue una distribución de Poisson si se cumplen las siguientes condiciones:
* Los datos son conteos de eventos (enteros no negativos, sin límite superior).
* Todos los eventos son independientes.
* La tasa promedio no cambia durante el período de interés.

La distribución de Poisson se especifica por un parámetro: lambda ($\lambda$). Este parámetro es igual a la media y la varianza. Cuando lambda aumente a valores lo suficientemente grandes, la distribución normal ($\lambda$, $\lambda$) podría utilizarse para aproximar la distribución de Poisson.

Fuente: Minitab, LLC. (s.f.). Distribución de Poisson. Soporte de Minitab. Recuperado el 16 de septiembre de 2026, de https://support.minitab.com/es-mx/minitab/help-and-how-to/probability-distributions-random-data-and-resampling-analyses/supporting-topics/distributions/poisson-distribution/

---

**Ejercicio:**
Un centro de atención al cliente sabe, por sus registros históricos, que recibe en promedio 15 llamadas por hora.
**Pregunta:** ¿Cuál es la probabilidad de que en la próxima hora reciban exactamente 20 llamadas?

**a. Datos del problema:**
Tenemos un promedio de llamadas por hora de $\lambda = 15$ y queremos calcular la probabilidad de recibir exactamente $k = 20$ llamadas.

**b. Fórmula general de la distribución de Poisson:**

$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

**c. Sustitución de los valores:**

$$P(X = 20) = \frac{15^{20} e^{-15}}{20!}$$

**d. Resultado final:**

$$P(X = 20) \approx 0.0418 \implies 4.18\%$$

---

**2. Encuentra el estimador de máxima verosimilitud (EMV) para $\lambda$, es decir, el valor de $\lambda$ que maximiza la función de log-verosimilitud.**

**a. Función de verosimilitud conjunta $L(\lambda)$:**
Dado que tenemos una muestra aleatoria independiente $X_1, X_2, \dots, X_n$, la función de verosimilitud conjunta es el producto de las funciones de probabilidad individuales:

$$L(\lambda) = \prod_{i=1}^{n} P(X_i = x_i) = \prod_{i=1}^{n} \frac{\lambda^{x_i} e^{-\lambda}}{x_i!}$$

Agrupando los términos (sumando los exponentes de $\lambda$ y multiplicando $e^{-\lambda}$ por sí mismo $n$ veces), obtenemos:

$$L(\lambda) = \frac{\lambda^{\sum_{i=1}^{n} x_i} e^{-n\lambda}}{\prod_{i=1}^{n} x_i!}$$

**b. Función de log-verosimilitud $l(\lambda)$:**
Aplicamos el logaritmo natural ($\ln$) para simplificar la expresión y transformar las multiplicaciones en sumas:

$$l(\lambda) = \ln(L(\lambda)) = \ln\left( \frac{\lambda^{\sum_{i=1}^{n} x_i} e^{-n\lambda}}{\prod_{i=1}^{n} x_i!} \right)$$

Usando las propiedades de los logaritmos, esto se expande a:

$$l(\lambda) = \ln\left( \lambda^{\sum_{i=1}^{n} x_i} \right) + \ln\left( e^{-n\lambda} \right) - \ln\left( \prod_{i=1}^{n} x_i! \right)$$

$$l(\lambda) = \left( \sum_{i=1}^{n} x_i \right) \ln(\lambda) - n\lambda - \ln\left( \prod_{i=1}^{n} x_i! \right)$$

**c. Derivada de $l(\lambda)$ respecto a $\lambda$:**
Ahora derivamos la función de log-verosimilitud con respecto a nuestro parámetro $\lambda$. Dado que el último término no contiene $\lambda$, se considera una constante y su derivada es cero:

$$\frac{d}{d\lambda} l(\lambda) = \frac{\sum_{i=1}^{n} x_i}{\lambda} - n$$

**d. Igualar a cero y despejar $\hat{\lambda}$:**
Para encontrar el máximo, igualamos la derivada a cero y despejamos para obtener nuestro estimador $\hat{\lambda}$:

$$\frac{\sum_{i=1}^{n} x_i}{\hat{\lambda}} - n = 0$$

Pasamos la $n$ al otro lado:

$$\frac{\sum_{i=1}^{n} x_i}{\hat{\lambda}} = n$$

Despejamos $\hat{\lambda}$:

$$\hat{\lambda} = \frac{\sum_{i=1}^{n} x_i}{n}$$

---

**3. Interpreta el resultado obtenido en términos de la media muestral.** Como se demostró en el desarrollo anterior, el estimador de máxima verosimilitud (EMV) para el parámetro $\lambda$ resulta ser:

$$\hat{\lambda} = \frac{\sum_{i=1}^{n} x_i}{n} = \bar{X}$$

**Relación con la media muestral:**

Este resultado indica que la mejor estimación (en términos de máxima verosimilitud) para el verdadero parámetro $\lambda$ de la población es, intuitivamente, el **promedio aritmético de los datos observados en la muestra** (la media muestral, $\bar{X}$).

En el contexto de la distribución de Poisson, el parámetro $\lambda$ representa la tasa promedio de ocurrencia de un evento en un intervalo dado (el valor esperado, $E(X) = \lambda$). Por lo tanto, tiene perfecto sentido lógico y matemático que si queremos estimar cuántos eventos ocurren en promedio en la población general, la mejor manera de hacerlo sea promediando la cantidad de eventos que ocurrieron en nuestra muestra recolectada. 

En términos prácticos (como en el ejemplo del centro de atención al cliente), si tomamos una muestra de $n$ horas diferentes y sumamos todas las llamadas recibidas en esas horas ($\sum x_i$), al dividir ese total entre el número de horas observadas ($n$), obtenemos exactamente $\bar{X}$. Este promedio empírico es el estimador más probable para el verdadero promedio teórico $\lambda$.

------------------------------------------------------------------------

## Conclusiones

Al finalizar esta práctica, pudimos comprobar cómo el método de máxima verosimilitud nos permite conectar la teoría estadística con los datos empíricos. A través del desarrollo matemático y usando las propiedades de los logaritmos, demostramos que el mejor estimador para el parámetro $\lambda$ de la distribución de Poisson es la media muestral ($\bar{X}$). Esto nos indica que la mejor manera de estimar la tasa promedio de eventos en una población es calculando el promedio de los datos que recolectamos. Así, confirmamos que este método matemático nos ofrece una base rigurosa para respaldar resultados que también tienen mucho sentido intuitivo.
