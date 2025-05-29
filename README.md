# Proyecto de Clase: Sistema de Optimización de Rutas  
**Materia:** Estructuras de Datos y Análisis de Algoritmos  
**Semestre:** 2025-1  
**Universidad:** Universidad Industrial de Santander (UIS)  
**Grupo:** E1  
**Docente:** Nury Farelo

## 👥 Integrantes del Grupo:
- Juan Daniel Torres Ramirez - 2240082  
- Juan David Mejia Fragoso - 2240085  
- Miguel Angel Aguilar Rodriguez - 2240030  
- Sebastián Nossa Agudelo - 2211555  

---

## 1. Introducción
En el ámbito de la computación, la optimización de rutas es fundamental en logística, transporte y navegación. Este proyecto desarrolla un sistema de optimización de rutas utilizando diferentes estructuras de datos (listas, árboles y grafos) con el fin de comparar su eficiencia, escalabilidad y aplicabilidad a redes reales.

---

## 2. Objetivo General
Diseñar e implementar un sistema que permita encontrar rutas óptimas entre diferentes ubicaciones en una red, aplicando y evaluando distintas estructuras de datos y algoritmos asociados a listas, árboles y grafos.

---

## 3. Entregas Parciales

### 📌 Entrega 1: Implementación con Listas Enlazadas
- Representación con listas doblemente enlazadas.
- Búsqueda recursiva con backtracking.
- Estructura simple pero poco eficiente en redes grandes.
- Uso de `merge sort` para organizar nodos y rutas.

### 📌 Entrega 2: Implementación con Árboles (`bigtree`)
- Representación jerárquica por subárboles de rutas.
- Búsqueda del camino mínimo prealmacenado por distancia acumulada.
- Consulta interactiva en consola.
- Eficiencia mejorada, pero estructura poco flexible para redes con ciclos.

### 📌 Entrega 3: Implementación con Grafos (`dict` + `Dijkstra`)
- Representación de red como grafo dirigido.
- Algoritmo de Dijkstra para hallar caminos mínimos.
- Visualización gráfica con `networkx`.
- Altamente eficiente y flexible, ideal para redes complejas.

---

## 4. Comparación de Implementaciones

| Criterio                      | Listas Enlazadas           | Árboles (`bigtree`)             | Grafos (`dict + Dijkstra`)       |
|-------------------------------|----------------------------|---------------------------------|----------------------------------|
| Tipo de red soportada         | Secuencial/simple          | Jerárquica                 | Compleja, con ciclos y múltiples rutas |
|Complejidad de búsqueda        | 𝒪(n!)                      | 𝒪(k) *(k = rutas cargadas)*    | 𝒪((V + E) log V)                |
| Escalabilidad                 | Baja                       | Media                           | Alta                             |
| Flexibilidad estructural      | Limitada                   | Moderada                        | Alta                             |
| Algoritmo de búsqueda         | Recursivo por fuerza bruta | Recorrido por caminos precalculados | Dijkstra (heap)              |
| Visualización incluida        | No                         | Parcial (`vshow()`)             | Completa (`networkx`)            |

> **Nota:** En la complejidad de Dijkstra, `V` representa el número de nodos (ubicaciones) y `E` el número de aristas (rutas entre ubicaciones).

---

## 5. Conclusiones Finales

- La implementación con **listas enlazadas** tiene una complejidad **exponencial (𝒪(n!))** en el peor caso, debido a que explora todos los caminos posibles de forma recursiva sin optimización.
- La implementación con **árboles** mejora en tiempo al utilizar **distancias precalculadas**, haciendo que la búsqueda sea casi constante: **𝒪(k)**, donde *k* es el número de rutas posibles desde un nodo.
- La implementación con **grafos y Dijkstra** ofrece la mejor eficiencia: **𝒪((V + E) log V)** gracias al uso de colas de prioridad, lo que la hace ideal para redes grandes y complejas.

> **Conclusión general:** A medida que aumentó la complejidad estructural (de listas a grafos), la eficiencia computacional del sistema mejoró notablemente. Esto evidencia cómo la selección adecuada de estructuras y algoritmos es clave para resolver problemas reales de forma óptima.
---

