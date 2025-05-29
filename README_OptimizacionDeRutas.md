
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
| Tipo de red soportada         | Secuencial/simple          | Jerárquica                      | Compleja, con ciclos y múltiples rutas |
| Eficiencia de búsqueda        | Muy baja (fuerza bruta)    | Alta (distancias precalculadas) | Muy alta (Dijkstra)             |
| Escalabilidad                 | Baja                       | Media                           | Alta                             |
| Flexibilidad estructural      | Limitada                   | Moderada                        | Alta                             |
| Facilidad de implementación   | Alta                       | Media                           | Media-baja                       |
| Visualización incluida        | No                         | Parcial (`vshow()`)             | Completa (`networkx`)            |

---

## 5. Conclusiones Finales

- La implementación con **listas** permitió introducir la lógica del problema, pero mostró ser ineficiente y poco escalable.
- Los **árboles** ofrecieron una mejora significativa en velocidad al estructurar rutas de forma jerárquica con distancias acumuladas.
- La solución más potente fue la basada en **grafos**, permitiendo representar cualquier tipo de red, encontrar rutas óptimas de forma eficiente con Dijkstra y visualizar el grafo completo.

> **Conclusión general:** La estructura de grafos fue la mejor opción en términos de eficiencia, escalabilidad y realismo para problemas de optimización de rutas. Este proyecto evidenció cómo la elección adecuada de la estructura de datos impacta profundamente en la solución de un problema computacional.

---
