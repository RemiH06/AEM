---
editor_options: 
  markdown: 
    wrap: 72
---

# Práctica 2 - Modelos de distribución multivariados (continuos y discretos)

------------------------------------------------------------------------

### 1.

Sea $X$ e $Y$ una variable aleatoria bidimensional discreta con función
de masa de probabilidad conjunta:

| $X \backslash Y$ |   1   |   3   |
|:----------------:|:-----:|:-----:|
|      **0**       |  $0$  | $1/8$ |
|      **1**       | $3/8$ |  $0$  |
|      **2**       | $3/8$ |  $0$  |
|      **3**       |  $0$  | $1/8$ |

Obtenga la función de distribución acumulada
$F(x, y) = P(X \le x, Y \le y)$ para los siguientes intervalos:

$$
F(x, y) = \begin{cases} 
\text{si } x < 0, y < 1 \\
\text{si } 0 \le x < 1, 1 \le y < 3 \\
\text{si } 0 \le x < 1, y \ge 3 \\
\text{si } 1 \le x < 2, y \ge 1 \\
\text{si } 2 \le x < 3, y \ge 1 \\
\text{si } x \ge 3, 1 \le y < 3 \\
\text{si } x \ge 3, y \ge 3 
\end{cases}
$$

#### Respuesta:

# Función de Distribución Acumulada Conjunta

## Función de masa de probabilidad conjunta

| $X \backslash Y$ |   1   |   3   |
|:----------------:|:-----:|:-----:|
|      **0**       |  $0$  | $1/8$ |
|      **1**       | $3/8$ |  $0$  |
|      **2**       | $3/8$ |  $0$  |
|      **3**       |  $0$  | $1/8$ |

## Respuesta

**Función de distribución acumulada conjunta** $F(x, y)$:

$$
F(x, y) = P(X \le x, Y \le y) = \begin{cases}
0, & \text{si } x < 0 \text{ o } y < 1 \\[4pt]
0, & \text{si } 0 \le x < 1,\ 1 \le y < 3 \\[4pt]
\dfrac{1}{8}, & \text{si } 0 \le x < 1,\ y \ge 3 \\[4pt]
\dfrac{3}{8}, & \text{si } 1 \le x < 2,\ 1 \le y < 3 \\[4pt]
\dfrac{1}{2}, & \text{si } 1 \le x < 2,\ y \ge 3 \\[4pt]
\dfrac{3}{4}, & \text{si } 2 \le x < 3,\ 1 \le y < 3 \\[4pt]
\dfrac{7}{8}, & \text{si } 2 \le x < 3,\ y \ge 3 \\[4pt]
\dfrac{3}{4}, & \text{si } x \ge 3,\ 1 \le y < 3 \\[4pt]
1, & \text{si } x \ge 3,\ y \ge 3
\end{cases}
$$

**Desarrollo (acumulando celdas con** $X \le x$, $Y \le y$)

-   $1\le x<2,\ y\ge3$:
    $\ P(0,1)+P(0,3)+P(1,1)+P(1,3) = 0+\frac18+\frac38+0=\frac48=\frac12$

-   $2\le x<3,\ 1\le y<3$:
    $\ P(0,1)+P(1,1)+P(2,1) = 0+\frac38+\frac38=\frac68=\frac34$

-   $2\le x<3,\ y\ge3$: suma de todas las celdas con $X\in\{0,1,2\}$:
    $\frac18+\frac38+\frac38=\frac78$

-   $x\ge3,\ 1\le y<3$: todas las celdas con $Y=1$:
    $0+\frac38+\frac38+0=\frac34$

-   

    ## $x\ge3,\ y\ge3$: tabla completa $=1$

### 2.

A continuación, se muestra la distribución de masa de probabilidad
conjunta de $X$, el número de contratos otorgados a la empresa A, y $Y$,
el número de contratos otorgados a la empresa B:

| $X \backslash Y$ |   0   |   1   |   2   |
|:----------------:|:-----:|:-----:|:-----:|
|      **0**       | $1/9$ | $2/9$ | $1/9$ |
|      **1**       | $2/9$ | $2/9$ |  $0$  |
|      **2**       | $1/9$ |  $0$  |  $0$  |

-   **a)** Encuentre $f_{XY}(0,1)$. ¿Cuál es la interpretación de este
    valor? **Respuesta:** $F_{XY}(0,1) = \frac{2}{9}$. Significa que la
    probabilidad de que la empresa A reciba 0 contratos y la empresa B
    reciba 1 contrato es de $\frac{2}{9}$(o aproximadamente 22.22%)

-   **b)** Proporcione las funciones de probabilidad marginal de $X$ y
    $Y$. **Respuesta:** Para obtener la probabilidad marginal de $X$,
    sumamos las probabilidades a lo largo de cada fila:

-   $f_X(0) = f_{XY}(0,0) + f_{XY}(0,1) + f_{XY}(0,2) = \frac{1}{9} + \frac{2}{9} + \frac{1}{9} = \frac{4}{9}$

-   $f_X(1) = f_{XY}(1,0) + f_{XY}(1,1) + f_{XY}(1,2) = \frac{2}{9} + \frac{2}{9} + 0 = \frac{4}{9}$

-   $f_X(2) = f_{XY}(2,0) + f_{XY}(2,1) + f_{XY}(2,2) = \frac{1}{9} + 0 + 0 = \frac{1}{9}$
    Para obtener la probabilidad marginal de $Y$, sumamos las
    probabilidades a lo largo de cada columna:

-   $f_Y(0) = f_{XY}(0,0) + f_{XY}(1,0) + f_{XY}(2,0) = \frac{1}{9} + \frac{2}{9} + \frac{1}{9} = \frac{4}{9}$

-   $f_Y(1) = f_{XY}(0,1) + f_{XY}(1,1) + f_{XY}(2,1) = \frac{2}{9} + \frac{2}{9} + 0 = \frac{4}{9}$

-   $f_Y(2) = f_{XY}(0,2) + f_{XY}(1,2) + f_{XY}(2,2) = \frac{1}{9} + 0 + 0 = \frac{1}{9}$

-   **c)** Proporcione la función de probabilidad condicional para $Y$
    dado que $X=2$. **Respuesta:** Aplicamos la fórmula de probabilidad
    condicional $f(Y \mid X=2) = \frac{f_{XY}(x,y)}{f_X(2)}$ utilizando
    $f_X(2) = \frac{1}{9}$:

-   $P(Y=0 \mid X=2) = \frac{f_{XY}(2,0)}{f_X(2)} = \frac{1/9}{1/9} = 1$

-   $P(Y=1 \mid X=2) = \frac{f_{XY}(2,1)}{f_X(2)} = \frac{0}{1/9} = 0$

-   $P(Y=2 \mid X=2) = \frac{f_{XY}(2,2)}{f_X(2)} = \frac{0}{1/9} = 0$

$$
f(Y \mid X=2) = \begin{cases} 
1, & \text{si } y = 0 \\
0, & \text{si } y = 1, 2 
\end{cases}
$$ - **d)** Proporcione la función de probabilidad condicional para $X$
dado que $Y=1$. **Respuesta:** Aplicamos la fórmula de probabilidad
condicional $f(X \mid Y=1) = \frac{f_{XY}(x,y)}{f_Y(1)}$ utilizando
$f_Y(1) = \frac{4}{9}$:

-   $P(X=0 \mid Y=1) = \frac{f_{XY}(0,1)}{f_Y(1)} = \frac{2/9}{4/9} = \frac{2}{4} = \frac{1}{2}$
-   $P(X=1 \mid Y=1) = \frac{f_{XY}(1,1)}{f_Y(1)} = \frac{2/9}{4/9} = \frac{2}{4} = \frac{1}{2}$
-   $P(X=2 \mid Y=1) = \frac{f_{XY}(2,1)}{f_Y(1)} = \frac{0}{4/9} = 0$

$$
f(X \mid Y=1) = \begin{cases} 
\frac{1}{2}, & \text{si } x = 0 \\
\frac{1}{2}, & \text{si } x = 1 \\
0, & \text{si } x = 2 
\end{cases}
$$ - **e)** ¿Cuál es la probabilidad de que se hayan otorgado dos
contratos a la empresa B dado que se le otorgó un contrato a la empresa
A? **Respuesta:** Se busca la probabilidad condicional
$P(Y=2 \mid X=1)$:
$$P(Y=2 \mid X=1) = \frac{f_{XY}(1,2)}{f_X(1)} = \frac{0}{4/9} = 0$$ La
probabilidad de que se le otorguen dos contratos a la empresa B dado que
a la empresa A se le otorgó un contrato es de **0**. - **f)** ¿$X$ y $Y$
son independientes? ¿Por qué sí o por qué no? **Respuesta:** Para que
$X$ y $Y$ sean independientes, usamos la scondición
$f_{XY}(x,y) = f_X(x) \cdot f_Y(y)$ para todo par $(x,y)$. Evaluamos
para $x=0, y=0$: \* Valor en la tabla: $f_{XY}(0,0) = \frac{1}{9}$ \*
Producto de marginales:
$f_X(0) \cdot f_Y(0) = \frac{4}{9} \cdot \frac{4}{9} = \frac{16}{81}$
Como $f_{XY}(0,0) \neq f_X(0) \cdot f_Y(0)$
$\left(\frac{1}{9} \neq \frac{16}{81}\right)$, la condición no se
satisface. **No son independientes**, ya que la probabilidad conjunta de
que ambas empresas reciban un número específico de contratos no es igual
al producto de sus probabilidades marginales individuales.

------------------------------------------------------------------------

### 3.

A continuación, se da la función de masa de probabilidad conjunta
asociada con datos obtenidos en un estudio de accidentes
automovilísticos en los que un niño (de menos de 5 años) estaba en el
auto y hubo al menos una persona muerta. Específicamente el estudio se
concentró en si el niño sobrevivió y qué tipo de cinturón de seguridad
(si lo había) utilizaba.

Defina:

$$
X = \begin{cases} 0, & \text{si el niño sobrevivió} \\ 1, & \text{si no} \end{cases}
$$

$$
Y = \begin{cases} 0, & \text{si no usaba cinturón} \\ 1, & \text{si usaba cinturón para adulto} \\ 2, & \text{si usaba cinturón del asiento del auto} \end{cases}
$$

| $X \backslash Y$ |  0   |  1   |  2   |
|:----------------:|:----:|:----:|:----:|
|      **0**       | 0.38 | 0.14 | 0.24 |
|      **1**       | 0.17 | 0.02 | 0.05 |

-   **a)** Encuentre $F(1,1)$. ¿Cuál es la interpretación de este valor?
    **Respuesta:** Por definición de la función de distribución
    acumulada conjunta:
    $$F(1,1) = P(X \le 1, Y \le 1) = f_{XY}(0,0) + f_{XY}(0,1) + f_{XY}(1,0) + f_{XY}(1,1)$$
    Sustituyendo los valores de la tabla:
    $$F(1,1) = 0.38 + 0.14 + 0.17 + 0.02 = 0.71$$ **Interpretación:**
    Existe una probabilidad del $0.71$ (o $71\%$) de que un niño
    involucrado en un accidente no haya utilizado cinturón o haya
    utilizado cinturón para adulto ($Y \le 1$), considerando cualquier
    resultado sobre su supervivencia ($X \le 1$).
-   **b)** Proporcione las funciones de probabilidad marginal de $X$ y
    $Y$. **Respuesta:** Para obtener la función de probabilidad marginal
    de $X$, sumamos las probabilidades a lo largo de cada fila:
-   $f_X(0) = f_{XY}(0,0) + f_{XY}(0,1) + f_{XY}(0,2) = 0.38 + 0.14 + 0.24 = 0.76$
-   $f_X(1) = f_{XY}(1,0) + f_{XY}(1,1) + f_{XY}(1,2) = 0.17 + 0.02 + 0.05 = 0.24$
    $$
    f_X(x) = \begin{cases} 
    0.76, & \text{si } x = 0 \\
    0.24, & \text{si } x = 1 
    \end{cases}
    $$ Para obtener la función de probabilidad marginal de $Y$, sumamos
    las probabilidades a lo largo de cada columna:
-   $f_Y(0) = f_{XY}(0,0) + f_{XY}(1,0) = 0.38 + 0.17 = 0.55$
-   $f_Y(1) = f_{XY}(0,1) + f_{XY}(1,1) = 0.14 + 0.02 = 0.16$
-   $f_Y(2) = f_{XY}(0,2) + f_{XY}(1,2) = 0.24 + 0.05 = 0.29$ $$
    f_Y(y) = \begin{cases} 
    0.55, & \text{si } y = 0 \\
    0.16, & \text{si } y = 1 \\
    0.29, & \text{si } y = 2 
    \end{cases}
    $$
-   **c)** Proporcione la función de probabilidad condicional para $Y$
    dado que $X=0$. **Respusta:** Aplicamos la fórmula de probabilidad
    condicional $f(Y \mid X=0) = \frac{f_{XY}(0,y)}{f_X(0)}$ utilizando
    la marginal $f_X(0) = 0.76$:
-   $P(Y=0 \mid X=0) = \frac{f_{XY}(0,0)}{f_X(0)} = \frac{0.38}{0.76} = \frac{1}{2}$
-   $P(Y=1 \mid X=0) = \frac{f_{XY}(0,1)}{f_X(0)} = \frac{0.14}{0.76} = \frac{7}{38}$
-   $P(Y=2 \mid X=0) = \frac{f_{XY}(0,2)}{f_X(0)} = \frac{0.24}{0.76} = \frac{6}{19}$
    $$
    f(Y \mid X=0) = \begin{cases} 
    \frac{1}{2}, & \text{si } y = 0 \\[4pt]
    \frac{7}{38}, & \text{si } y = 1 \\[4pt]
    \frac{6}{19}, & \text{si } y = 2 
    \end{cases}
    $$
-   **d)** Proporcione la función de probabilidad condicional para $X$
    dado que $Y=2$. **Respuesta:** Aplicamos la fórmula de probabilidad
    condicional $f(X \mid Y=2) = \frac{f_{XY}(x,2)}{f_Y(2)}$ utilizando
    la marginal $f_Y(2) = 0.29$:
-   $P(X=0 \mid Y=2) = \frac{f_{XY}(0,2)}{f_Y(2)} = \frac{0.24}{0.29} = \frac{24}{29}$
-   $P(X=1 \mid Y=2) = \frac{f_{XY}(1,2)}{f_Y(2)} = \frac{0.05}{0.29} = \frac{5}{29}$
    $$
    f(X \mid Y=2) = \begin{cases} 
    \frac{24}{29}, & \text{si } x = 0 \\[4pt]
    \frac{5}{29}, & \text{si } x = 1 
    \end{cases}
    $$
-   **e)** ¿Cuál es la probabilidad de que un niño sobreviva dado que
    llevaba puesto el cinturón del asiento del auto? **Respuesta:**
    $$P(X=0 \mid Y=2) = \frac{f_{XY}(0,2)}{f_Y(2)} = \frac{0.24}{0.29} = \frac{24}{29} \approx 0.8276$$
    La probabilidad de que un niño sobreviva dado que llevaba puesto el
    cinturón del asiento del auto es de $\frac{24}{29}$ (aproximadamente
    $82.76\%$).
-   **f)** ¿$X$ y $Y$ son independientes? ¿Por qué sí o por qué no?
    **Respuesta:** Para que $X$ y $Y$ sean independientes, vamos a usar
    $f_{XY}(x,y) = f_X(x) \cdot f_Y(y)$ para todos los pares $(x,y)$.
    Evaluamos en el punto $(x=0, y=0)$:
-   Valor en la tabla: $f_{XY}(0,0) = 0.38$
-   Producto de marginales:
    $f_X(0) \cdot f_Y(0) = 0.76 \cdot 0.55 = 0.418$ Dado que
    $f_{XY}(0,0) \neq f_X(0) \cdot f_Y(0)$ ($0.38 \neq 0.418$), la
    condición de independencia no se satisface. **No son
    independientes**, lo que indica que el uso del cinturón de seguridad
    ($Y$) y la supervivencia del niño ($X$) están asociados.

------------------------------------------------------------------------

### 4.

De un grupo de tres republicanos, dos demócratas y uno independiente se
ha de seleccionar aleatoriamente un comité de dos personas. La función
de masa de probabilidad conjunta asociada con el número de republicanos
($X$) y el número de demócratas ($Y$) que conforman un comité se muestra
a continuación:

| $Y \backslash X$ |   0    |   1    |   2    |
|:----------------:|:------:|:------:|:------:|
|      **0**       |  $0$   | $3/15$ | $3/15$ |
|      **1**       | $2/15$ | $6/15$ |  $0$   |
|      **2**       | $1/15$ |  $0$   |  $0$   |

-   **a)** Encuentre la probabilidad de que en el comité haya dos
    republicanos y un demócrata. **Respuesta:**
    $$P(X=2, Y=1) = f_{XY}(2,1) = 0$$ La probabilidad es **0**, ya que
    el comité consta únicamente de dos personas, por lo que es imposible
    seleccionar a tres personas en total.
-   **b)** Encuentre la probabilidad de que en el comité haya un
    republicano. **Respuesta:** Se busca la probabilidad marginal de que
    el comité contenga exactamente un republicano ($X=1$) $Y$:
    $$P(X=1) = f_X(1) = f_{XY}(1,0) + f_{XY}(1,1) + f_{XY}(1,2)$$
    $$P(X=1) = \frac{3}{15} + \frac{6}{15} + 0 = \frac{9}{15} = \frac{3}{5}$$
    La probabilidad de que en el comité haya un republicano es de
    $\frac{3}{5}$ (o $0.6$ / $60\%$).
-   **c)** Encuentre la probabilidad de que en el comité haya dos
    demócratas. **Respuesta:** Se busca la probabilidad marginal de que
    el comité contenga exactamente dos demócratas ($Y=2$) $X$:
    $$P(Y=2) = f_Y(2) = f_{XY}(0,2) + f_{XY}(1,2) + f_{XY}(2,2)$$
    $$P(Y=2) = \frac{1}{15} + 0 + 0 = \frac{1}{15}$$ La probabilidad de
    que en el comité haya dos demócratas es de $\frac{1}{15}$ (o
    aproximadamente $6.67\%$).
-   **d)** Encuentre la probabilidad de que en el comité no haya
    demócratas dado que haya dos republicanos. **Respuestas:**
    $$P(Y=0 \mid X=2) = \frac{f_{XY}(2,0)}{f_X(2)}$$ Primero calculamos
    la probabilidad marginal $f_X(2)$:
    $$f_X(2) = f_{XY}(2,0) + f_{XY}(2,1) + f_{XY}(2,2) = \frac{3}{15} + 0 + 0 = \frac{3}{15}$$
    Sustituyendo en la fórmula condicional:
    $$P(Y=0 \mid X=2) = \frac{3/15}{3/15} = 1$$ La probabilidad de que
    no haya demócratas dado que hay dos republicanos es de 1 (o
    $100\%$).
-   **e)** Encuentre la probabilidad de que en el comité haya un
    republicano dado que haya un demócrata. **Respuesta:**
    $$P(X=1 \mid Y=1) = \frac{f_{XY}(1,1)}{f_Y(1)}$$ Primero calculamos
    la probabilidad marginal $f_Y(1)$ sumando la fila $Y=1$:
    $$f_Y(1) = f_{XY}(0,1) + f_{XY}(1,1) + f_{XY}(2,1) = \frac{2}{15} + \frac{6}{15} + 0 = \frac{8}{15}$$
    Sustituyendo en la fórmula de probabilidad condicional:
    $$P(X=1 \mid Y=1) = \frac{6/15}{8/15} = \frac{6}{8} = \frac{3}{4}$$
    La probabilidad de que haya un republicano dado que hay un demócrata
    es de $\frac{3}{4}$ (o $0.75$ / $75\%$).
-   **f)** ¿$X$ y $Y$ son independientes? ¿Por qué sí o por qué no?
    **Respuesta:** Para que $X$ y $Y$ sean independientes, debe
    cumplirse $f_{XY}(x,y) = f_X(x) \cdot f_Y(y)$ para todos los pares
    $(x,y)$. Evaluamos en el punto $(x=1, y=1)$:
-   Valor en la tabla: $f_{XY}(1,1) = \frac{6}{15} = 0.4$
-   Producto de marginales:
    $f_X(1) \cdot f_Y(1) = \left(\frac{9}{15}\right) \cdot \left(\frac{8}{15}\right) = \frac{72}{225} = \frac{24}{75} = 0.32$
    Dado que $f_{XY}(1,1) \neq f_X(1) \cdot f_Y(1)$ ($0.4 \neq 0.32$),
    la condición de independencia no se cumple. **No son
    independientes**. El número de republicanos y el de demócratas
    elegidos están relacionados, ya que el tamaño total del comité está
    limitado a dos personas.

------------------------------------------------------------------------

### 5.

A continuación, se m uestra la función de masa de probabilidad conjunta
sobre la población de departamentos en renta de Hong Kong donde $X$
representa la renta mensual de los departamentos e $Y$ representa el
tipo de departamento.

| Renta  Tipo                              | Público | Privado | Otros |
|:-----------------------------------------|:-------:|:-------:|:-----:|
| **Baja** $(\le 1\text{k})$               |  0.17   |  0.01   | 0.02  |
| **Media** $(1\text{k}, 5\text{k}]$       |  0.35   |  0.03   | 0.01  |
| **Media alta** $(5\text{k}, 12\text{k}]$ |  0.09   |  0.07   | 0.01  |
| **Alta** $(> 12\text{k})$                |    0    |  0.14   | 0.10  |

Calcule las siguientes probabilidades y dé una interpretación de los
resultados:

-   **a)** $P(X = \text{Media}, Y = \text{Privado})$
-   **b)** $P(X = \text{Baja}, Y = \text{Público})$
-   **c)** $P(Y = \text{Otros})$
-   **d)** $P(X = \text{Alta})$
-   **e)** $P(X = \text{Alta} \mid Y = \text{Privado})$
-   **f)** $P(Y = \text{Otros} \mid X = \text{Media alta})$
-   **g)** ¿El precio de la renta es independiente del tipo de
    departamento?

#### Respuesta:

Primero verificamos que la tabla es una función de masa válida sumando
todas las celdas, lo cual da $1.00$.

-   **a)** $P(X = \text{Media}, Y = \text{Privado})$

Se lee directamente de la tabla, en el cruce de la fila Media y la
columna Privado:

$$\boxed{P(X = \text{Media}, Y = \text{Privado}) = 0.03}$$

Es la probabilidad de que un departamento elegido al azar tenga renta
media y sea de tipo privado.

-   **b)** $P(X = \text{Baja}, Y = \text{Público})$

$$\boxed{P(X = \text{Baja}, Y = \text{Público}) = 0.17}$$

Es la celda con mayor probabilidad de toda la tabla, la combinación
renta baja con departamento público concentra buena parte de la masa
de probabilidad.

-   **c)** $P(Y = \text{Otros})$

Sumamos la columna Otros (marginal de $Y$):

$$P(Y = \text{Otros}) = 0.02 + 0.01 + 0.01 + 0.10 = \boxed{0.14}$$

-   **d)** $P(X = \text{Alta})$

Sumamos la fila Alta (marginal de $X$):

$$P(X = \text{Alta}) = 0 + 0.14 + 0.10 = \boxed{0.24}$$

-   **e)** $P(X = \text{Alta} \mid Y = \text{Privado})$

Primero obtenemos la marginal $P(Y=\text{Privado})$ sumando la columna
Privado:

$$P(Y = \text{Privado}) = 0.01 + 0.03 + 0.07 + 0.14 = 0.25$$

Sustituyendo en la fórmula condicional:

$$P(X = \text{Alta} \mid Y = \text{Privado}) = \frac{P(X=\text{Alta}, Y=\text{Privado})}{P(Y=\text{Privado})} = \frac{0.14}{0.25} = \boxed{0.56}$$

-   **f)** $P(Y = \text{Otros} \mid X = \text{Media alta})$

Primero obtenemos la marginal $P(X=\text{Media alta})$ sumando la fila
Media alta:

$$P(X = \text{Media alta}) = 0.09 + 0.07 + 0.01 = 0.17$$

Sustituyendo en la fórmula condicional:

$$P(Y = \text{Otros} \mid X = \text{Media alta}) = \frac{P(X=\text{Media alta}, Y=\text{Otros})}{P(X=\text{Media alta})} = \frac{0.01}{0.17} \approx \boxed{0.0588}$$

-   **g)** ¿El precio de la renta es independiente del tipo de
    departamento?

Para que $X$ y $Y$ sean independientes, debe cumplirse
$f_{XY}(x,y) = f_X(x)\cdot f_Y(y)$ para todo par $(x,y)$. Con las
marginales completas:

$$f_X: \quad \text{Baja}=0.20,\ \text{Media}=0.39,\ \text{Media alta}=0.17,\ \text{Alta}=0.24$$

$$f_Y: \quad \text{Público}=0.61,\ \text{Privado}=0.25,\ \text{Otros}=0.14$$

Basta un contraejemplo para descartar la independencia. Evaluamos en
$(X=\text{Baja}, Y=\text{Público})$:

$$f_X(\text{Baja})\cdot f_Y(\text{Público}) = 0.20 \cdot 0.61 = 0.122$$

Como $f_{XY}(\text{Baja},\text{Público}) = 0.17 \neq 0.122$, la
condición no se cumple.

$$\boxed{\text{No, el precio de la renta NO es independiente del tipo de departamento}}$$

Tiene sentido en el contexto del problema: los departamentos públicos
tienden sistemáticamente a tener rentas más bajas, así que el tipo de
departamento y su precio están asociados.

------------------------------------------------------------------------

### 6.

Sean $X$ e $Y$ variables aleatorias continuas con función de densidad de
probabilidad conjunta:

$$
f_{XY}(x,y) = \begin{cases} \frac{1}{2}x + \frac{3}{2}y, & 0 \le x \le 1, \, 0 \le y \le 1 \\ 0, & \text{otros} \end{cases}
$$

Determine:

-   **a)** Determine la función de distribución acumulada $F(x,y)$.

Para encontrar la distribución acumulada conjunta, integramos la función
de densidad $f_{XY}(u,v)$ respecto a $u$ desde $0$ hasta $x$, y respecto
a $v$ desde $0$ hasta $y$:

$$
F_{XY}(x,y) = \int_0^y \int_0^x \left( \frac{1}{2}u + \frac{3}{2}v \right) \,du\,dv
$$

$$
= \int_0^y \left[ \frac{1}{4}u^2 + \frac{3}{2}vu \right]_0^x \,dv = \int_0^y \left( \frac{1}{4}x^2 + \frac{3}{2}vx \right) \,dv
$$

$$
= \left[ \frac{1}{4}x^2v + \frac{3}{4}xv^2 \right]_0^y = \frac{1}{4}x^2y + \frac{3}{4}xy^2
$$

$$
\boxed{F_{XY}(x,y) = \frac{1}{4}x^2y + \frac{3}{4}xy^2} \quad \text{para } 0 \le x \le 1, \, 0 \le y \le 1
$$

------------------------------------------------------------------------

-   **b)** Determine las funciones de densidad de probabilidad marginal
    para $X$ e $Y$.

Para la marginal de $X$, integramos la función conjunta respecto a $y$
en su dominio de $0$ a $1$:

$$
f_X(x) = \int_0^1 \left( \frac{1}{2}x + \frac{3}{2}y \right) \,dy = \left[ \frac{1}{2}xy + \frac{3}{4}y^2 \right]_0^1 = \frac{1}{2}x + \frac{3}{4}
$$

$$
\boxed{f_X(x) = \frac{1}{2}x + \frac{3}{4}} \quad \text{para } 0 \le x \le 1
$$

Para la marginal de $Y$, integramos la función conjunta respecto a $x$
en su dominio de $0$ a $1$:

$$
f_Y(y) = \int_0^1 \left( \frac{1}{2}x + \frac{3}{2}y \right) \,dx = \left[ \frac{1}{4}x^2 + \frac{3}{2}xy \right]_0^1 = \frac{1}{4} + \frac{3}{2}y
$$

$$
\boxed{f_Y(y) = \frac{1}{4} + \frac{3}{2}y} \quad \text{para } 0 \le y \le 1
$$

------------------------------------------------------------------------

-   **c)** Determine las funciones de densidad de probabilidad
    condicional de $X$ e $Y$.

Usamos la definición de probabilidad condicional
$f_{X|Y}(x|y) = \frac{f_{XY}(x,y)}{f_Y(y)}$. Para $X$ dado $Y$:

$$
f_{X|Y}(x|y) = \frac{\frac{1}{2}x + \frac{3}{2}y}{\frac{1}{4} + \frac{3}{2}y}
$$

Multiplicando el numerador y el denominador por $4$ para simplificar la
fracción:

$$
\boxed{f_{X|Y}(x|y) = \frac{2x + 6y}{1 + 6y}}
$$

Para $Y$ dado $X$, la fórmula es
$f_{Y|X}(y|x) = \frac{f_{XY}(x,y)}{f_X(x)}$:

$$
f_{Y|X}(y|x) = \frac{\frac{1}{2}x + \frac{3}{2}y}{\frac{1}{2}x + \frac{3}{4}}
$$

Multiplicando el numerador y el denominador por $4$:

$$
\boxed{f_{Y|X}(y|x) = \frac{2x + 6y}{2x + 3}}
$$

------------------------------------------------------------------------

-   **d)** Determine si las variables aleatorias son independientes.

Dos variables son independientes si y solo si su función de densidad
conjunta es igual al producto de sus funciones marginales:
$f_{XY}(x,y) = f_X(x)f_Y(y)$. Multiplicamos las marginales obtenidas en
el inciso b:

$$
f_X(x)f_Y(y) = \left( \frac{1}{2}x + \frac{3}{4} \right) \left( \frac{1}{4} + \frac{3}{2}y \right)
$$

$$
= \frac{1}{8}x + \frac{3}{4}xy + \frac{3}{16} + \frac{9}{8}y
$$

Como el producto de las marginales no es idéntico a la función de
densidad conjunta original $\left(\frac{1}{2}x + \frac{3}{2}y\right)$:

$$
\boxed{\text{Las variables } X \text{ e } Y \text{ NO son independientes}}
$$

------------------------------------------------------------------------

### 7.

Un sistema electrónico tiene uno de cada dos tipos diferentes de
componentes de operación en operación conjunta. Denote con $X$ y $Y$ las
duraciones aleatorias de los componentes del tipo I y tipo II
respectivamente. La función de densidad de probabilidad conjunta está
dada por:

$$
f_{XY}(x,y) = \begin{cases} \frac{1}{8} x e^{-(x+y)/2}, & x > 0, \, y > 0 \\ 0, & \text{otros} \end{cases}
$$

*(Las mediciones son en cientos de horas).*

-   **a)** Encuentre $P(X > 1, Y > 1)$.

Para calcular esta probabilidad, integramos la función de densidad
conjunta en la región $x > 1$ y $y > 1$. Como el exponente se puede
separar ($e^{-(x+y)/2} = e^{-x/2}e^{-y/2}$), podemos dividir la integral
doble en el producto de dos integrales simples:

$$
P(X > 1, Y > 1) = \int_1^\infty \int_1^\infty \frac{1}{8} x e^{-(x+y)/2} \,dy\,dx = \frac{1}{8} \left( \int_1^\infty x e^{-x/2} \,dx \right) \left( \int_1^\infty e^{-y/2} \,dy \right)
$$

Resolvemos primero la integral respecto a $y$:

$$
\int_1^\infty e^{-y/2} \,dy = \left[ -2e^{-y/2} \right]_1^\infty = 0 - \left(-2e^{-1/2}\right) = 2e^{-1/2}
$$

Ahora resolvemos la integral respecto a $x$ usando integración por
partes ($u = x$, $dv = e^{-x/2}dx \implies du = dx$, $v = -2e^{-x/2}$):

$$
\int_1^\infty x e^{-x/2} \,dx = \left[ -2x e^{-x/2} \right]_1^\infty - \int_1^\infty -2e^{-x/2} \,dx
$$

Evaluamos el primer término (el límite en infinito es $0$ aplicando
L'Hôpital) y resolvemos la segunda integral:

$$
= \left( 0 - (-2(1)e^{-1/2}) \right) + \left[ -4e^{-x/2} \right]_1^\infty = 2e^{-1/2} + \left( 0 - (-4e^{-1/2}) \right)
$$

$$
= 2e^{-1/2} + 4e^{-1/2} = 6e^{-1/2}
$$

Sustituimos ambos resultados en la expresión inicial:

$$
P(X > 1, Y > 1) = \frac{1}{8} \cdot \left( 6e^{-1/2} \right) \cdot \left( 2e^{-1/2} \right) = \frac{12}{8} e^{-1} = \frac{3}{2}e^{-1}
$$

$$
\boxed{P(X > 1, Y > 1) = \frac{3}{2e}}
$$

------------------------------------------------------------------------

-   **b)** Encuentre la probabilidad de que el componente tipo II tenga
    una vida útil de más de 200 horas.

Dado que las mediciones están en cientos de horas, $200$ horas equivalen
a $y = 2$. Nos piden encontrar $P(Y > 2)$, lo que implica integrar $y$
desde $2$ hasta infinito, y evaluar $x$ en todo su dominio válido (desde
$0$ hasta infinito):

$$
P(Y > 2) = \int_2^\infty \int_0^\infty \frac{1}{8} x e^{-(x+y)/2} \,dx\,dy = \frac{1}{8} \left( \int_0^\infty x e^{-x/2} \,dx \right) \left( \int_2^\infty e^{-y/2} \,dy \right)
$$

Resolvemos la integral respecto a $x$ (con los nuevos límites $0$ a
$\infty$), utilizando el resultado de integración por partes que
obtuvimos en el inciso anterior:

$$
\int_0^\infty x e^{-x/2} \,dx = \left[ -2x e^{-x/2} \right]_0^\infty - \left[ 4e^{-x/2} \right]_0^\infty
$$

$$
= (0 - 0) - (0 - 4e^0) = 4
$$

Ahora resolvemos la integral respecto a $y$ desde $2$ hasta $\infty$:

$$
\int_2^\infty e^{-y/2} \,dy = \left[ -2e^{-y/2} \right]_2^\infty = 0 - \left(-2e^{-2/2}\right) = 2e^{-1}
$$

Sustituimos ambos valores en la expresión principal:

$$
P(Y > 2) = \frac{1}{8} \cdot (4) \cdot \left( 2e^{-1} \right) = \frac{8}{8} e^{-1} = e^{-1}
$$

$$
\boxed{P(Y > 2) = \frac{1}{e}}
$$

------------------------------------------------------------------------

### 8.

Sean $X$ e $Y$ variables aleatorias continuas con función de densidad de
probabilidad conjunta:

$$
f_{XY}(x,y) = \begin{cases} \frac{1}{4}(1 + xy(x^2 - y^2)), & -1 \le x \le 1, \, -1 \le y \le 1 \\ 0, & \text{otros} \end{cases}
$$

Determine: - **a)** La función de distribución acumulada. - **b)** Las
funciones de densidad de probabilidad marginal para $X$ e $Y$. - **c)**
Las funciones de densidad de probabilidad condicional de $X$ e $Y$. -
**d)** Si las variables aleatorias son independientes.

#### Respuesta:

Nota estructural: el término $xy(x^2-y^2) = x^3y - xy^3$ es impar tanto
en $x$ como en $y$ por separado, lo cual simplifica el cálculo de las
marginales.

-   **a)** La función de distribución acumulada.

Por definición:

$$F(x,y) = \int_{-1}^{x}\int_{-1}^{y} \frac{1}{4}\left(1+s^3t-st^3\right) dt\,ds$$

Resolvemos primero la integral interna respecto a $t$ (con $s$ fija):

$$\int_{-1}^{y}\frac{1}{4}\left(1+s^3t-st^3\right)dt = \frac{1}{4}\left[t+\frac{s^3t^2}{2}-\frac{st^4}{4}\right]_{-1}^{y}$$

Evaluando en $t=y$ y restando lo evaluado en $t=-1$ (recordando que
$(-1)^2=1$ y $(-1)^4=1$):

$$= \frac{1}{4}\left[(y+1)+\frac{s^3}{2}(y^2-1)-\frac{s}{4}(y^4-1)\right]$$

Ahora integramos este resultado respecto a $s$, de $-1$ a $x$:

$$F(x,y) = \frac{1}{4}\int_{-1}^{x}\left[(y+1)+\frac{s^3}{2}(y^2-1)-\frac{s}{4}(y^4-1)\right]ds$$

$$= \frac{1}{4}\left[(y+1)s+\frac{(y^2-1)s^4}{8}+\frac{(1-y^4)s^2}{8}\right]_{-1}^{x}$$

Evaluando en $s=x$ y restando lo evaluado en $s=-1$:

$$= \frac{1}{4}\left[(x+1)(y+1)+\frac{(y^2-1)(x^4-1)}{8}+\frac{(1-y^4)(x^2-1)}{8}\right]$$

Repartiendo el $\frac{1}{4}$ y simplificando el último signo:

$$\boxed{F(x,y) = \frac{(x+1)(y+1)}{4} + \frac{(x^4-1)(y^2-1)-(x^2-1)(y^4-1)}{32}} \quad \text{para } -1\le x\le 1,\ -1\le y\le 1$$

Como verificación, en $x=1$ el segundo bloque se anula (por los
factores $x^4-1$ y $x^2-1$), quedando $F(1,y)=\frac{y+1}{2}$, que
coincide con la acumulada de la marginal de $Y$.

------------------------------------------------------------------------

-   **b)** Las funciones de densidad de probabilidad marginal para $X$
    e $Y$.

$$f_X(x) = \int_{-1}^{1}\frac{1}{4}\left(1+x^3y-xy^3\right)dy = \frac{1}{4}\left[\int_{-1}^{1}1\,dy + x^3\int_{-1}^{1}y\,dy - x\int_{-1}^{1}y^3\,dy\right]$$

Resolvemos cada integral por separado:

$$\int_{-1}^{1}1\,dy = \big[y\big]_{-1}^{1} = 1-(-1) = 2$$

$$\int_{-1}^{1}y\,dy = \left[\frac{y^2}{2}\right]_{-1}^{1} = \frac{1}{2}-\frac{1}{2} = 0$$

$$\int_{-1}^{1}y^3\,dy = \left[\frac{y^4}{4}\right]_{-1}^{1} = \frac{1}{4}-\frac{1}{4} = 0$$

Las últimas dos se anulan porque $y$ y $y^3$ son funciones impares
integradas en un intervalo simétrico $[-1,1]$: el área que se acumula
del lado positivo se cancela exactamente con la del lado negativo.
Entonces:

$$f_X(x) = \frac{1}{4}\big[2+x^3(0)-x(0)\big] = \boxed{\frac{1}{2}} \quad \text{para } -1\le x\le 1$$

Por el mismo argumento (ahora $x$ y $x^3$ son las funciones impares),
al integrar respecto a $x$:

$$f_Y(y) = \int_{-1}^{1}\frac{1}{4}\left(1+x^3y-xy^3\right)dx = \frac{1}{4}\big[2+y(0)-y^3(0)\big] = \boxed{\frac{1}{2}} \quad \text{para } -1\le y\le 1$$

Ambas marginales resultan uniformes en $[-1,1]$. Esto no implica
independencia, ya que el término cruzado desaparece al integrar sobre
todo el rango pero sigue presente en la densidad conjunta.

------------------------------------------------------------------------

-   **c)** Las funciones de densidad de probabilidad condicional de
    $X$ e $Y$.

Usando $f_{X|Y}(x|y) = \dfrac{f_{XY}(x,y)}{f_Y(y)}$ y sustituyendo
$f_Y(y)=\frac{1}{2}$:

$$f_{X|Y}(x|y) = \frac{\frac{1}{4}(1+x^3y-xy^3)}{\frac{1}{2}} = \boxed{\frac{1}{2}\left(1+x^3y-xy^3\right)} \quad \text{para } -1\le x\le 1$$

De forma análoga, usando $f_{Y|X}(y|x) = \dfrac{f_{XY}(x,y)}{f_X(x)}$
y sustituyendo $f_X(x)=\frac{1}{2}$:

$$f_{Y|X}(y|x) = \frac{\frac{1}{4}(1+x^3y-xy^3)}{\frac{1}{2}} = \boxed{\frac{1}{2}\left(1+x^3y-xy^3\right)} \quad \text{para } -1\le y\le 1$$

Ambas comparten la misma expresión algebraica porque la densidad
conjunta es antisimétrica al intercambiar $x$ por $y$
($xy(x^2-y^2)$ cambia de signo), pero cada una varía respecto a una
variable distinta con la otra fija.

Como verificación, cada condicional integra a $1$ sobre su rango, por
ejemplo:

$$\int_{-1}^{1} f_{X|Y}(x|y)\,dx = \frac{1}{2}\int_{-1}^{1}\left(1+x^3y-xy^3\right)dx = \frac{1}{2}(2+0-0) = 1$$

------------------------------------------------------------------------

-   **d)** Si las variables aleatorias son independientes.

Dos variables continuas son independientes si y solo si
$f_{XY}(x,y) = f_X(x)\cdot f_Y(y)$ para todo el dominio. Con las
marginales obtenidas:

$$f_X(x)\cdot f_Y(y) = \frac{1}{2}\cdot\frac{1}{2} = \frac{1}{4} \quad \text{(constante)}$$

Mientras que la densidad conjunta sí depende de $x$ y $y$:

$$f_{XY}(x,y) = \frac{1}{4}\left(1+x^3y-xy^3\right)$$

Evaluamos en un punto de contraejemplo, $x=1,\ y=0.5$:

$$f_{XY}(1,0.5) = \frac{1}{4}\left(1+0.5-0.125\right) = \frac{1}{4}(1.375) = 0.34375$$

$$f_X(1)\cdot f_Y(0.5) = \frac{1}{2}\cdot\frac{1}{2} = 0.25$$

Como $0.34375 \neq 0.25$:

$$\boxed{\text{Las variables } X \text{ e } Y \text{ NO son independientes}}$$

*(Este ejercicio muestra que marginales uniformes o "simples" no
garantizan independencia: toda la dependencia está codificada en el
término cruzado $xy(x^2-y^2)$, que se cancela al marginalizar pero
reaparece al evaluar la densidad conjunta en un punto específico).*

------------------------------------------------------------------------

### 9.

La administración en un restaurante de comida rápida está interesada en
el comportamiento conjunto de las variables aleatorias $X$ y $Y$. $X$
representa el tiempo total entre la llegada de un cliente a la tienda y
la salida de la ventanilla de servicio; $Y$, el tiempo que un cliente
espera en la fila antes de llegar a la ventanilla de servicio. Como $X$
incluye el tiempo que un cliente espera en la fila, debemos tener
$X \ge Y$. La distribución de valores observados puede ser modelada por
la siguiente función de densidad de probabilidad conjunta:

$$
f_{XY}(x,y) = \begin{cases} e^{-x}, & 0 \le y \le x < \infty \\ 0, & \text{otros} \end{cases}
$$

*(con el tiempo medido en minutos).*

Encuentre:

-   **a)** Encuentre $P(X < 2, Y > 1)$.

Para encontrar esta probabilidad, debemos integrar la función de
densidad conjunta sobre la región de interés. Las condiciones dadas son
$X < 2$ y $Y > 1$. Además, la función conjunta nos indica que el soporte
natural es $0 \le y \le x$.

Combinando estas restricciones, obtenemos los límites de integración:
$1 < y \le x < 2$. Podemos plantear la integral doble integrando primero
respecto a $y$ (desde $1$ hasta $x$) y luego respecto a $x$ (desde $1$
hasta $2$):

$$
P(X < 2, Y > 1) = \int_1^2 \int_1^x e^{-x} \,dy\,dx
$$

Resolvemos primero la integral interna respecto a $y$ (tratando a $x$
como constante):

$$
\int_1^x e^{-x} \,dy = e^{-x} \Big[ y \Big]_1^x = e^{-x} (x - 1)
$$

Ahora sustituimos este resultado en la integral externa y resolvemos
respecto a $x$:

$$
\int_1^2 (x - 1)e^{-x} \,dx
$$

Aplicamos integración por partes. Sea $u = x - 1$ y $dv = e^{-x}dx$.
Entonces $du = dx$ y $v = -e^{-x}$:

$$
\int (x - 1)e^{-x} \,dx = -(x - 1)e^{-x} - \int -e^{-x} \,dx = -(x - 1)e^{-x} - e^{-x}
$$

Factorizando el resultado:

$$
= e^{-x} \big[ -(x - 1) - 1 \big] = e^{-x} (-x + 1 - 1) = -xe^{-x}
$$

Evaluamos en los límites de $1$ a $2$:

$$
\Big[ -xe^{-x} \Big]_1^2 = (-2e^{-2}) - (-1e^{-1}) = e^{-1} - 2e^{-2}
$$

$$
\boxed{P(X < 2, Y > 1) = \frac{1}{e} - \frac{2}{e^2} \approx 0.0972}
$$

------------------------------------------------------------------------

-   **b)** Las funciones de densidad marginal para $X$ y $Y$.

Para la **marginal de** $X$, integramos la función conjunta respecto a
$y$ sobre su dominio válido. Dado un valor $x$, $y$ varía desde $0$
hasta $x$:

$$
f_X(x) = \int_0^x e^{-x} \,dy = e^{-x} \Big[ y \Big]_0^x = x e^{-x}
$$

$$
\boxed{f_X(x) = x e^{-x}} \quad \text{para } x \ge 0
$$

Para la **marginal de** $Y$, integramos la función conjunta respecto a
$x$ sobre su dominio válido. Dado un valor $y$, $x$ varía desde $y$
hasta infinito:

$$
f_Y(y) = \int_y^\infty e^{-x} \,dx = \Big[ -e^{-x} \Big]_y^\infty = 0 - (-e^{-y}) = e^{-y}
$$

$$
\boxed{f_Y(y) = e^{-y}} \quad \text{para } y \ge 0
$$

------------------------------------------------------------------------

-   **c)** ¿Cuál es la función de densidad condicional de $X$ dado que
    $Y = y$?

Utilizamos la fórmula de probabilidad condicional
$f_{X|Y}(x|y) = \frac{f_{XY}(x,y)}{f_Y(y)}$:

$$
f_{X|Y}(x|y) = \frac{e^{-x}}{e^{-y}} = e^{-x} \cdot e^y = e^{-(x-y)}
$$

$$
\boxed{f_{X|Y}(x|y) = e^{-(x-y)}} \quad \text{para } x \ge y
$$

*(Nota: El dominio es* $x \ge y$ porque si ya sabemos que el cliente
esperó $y$ minutos, su tiempo total $X$ no puede ser menor que $y$).

------------------------------------------------------------------------

-   **d)** ¿Cuál es la función de densidad condicional de $Y$ dado que
    $X = x$?

Utilizamos la fórmula $f_{Y|X}(y|x) = \frac{f_{XY}(x,y)}{f_X(x)}$:

$$
f_{Y|X}(y|x) = \frac{e^{-x}}{x e^{-x}} = \frac{1}{x}
$$

$$
\boxed{f_{Y|X}(y|x) = \frac{1}{x}} \quad \text{para } 0 \le y \le x
$$

*(Nota: Esto significa que si sabemos que el tiempo total fue* $x$, el
tiempo de espera $y$ sigue una distribución uniforme continua entre $0$
y $x$).

------------------------------------------------------------------------

-   **e)** ¿La función de densidad condicional que obtuvo en el inciso c
    es la misma que la función de densidad marginal hallada en el inciso
    b?

Comparamos los resultados obtenidos en c) y b): \* Marginal de $X$:
$f_X(x) = x e^{-x}$ \* Condicional de $X|Y$: $f_{X|Y}(x|y) = e^{-(x-y)}$

$$
\boxed{\text{No, las funciones de densidad no son la misma.} \quad x e^{-x} \neq e^{-(x-y)}}
$$

------------------------------------------------------------------------

-   **f)** ¿Qué implica su respuesta del inciso e?

En teoría de probabilidad, si la distribución condicional de una
variable depende de la otra (es decir, $f_{X|Y}(x|y) \neq f_X(x)$),
significa que el conocimiento de una variable altera la probabilidad de
ocurrencia de la otra.

$$
\boxed{\text{Implica que las variables aleatorias } X \text{ e } Y \text{ NO son independientes (son variables dependientes).}}
$$

------------------------------------------------------------------------

------------------------------------------------------------------------

### 10.

Considere la función de densidad de probabilidad conjunta de $X$, la
proporción de la capacidad de un tanque que ha sido abastecido al
principio de la semana, y $Y$, la proporción de la capacidad vendida
durante la semana:

$$
f_{XY}(x,y) = \begin{cases} 3x, & 0 \le y \le x \le 1 \\ 0, & \text{otros} \end{cases}
$$

-   **a)** Encuentre
    $P\left(X \le \frac{1}{2}, Y \le \frac{1}{3}\right)$

Para calcular esta probabilidad, debemos integrar la función de densidad
conjunta $f_{XY}(x,y) = 3x$ sobre la región dada por las condiciones
$X \le 1/2$ y $Y \le 1/3$. Además, debemos respetar la restricción del
dominio original $0 \le y \le x \le 1$.

Podemos plantear esto integrando primero respecto a $x$ y luego respecto
a $y$. \* La variable $y$ variará desde $0$ hasta su límite máximo
exigido: $1/3$. \* Para un valor dado de $y$, la variable $x$ debe ser
mayor o igual a $y$ (por el dominio) y menor o igual a $1/2$ (por la
condición). Por lo tanto, $x$ varía desde $y$ hasta $1/2$.

$$
P\left(X \le \frac{1}{2}, Y \le \frac{1}{3}\right) = \int_0^{1/3} \int_y^{1/2} 3x \,dx\,dy
$$

Resolvemos la integral interna respecto a $x$:

$$
\int_y^{1/2} 3x \,dx = \left[ \frac{3}{2}x^2 \right]_y^{1/2} = \frac{3}{2}\left(\frac{1}{2}\right)^2 - \frac{3}{2}(y)^2 = \frac{3}{8} - \frac{3}{2}y^2
$$

Sustituimos este resultado en la integral externa y resolvemos respecto
a $y$:

$$
\int_0^{1/3} \left( \frac{3}{8} - \frac{3}{2}y^2 \right) \,dy = \left[ \frac{3}{8}y - \frac{3}{2} \cdot \frac{y^3}{3} \right]_0^{1/3} = \left[ \frac{3}{8}y - \frac{1}{2}y^3 \right]_0^{1/3}
$$

Evaluamos en los límites:

$$
= \left( \frac{3}{8}\left(\frac{1}{3}\right) - \frac{1}{2}\left(\frac{1}{3}\right)^3 \right) - 0 = \frac{1}{8} - \frac{1}{2}\left(\frac{1}{27}\right) = \frac{1}{8} - \frac{1}{54}
$$

Para restar, buscamos un denominador común (216):

$$
= \frac{27}{216} - \frac{4}{216} = \frac{23}{216}
$$

$$
\boxed{P\left(X \le \frac{1}{2}, Y \le \frac{1}{3}\right) = \frac{23}{216}}
$$

------------------------------------------------------------------------

-   **b)** Encuentre $P\left(Y \le \frac{1}{2}X\right)$, la probabilidad
    de que la cantidad vendida sea menor que la mitad de la cantidad
    comprada.

Como $\frac{x}{2} < x$ para todo $x > 0$, la condición
$y \le \frac{x}{2}$ ya implica $y \le x$, así que la región es
simplemente $0 \le y \le \frac{x}{2}$ y $0 \le x \le 1$:

$$
P\left(Y \le \frac{X}{2}\right) = \int_0^1 \int_0^{x/2} 3x \,dy\,dx
$$

Resolvemos la integral respecto a $y$:

$$
= \int_0^1 3x \Big[ y \Big]_0^{x/2} \,dx = \int_0^1 3x \left( \frac{x}{2} \right) \,dx = \int_0^1 \frac{3}{2}x^2 \,dx
$$

Resolvemos la integral respecto a $x$:

$$
= \frac{3}{2} \left[ \frac{x^3}{3} \right]_0^1 = \frac{3}{2} \left( \frac{1}{3} \right) = \frac{1}{2}
$$

$$
\boxed{P\left(Y \le \frac{X}{2}\right) = \frac{1}{2}}
$$

------------------------------------------------------------------------

-   **c)** ¿Serán $X$ y $Y$ independientes?

Para que dos variables sean independientes, debe cumplirse que
$f_{XY}(x,y) = f_X(x)f_Y(y)$ para todo el dominio. Primero encontramos
las densidades marginales.

**Marginal de** $X$: Para un $x$ dado, $y$ varía de $0$ a $x$. $$
f_X(x) = \int_0^x 3x \,dy = 3x \Big[ y \Big]_0^x = 3x^2 \quad \text{para } 0 \le x \le 1
$$

**Marginal de** $Y$: Para un $y$ dado, $x$ varía de $y$ a $1$. $$
f_Y(y) = \int_y^1 3x \,dx = \left[ \frac{3}{2}x^2 \right]_y^1 = \frac{3}{2}(1 - y^2) \quad \text{para } 0 \le y \le 1
$$

Ahora comprobamos el producto: $$
f_X(x)f_Y(y) = (3x^2)\left[ \frac{3}{2}(1 - y^2) \right] = \frac{9}{2}x^2(1 - y^2)
$$

Como $f_X(x)f_Y(y) \neq 3x$ (que es nuestra función conjunta original):

$$
\boxed{\text{No, las variables } X \text{ e } Y \text{ NO son independientes.}}
$$

*(Regla general rápida: Si el soporte (dominio válido) de la función
conjunta depende de una variable en función de la otra, como*
$0 \le y \le x$, las variables nunca pueden ser independientes).