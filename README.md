# Codeforces 453B — Little Pony and Harmony Chest

Implementación de una solución mediante **Programación Dinámica (DP) Top-Down con memoización** para el problema [453B de Codeforces](https://codeforces.com/problemset/problem/453/B).

## Descripción

El problema consiste en construir una secuencia de enteros positivos, coprimos de a pares, que minimice la suma de las diferencias absolutas respecto de una secuencia de entrada.

## Implementación

La solución utiliza:
- **Programación dinámica Top-Down:** descomposición del problema en subproblemas.
- **Memoización:** almacenamiento de estados previamente calculados.
- **Bitmasking:** representación eficiente de los factores primos utilizados.
- **Reconstrucción de soluciones:** obtención de una secuencia óptima a partir de los estados calculados.

## Análisis y experimentación

Se realizaron pruebas con distintos casos de entrada, incluyendo casos borde y secuencias de distintos tamaños. Además, se comparó el resultado con una implementación de fuerza bruta para validar la solución y se analizaron los tiempos de ejecución con y sin memoización.

## Tecnologías

- Python
- Programación Dinámica
- Análisis de complejidad algorítmica
- Matplotlib (visualización de resultados)

Proyecto desarrollado como parte de la asignatura **Análisis de Algoritmos**, Ingeniería Civil en Ciencia de Datos, PUCV.
