#Programa realizado para la segunda entrega del proyecto del proyecto de clase de la materia "Estructuras de Datos y Análisis de algoritmos" con la profesora Nury Farelo
#Hecho por: Juan Daniel Torres Ramirez <-> 2240082 ; Juan David Mejia Fragoso <-> 2240085 ; Miguel Angel <-> [CODIGO] ; Sebastian Nossa Agudelo <-> [2211555]
# 2025-1 || UIS || GRUPO: E1 || 27/04/2025

#****************************************************************************

#Se utilizará la libreria BigTree, lo que se plantea es hacer un arbol general el cual contenga todas las ubicaciones existentes y
#que cada nodo tenga como atributo a un arbol de rutas en el cual se planteran las rutas posibles desde esa ubicacion. Es en este lugar
#en donde se aplicaran algoritmos y tecnicas para hallar las rutas mas cortas y cumplir con el objetivo del proyecto -->: "Optimizar Rutas"

#****************************************************************************

#Importaciones
from bigtree import Node, find, find_name, find_path, find_relative_path, find_full_path, find_attr
import os

#Se definira un arbol general generico el cual se puede modificar a futuro, esto se hace para poder ejecutar el programa y tener una base
#En este caso, la raiz sera "PIEDECUESTA" (La utopia colombiana) :)
#No obstante, los arboles de rutas de cada nodo deberan ser declarados antes que el arbol general.

#A cada nodo le creamos sus arboles de rutas, esto para que cuando el usuario quiera elegir una ruta en especifico, el sistema compare y encuentre la ruta mas corta.
#**********************************************
#Para PIEDECUESTA (R0)
#Se definen los nodos
R0PIEDECUESTA = Node("R0PIEDECUESTA", distance = 0)
R0FLORIDABLANCA = Node("R0FLORIDABLANCA", parent=R0PIEDECUESTA, distance = 5)
R0BUCARAMANGA = Node("R0BUCARAMANGA", parent=R0FLORIDABLANCA, distance = (5+7))
R0GIRON = Node("R0GIRON", parent=R0BUCARAMANGA, distance = (5+7+4))
R0BOGOTA = Node("R0BOGOTA", parent=R0PIEDECUESTA, distance = (440))
R0MEDELLIN = Node("R0MEDELLIN", parent=R0BUCARAMANGA, distance = (5+7+4+400))
R0GUAJIRA = Node("R0GUAJIRA", parent=R0MEDELLIN, distance = (5+7+4+400+550)) #Vemos como se suman las distancias dependiendo de la trayectoria

#Relaciones padre e hijos
R0PIEDECUESTA.children = [R0BOGOTA, R0FLORIDABLANCA]
R0BUCARAMANGA.children = [R0GIRON, R0MEDELLIN]
R0FLORIDABLANCA.children = [R0BUCARAMANGA]
R0MEDELLIN.children = [R0GUAJIRA]

# Para PIEDECUESTA (R01) - Segunda opción
R01PIEDECUESTA = Node("R01PIEDECUESTA", distance=0)
R01BOGOTA = Node("R01BOGOTA", parent=R01PIEDECUESTA, distance=450)  #Ruta directa más larga
R01FLORIDABLANCA = Node("R01FLORIDABLANCA", parent=R01PIEDECUESTA, distance=6)  #Ruta ligeramente más larga
R01BUCARAMANGA = Node("R01BUCARAMANGA", parent=R01FLORIDABLANCA, distance=13)
R01GIRON = Node("R01GIRON", parent=R01BUCARAMANGA, distance=18)  #Ruta a Girón a través de Floridablanca y Bucaramanga
R01MEDELLIN = Node("R01MEDELLIN", parent=R01BUCARAMANGA, distance=420)  #Ruta a Medellín a través de Floridablanca y Bucaramanga
R01GUAJIRA = Node("R01GUAJIRA", parent=R01MEDELLIN, distance=970) #Ruta a la guajira

R01PIEDECUESTA.children = [R01BOGOTA, R01FLORIDABLANCA]
R01FLORIDABLANCA.children = [R01BUCARAMANGA]
R01BUCARAMANGA.children = [R01GIRON, R01MEDELLIN]
R01MEDELLIN.children = [R01GUAJIRA]
#**********************************************
#**********************************************
#Para FLORIDABLANCA (R1)
#Se definen los nodos
R1FLORIDABLANCA = Node("R1FLORIDABLANCA", distance=0)
R1PIEDECUESTA = Node("R1PIEDECUESTA", parent=R1FLORIDABLANCA, distance=5)
R1BUCARAMANGA = Node("R1BUCARAMANGA", parent=R1FLORIDABLANCA, distance=7)
R1GIRON = Node("R1GIRON", parent=R1BUCARAMANGA, distance=11)
R1MEDELLIN = Node("R1MEDELLIN", parent=R1BUCARAMANGA, distance=411)
R1GUAJIRA = Node("R1GUAJIRA", parent=R1MEDELLIN, distance=961)
R1BOGOTA = Node("R1BOGOTA", parent=R1PIEDECUESTA, distance=445) #Bogotá es accesible desde Piedecuesta

#Relaciones padre e hijos
R1FLORIDABLANCA.children = [R1PIEDECUESTA, R1BUCARAMANGA]
R1PIEDECUESTA.children = [R1BOGOTA] #Bogotá como hijo de Piedecuesta
R1BUCARAMANGA.children = [R1GIRON, R1MEDELLIN]
R1MEDELLIN.children = [R1GUAJIRA]

# Para FLORIDABLANCA (R11) - Segunda opción
R11FLORIDABLANCA = Node("R11FLORIDABLANCA", distance=0)
R11PIEDECUESTA = Node("R11PIEDECUESTA", parent=R11FLORIDABLANCA, distance=6)  #Ruta ligeramente más larga
R11BUCARAMANGA = Node("R11BUCARAMANGA", parent=R11FLORIDABLANCA, distance=8)  #Ruta ligeramente más larga
R11GIRON = Node("R11GIRON", parent=R11BUCARAMANGA, distance=16)  #Ruta a Girón a través de Bucaramanga
R11BOGOTA = Node("R11BOGOTA", parent=R11PIEDECUESTA, distance=450)  #Ruta a Bogotá a través de Piedecuesta
R11MEDELLIN = Node("R11MEDELLIN", parent=R11FLORIDABLANCA, distance=410) #Ruta directa a medellin
R11GUAJIRA = Node("R11GUAJIRA", parent=R11MEDELLIN, distance=960)

R11FLORIDABLANCA.children = [R11PIEDECUESTA, R11BUCARAMANGA, R11MEDELLIN]
R11PIEDECUESTA.children = [R11BOGOTA]
R11BUCARAMANGA.children = [R11GIRON]
R11MEDELLIN.children = [R11GUAJIRA]
#**********************************************
#**********************************************
#Para BUCARAMANGA (R2)
R2BUCARAMANGA = Node("R2BUCARAMANGA", distance=0)
R2FLORIDABLANCA = Node("R2FLORIDABLANCA", parent=R2BUCARAMANGA, distance=7)
R2GIRON = Node("R2GIRON", parent=R2BUCARAMANGA, distance=4)
R2MEDELLIN = Node("R2MEDELLIN", parent=R2BUCARAMANGA, distance=404)
R2GUAJIRA = Node("R2GUAJIRA", parent=R2MEDELLIN, distance=954)
R2PIEDECUESTA = Node("R2PIEDECUESTA", parent=R2FLORIDABLANCA, distance=12)
R2BOGOTA = Node("R2BOGOTA", parent=R2PIEDECUESTA, distance=452) #Bogotá accesible desde Piedecuesta (a través de Floridablanca)


R2BUCARAMANGA.children = [R2FLORIDABLANCA, R2GIRON, R2MEDELLIN]
R2FLORIDABLANCA.children = [R2PIEDECUESTA]
R2PIEDECUESTA.children = [R2BOGOTA] #Bogotá como hijo de Piedecuesta
R2MEDELLIN.children = [R2GUAJIRA]

# Para BUCARAMANGA (R21) - Segunda opción
R21BUCARAMANGA = Node("R21BUCARAMANGA", distance=0)
R21FLORIDABLANCA = Node("R21FLORIDABLANCA", parent=R21BUCARAMANGA, distance=8) #Ruta ligeramente mas larga
R21PIEDECUESTA = Node("R21PIEDECUESTA", parent=R21FLORIDABLANCA, distance=14) #Ruta a Piedecuesta por Floridablanca
R21GIRON = Node("R21GIRON", parent=R21BUCARAMANGA, distance=5) #Ruta ligeramente mas larga
R21BOGOTA = Node("R21BOGOTA", parent=R21PIEDECUESTA, distance=460) #Ruta a Bogota por Piedecuesta y Floridablanca
R21MEDELLIN = Node("R21MEDELLIN", parent=R21BUCARAMANGA, distance=400) #Ruta Directa y ligeramente mas corta
R21GUAJIRA = Node("R21GUAJIRA", parent=R21MEDELLIN, distance=950)

R21BUCARAMANGA.children = [R21FLORIDABLANCA, R21GIRON, R21MEDELLIN]
R21FLORIDABLANCA.children = [R21PIEDECUESTA]
R21PIEDECUESTA.children = [R21BOGOTA]
R21MEDELLIN.children = [R21GUAJIRA]
#**********************************************
#**********************************************
#Para GIRON
R3GIRON = Node("R3GIRON", distance=0)
R3PIEDECUESTA = Node("R3PIEDECUESTA", parent=R3GIRON, distance=16)
R3FLORIDABLANCA = Node("R3FLORIDABLANCA", parent=R3GIRON, distance=11)
R3BUCARAMANGA = Node("R3BUCARAMANGA", parent=R3GIRON, distance=4)
R3BOGOTA = Node("R3BOGOTA", parent=R3PIEDECUESTA, distance=456) #Bogotá a través de Piedecuesta
R3MEDELLIN = Node("R3MEDELLIN", parent=R3BUCARAMANGA, distance=408)
R3GUAJIRA = Node("R3GUAJIRA", parent=R3MEDELLIN, distance=958)

R3GIRON.children = [R3PIEDECUESTA, R3FLORIDABLANCA, R3BUCARAMANGA]
R3PIEDECUESTA.children = [R3BOGOTA]
R3BUCARAMANGA.children = [R3MEDELLIN]
R3MEDELLIN.children = [R3GUAJIRA]

# Para GIRON (R31) - Segunda opción
R31GIRON = Node("R31GIRON", distance=0)
R31PIEDECUESTA = Node("R31PIEDECUESTA", parent=R31GIRON, distance=17) #Ruta ligeramente mas larga
R31FLORIDABLANCA = Node("R31FLORIDABLANCA", parent=R31GIRON, distance=12) #Ruta ligeramente mas larga
R31BUCARAMANGA = Node("R31BUCARAMANGA", parent=R31GIRON, distance=5) #Ruta ligeramente mas larga
R31BOGOTA = Node("R31BOGOTA", parent=R31PIEDECUESTA, distance=460) #Ruta a Bogota por Piedecuesta
R31MEDELLIN = Node("R31MEDELLIN", parent=R31BUCARAMANGA, distance=410) #Ruta a Medellin por Bucaramanga
R31GUAJIRA = Node("R31GUAJIRA", parent=R31MEDELLIN, distance=960)

R31GIRON.children = [R31PIEDECUESTA, R31FLORIDABLANCA, R31BUCARAMANGA]
R31PIEDECUESTA.children = [R31BOGOTA]
R31BUCARAMANGA.children = [R31MEDELLIN]
R31MEDELLIN.children = [R31GUAJIRA]
#**********************************************
#**********************************************
#Para BOGOTA
R4BOGOTA = Node("R4BOGOTA", distance=0)
R4PIEDECUESTA = Node("R4PIEDECUESTA", parent=R4BOGOTA, distance=440)
R4FLORIDABLANCA = Node("R4FLORIDABLANCA", parent=R4PIEDECUESTA, distance=445)  #A través de Piedecuesta
R4BUCARAMANGA = Node("R4BUCARAMANGA", parent=R4FLORIDABLANCA, distance=452) #A través de Piedecuesta y Floridablanca
R4GIRON = Node("R4GIRON", parent=R4BUCARAMANGA, distance=456) #A través de Piedecuesta, Floridablanca y Bucaramanga
R4MEDELLIN = Node("R4MEDELLIN", parent=R4BUCARAMANGA, distance=852)  #A través de Bucaramanga
R4GUAJIRA = Node("R4GUAJIRA", parent=R4MEDELLIN, distance=1402)

R4BOGOTA.children = [R4PIEDECUESTA]
R4PIEDECUESTA.children = [R4FLORIDABLANCA]
R4FLORIDABLANCA.children = [R4BUCARAMANGA]
R4BUCARAMANGA.children = [R4GIRON, R4MEDELLIN]
R4MEDELLIN.children = [R4GUAJIRA]

# Para BOGOTA (R41) - Segunda opción
R41BOGOTA = Node("R41BOGOTA", distance=0)
R41PIEDECUESTA = Node("R41PIEDECUESTA", parent=R41BOGOTA, distance=450) #Ruta ligeramente mas larga
R41FLORIDABLANCA = Node("R41FLORIDABLANCA", parent=R41PIEDECUESTA, distance=455) #Ruta a Floridablanca por Piedecuesta
R41BUCARAMANGA = Node("R41BUCARAMANGA", parent=R41FLORIDABLANCA, distance=460) #Ruta a Bucaramanga por Piedecuesta y Floridablanca
R41GIRON = Node("R41GIRON", parent=R41BUCARAMANGA, distance=465) #Ruta a Giron por Piedecuesta, Floridablanca y Bucaramanga
R41MEDELLIN = Node("R41MEDELLIN", parent=R41BOGOTA, distance=840) #Ruta directa y ligeramente mas corta
R41GUAJIRA = Node("R41GUAJIRA", parent=R41MEDELLIN, distance=1390)

R41BOGOTA.children = [R41PIEDECUESTA, R41MEDELLIN]
R41PIEDECUESTA.children = [R41FLORIDABLANCA]
R41FLORIDABLANCA.children = [R41BUCARAMANGA]
R41BUCARAMANGA.children = [R41GIRON]
R41MEDELLIN.children = [R41GUAJIRA]
#**********************************************
#**********************************************
#Para MEDELLIN
R5MEDELLIN = Node("R5MEDELLIN", distance=0)
R5PIEDECUESTA = Node("R5PIEDECUESTA", parent=R5MEDELLIN, distance=844)
R5FLORIDABLANCA = Node("R5FLORIDABLANCA", parent=R5PIEDECUESTA, distance=837)
R5BUCARAMANGA = Node("R5FLORIDABLANCA", parent=R5FLORIDABLANCA, distance=830)
R5GIRON = Node("R5GIRON", parent=R5BUCARAMANGA, distance=834)
R5BOGOTA = Node("R5BOGOTA", parent=R5PIEDECUESTA, distance=852)
R5GUAJIRA = Node("R5GUAJIRA", parent=R5MEDELLIN, distance=550)

R5MEDELLIN.children = [R5PIEDECUESTA, R5GUAJIRA]
R5PIEDECUESTA.children = [R5FLORIDABLANCA, R5BOGOTA]
R5FLORIDABLANCA.children = [R5BUCARAMANGA]
R5BUCARAMANGA.children = [R5GIRON]

# Para MEDELLIN (R51) - Segunda opción
R51MEDELLIN = Node("R51MEDELLIN", distance=0)
R51PIEDECUESTA = Node("R51PIEDECUESTA", parent=R51MEDELLIN, distance=850) #Ruta ligeramente mas larga
R51FLORIDABLANCA = Node("R51FLORIDABLANCA", parent=R51PIEDECUESTA, distance=845) #Ruta a Floridablanca por Piedecuesta
R51BUCARAMANGA = Node("R51BUCARAMANGA", parent=R51FLORIDABLANCA, distance=840) #Ruta a Bucaramanga por Piedecuesta y Floridablanca
R51GIRON = Node("R51GIRON", parent=R51BUCARAMANGA, distance=845) #Ruta a Giron por Piedecuesta, Floridablanca y Bucaramanga
R51BOGOTA = Node("R51BOGOTA", parent=R51PIEDECUESTA, distance=860) #Ruta a Bogota por Piedecuesta
R51GUAJIRA = Node("R51GUAJIRA", parent=R51MEDELLIN, distance=560) #Ruta ligeramente mas larga

R51MEDELLIN.children = [R51PIEDECUESTA, R51GUAJIRA]
R51PIEDECUESTA.children = [R51FLORIDABLANCA, R51BOGOTA]
R51FLORIDABLANCA.children = [R51BUCARAMANGA]
R51BUCARAMANGA.children = [R51GIRON]
#**********************************************
#**********************************************
#Para GUAJIRA
R6GUAJIRA = Node("R6GUAJIRA", distance=0)
R6PIEDECUESTA = Node("R6PIEDECUESTA", parent=R6GUAJIRA, distance=1394)
R6FLORIDABLANCA = Node("R6FLORIDABLANCA", parent=R6PIEDECUESTA, distance=1387)
R6BUCARAMANGA = Node("R6BUCARAMANGA", parent=R6FLORIDABLANCA, distance=1380)
R6GIRON = Node("R6GIRON", parent=R6BUCARAMANGA, distance=1384)
R6BOGOTA = Node("R6BOGOTA", parent=R6PIEDECUESTA, distance=1402)
R6MEDELLIN = Node("R6MEDELLIN", parent=R6GUAJIRA, distance=550)

R6GUAJIRA.children = [R6PIEDECUESTA, R6MEDELLIN]
R6PIEDECUESTA.children = [R6FLORIDABLANCA, R6BOGOTA]
R6FLORIDABLANCA.children = [R6BUCARAMANGA]
R6BUCARAMANGA.children = [R6GIRON]

# Para GUAJIRA (R61) - Segunda opción
R61GUAJIRA = Node("R61GUAJIRA", distance=0)
R61PIEDECUESTA = Node("R61PIEDECUESTA", parent=R61GUAJIRA, distance=1400) #Ruta ligeramente mas larga
R61FLORIDABLANCA = Node("R61FLORIDABLANCA", parent=R61PIEDECUESTA, distance=1395) #Ruta a Floridablanca por Piedecuesta
R61BUCARAMANGA = Node("R61BUCARAMANGA", parent=R61FLORIDABLANCA, distance=1390) #Ruta a Bucaramanga por Piedecuesta y Floridablanca
R61GIRON = Node("R61GIRON", parent=R61BUCARAMANGA, distance=1395) #Ruta a Giron por Piedecuesta, Floridablanca y Bucaramanga
R61BOGOTA = Node("R61BOGOTA", parent=R61PIEDECUESTA, distance=1410) #Ruta a Bogota por Piedecuesta
R61MEDELLIN = Node("R61MEDELLIN", parent=R61GUAJIRA, distance=560) #Ruta ligeramente mas larga

R61GUAJIRA.children = [R61PIEDECUESTA, R61MEDELLIN]
R61PIEDECUESTA.children = [R61FLORIDABLANCA, R61BOGOTA]
R61FLORIDABLANCA.children = [R61BUCARAMANGA]
R61BUCARAMANGA.children = [R61GIRON]
#**********************************************

######################################################################
#--------------------------------------------------> ¡¡ARBOL GENERAL!!
#Se definen los nodos
root = PIEDECUESTA = Node("PIEDECUESTA", rutas0 = R0PIEDECUESTA, rutas01 = R01PIEDECUESTA)
FLORIDABLANCA = Node("FLORIDABLANCA", parent=PIEDECUESTA, rutas1 = R1FLORIDABLANCA, rutas11 = R11FLORIDABLANCA)
BUCARAMANGA = Node("BUCARAMANGA", parent=FLORIDABLANCA, rutas2 = R2BUCARAMANGA, rutas21 = R21BUCARAMANGA)
GIRON = Node("GIRON", parent=BUCARAMANGA, rutas3 = R3GIRON, rutas31 = R31GIRON)
BOGOTA = Node("BOGOTA", parent=PIEDECUESTA, rutas4 = R4BOGOTA, rutas41 = R41BOGOTA)
MEDELLIN = Node("MEDELLIN", parent=BUCARAMANGA, rutas5 = R5MEDELLIN, rutas51 = R51MEDELLIN)
GUAJIRA = Node("GUAJIRA", parent=MEDELLIN, rutas6 = R6GUAJIRA, rutas61 = R61GUAJIRA)

#Relaciones padre e hijos
PIEDECUESTA.children = [BOGOTA, FLORIDABLANCA]
BUCARAMANGA.children = [GIRON, MEDELLIN]
FLORIDABLANCA.children = [BUCARAMANGA]
MEDELLIN.children = [GUAJIRA]

#Revisamos el arbol hasta el momento:
print("ARBOL GENERAL --->")
root.vshow(style="double")
print("")

#Ahora se imprimiran las rutas de cada ubicacion
print("****Rutas de PIEDECUESTA --->")
print("")
root.rutas0.show(style="ansi", attr_list=["distance"])
print("")
root.rutas01.show(style="ansi", attr_list=["distance"])
print("")
print("****Rutas de FLORIDABLANCA --->")
print("")
R1FLORIDABLANCA.show(style="ansi", attr_list=["distance"])
print("")
R11FLORIDABLANCA.show(style="ansi", attr_list=["distance"])
print("")
print("****Rutas de BUCARAMANGA --->")
print("")
R2BUCARAMANGA.show(style="ansi", attr_list=["distance"])
print("")
R21BUCARAMANGA.show(style="ansi", attr_list=["distance"])
print("")
print("****Rutas de GIRON --->")
print("")
R3GIRON.show(style="ansi", attr_list=["distance"])
print("")
R31GIRON.show(style="ansi", attr_list=["distance"])
print("")
print("****Rutas de BOGOTA --->")
print("")
R4BOGOTA.show(style="ansi", attr_list=["distance"])
print("")
R41BOGOTA.show(style="ansi", attr_list=["distance"])
print("")
print("****Rutas de MEDELLIN --->")
print("")
R5MEDELLIN.show(style="ansi", attr_list=["distance"])
print("")
R51MEDELLIN.show(style="ansi", attr_list=["distance"])
print("")
print("****Rutas de GUAJIRA --->")
print("")
R6GUAJIRA.show(style="ansi", attr_list=["distance"])
print("")
R6GUAJIRA.show(style="ansi", attr_list=["distance"])
print("")

#********************************************
#Bueno, entonces ya habiendo creado la base para el problema de optimización, se agregara una nueva funcion que mejore al sistema. Esta será una funcion que permita al usuario
#Obtener informacion sobre cuantas ubicaciones y cuantas rutas tiene cada ubicacion (Pesos y conteo de arboles de rutas por cada nodo general)
#Esto es muy util debido a que le permite al usuario ver cuanta variedad de rutas hay en un sistema de navegación; es claro que entre mas rutas es mejor puesto que permite guiarse por más caminos.
#Sin embargo, en este ejemplo se utilizaron 7 ubicaciones con 2 arboles de rutas cada uno, esto, por practicidad y para probar el sistema.

#Se debe introducir el arbol raiz del arbol de ubicaciones (El general)
def locations(self):
  return len(list(root.descendants)) + 1

def contarRutas(node):
  #Cuenta el nuermo de arboles de ruta (atributos de tipo arbol (nodos)) para un nodo dado.
  return len([
        attr for attr, val in vars(node).items()
        if attr.startswith("rutas") and isinstance(val, Node)
    ])

def imprimirNumeroDeRutas(raiz):
    resultado = {}
    for node in [raiz] + list(raiz.descendants):
        resultado[node.name] = contarRutas(node)
    return resultado

def nombresNodos(nodoRaiz):
    #Obtiene los nombres de todos los nodos del arbol (Raiz y descendientes).
    nodeNames = [nodoRaiz.name]  #Empieza con el nombre de la raiz
    nodeNames.extend([node.name for node in nodoRaiz.descendants])  #Agrega los nombres de los descendientes
    return nodeNames

def distanciaMasCorta(root, inicio, final):
    # 1) Encontrar el nodo de partida en el árbol principal
    nodo_inicio = find_name(root, inicio)
    if not nodo_inicio:
        return -1, None

    candidatas = []
    # 2) Iterar sobre todos los subárboles de rutas (ej: rutas0, rutas1)
    for attr in vars(nodo_inicio):
        if not attr.startswith("rutas"):
            continue
        subarbol = getattr(nodo_inicio, attr)  # Subárbol actual (ej: R0PIEDECUESTA)

        # 3) Buscar todos los nodos en el subárbol que coincidan con el destino
        for nodo in subarbol.descendants:
            if nodo.name.endswith(final):
                # Construir la ruta relativa DESDE subarbol hasta nodo
                path_parts = []
                current = nodo
                while current != subarbol and current is not None:
                    path_parts.append(current.name)
                    current = current.parent
                if current != subarbol:
                    continue  # Si no está bajo el subarbol, ignorar
                path_parts.reverse()

                # 4) Reconstruir el camino desde el nodo de inicio del subárbol
                camino = [subarbol]  # Incluir la raíz del subárbol
                for part in path_parts:
                    current_node = find_name(subarbol, part)
                    if current_node:
                        camino.append(current_node)

                if camino:
                    # La distancia ya está precalculada en el nodo destino
                    dist = getattr(nodo, "distance", 0)
                    candidatas.append((dist, camino))

    # 5) Si no hay rutas válidas
    if not candidatas:
        return -1, None

    # 6) Seleccionar la ruta con la menor distancia
    distancia, camino = min(candidatas, key=lambda x: x[0])
    print("Camino más corto:", [n.name for n in camino])
    return distancia, camino

#Finalmente, se realizara un metodo main() en el cual estara la logica para indicar cual ruta tomar, de que nodos se compone y para consultar las ubicaciones y las rutas
def main():
  print("Usted esta ingresando al sistema de optimizacion de rutas del equipo #1 de estructuras de datos y analisis de algoritmos Grupo -> E1")
  print("")
  print("A continuacion, le mostraremos el numero de ubicaciones y el numero de rutas que posee cada ubicacion")
  num = locations(root)
  print(f"El número de ubicaciones es: {num}")
  rutas_por_nodo = imprimirNumeroDeRutas(root)
  print("El número de rutas por cada ubicación:")
  for nombre, nro in rutas_por_nodo.items():
    print(f"  - {nombre}: {nro} rutas")
  print("")
  print("Si desea ver el arbol antes de introducir su lugar de partida y su destino, porfavor presiones 1, de lo contrario presiones 0")
  x = int(input("Porfavor ingrese 1 Ó 0: "))
  while x != 1 and x != 0:
    print("Porfavor ingrese 1 Ó 0")
    x = int(input("Porfavor ingrese 1 Ó 0: "))
  if x == 1:
    root.vshow(style="double")
  print("")
  print("Ahora porfavor seleccione primero una ubicacion de partida y luego una de destino")
  validos = nombresNodos(root)
  inicio = input("Porfavor ingrese una ubicacion valida (Ingrese exactamente lo que aparece de nombre (Mayusculas incluidas)): ")
  while inicio not in validos:
        print("Ubicación no valida, por favor ingrese una ubicacion de la que exista:", validos)
        inicio = input("Por favor ingrese una ubicación válida: ")
  print("Ahora porfavor ingrese la ubicacion de destino: ")
  destino = input("Porfavor ingrese una ubicacion valida (Ingrese exactamente lo que aparece de nombre (Mayusculas incluidas)): ")
  while destino not in validos:
        print("Ubicación no valida, por favor ingrese una ubicacion valida", validos)
        destino = input("Por favor ingrese una ubicación válida: ")
  print("")
  #Decidir cual camino es mejor
  print(f"La respuesta es: ")
  print("")
  mejor_dist, mejor_camino = distanciaMasCorta(root, inicio, destino)
  if mejor_dist != -1:  #Se verifica si se encontró un camino
      print("La distancia más corta entre", inicio, "y", destino, "es:", mejor_dist)
  elif inicio == destino:
      print(f"Ya estas en  {inicio}  No hay necesidad de un camino y la distancia es 0")
  else:
      print("No se encontró un camino entre", inicio, "y", destino)
  if destino == "PIEDECUESTA":
    print("")
    print("########################################################################")
    print("########################################################################")
    print("#################### BIENVENIDOS A PIEDECUESTA #########################")
    print("####################   LA UTOPIA COLOMBIANA ############################")
    print("########################################################################")
    print("########################################################################")

if __name__ == "__main__":
    main()

#NOTA IMPORTANTE: EN LOS NODOS APARECEN VALORES YA TOTALES, POR EJEMPLO, DE PIEDECUESTA A FLORIDABLANCA APARECE, POR EJEMPLO, 5, Y DE PIEDECUESTA A BUCARAMANGA APARECE 12, ENTONCES EL VALOR DE PIEDECUESTA
#A BUCARAMANGA ES 12 Y NO 17, POR QUE EL 12 TIENE INCLUIDO EL 5.