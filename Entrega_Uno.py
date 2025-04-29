import time

class NodoRuta:
    def __init__(self, destino, peso):
        self.destino = destino  # Nombre del destino
        self.peso = peso  # Peso de la ruta (tiempo)
        self.siguiente = None  # Apunta al siguiente vecino en la lista de rutas
        self.anterior = None  # Apunta al vecino anterior en la lista de rutas
        
class NodoUbicacion:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion  # Nombre de la ubicación
        self.rutas = None  # Lista enlazada de rutas
        self.siguiente = None  # Apunta al siguiente nodo en la lista de ubicaciones
        self.anterior = None  # Apunta al nodo anterior en la lista de ubicaciones

class RedDeUbicaciones:
    def __init__(self):
        self.head = None  # Primer nodo de la lista de ubicaciones
        self.tail = None  # Cola

    def esta_vacia(self):
        # Verifica si la lista de ubicaciones está vacía
        return self.head is None

    def agregar_ubicacion(self, ubicacion):
        # Agrega una ubicación al comienzo de la lista
        nuevo_nodo = NodoUbicacion(ubicacion)
        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.head
            self.head.anterior = nuevo_nodo
            self.head = nuevo_nodo

    def actualizar_tail(self):
        # Actualiza la cola para que apunte al último nodo de la lista
        actual = self.head
        while actual and actual.siguiente:
            actual = actual.siguiente
        self.tail = actual

    def ordenar_ubicaciones(self):
        # Ordena la lista de ubicaciones con Merge Sort y actualiza la cola
        self.head = self.merge_sort(self.head)
        self.actualizar_tail()

    def agregar_ruta(self, origen, destino, peso):
        nodo_origen = self.buscar_ubicacion(origen)
        if nodo_origen:
            nueva_ruta = NodoRuta(destino, peso)
            if nodo_origen.rutas is None:
                nodo_origen.rutas = nueva_ruta
            else:
                ruta_actual = nodo_origen.rutas
                while ruta_actual.siguiente:
                    ruta_actual = ruta_actual.siguiente
                ruta_actual.siguiente = nueva_ruta
                nueva_ruta.anterior = ruta_actual

    def ordenar_rutas(self, ubicacion): 
        # Ordena las rutas de una ubicación específica con Merge Sort
        nodo_origen = self.buscar_ubicacion(ubicacion)
        if nodo_origen and nodo_origen.rutas:
            nodo_origen.rutas = self.merge_sort_rutas(nodo_origen.rutas)

    def buscar_ubicacion(self, ubicacion):
        # Busca una ubicación en la lista de ubicaciones
        actual = self.head
        while actual:
            if actual.ubicacion == ubicacion:
                return actual
            if actual.ubicacion > ubicacion:
                return None
            actual = actual.siguiente
        return None

    def contar_ubicaciones(self):
        # Cuenta cuántas ubicaciones hay en la lista
        contador = 0
        actual = self.head
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def imprimir_red(self):
        # Imprime todas las ubicaciones y sus rutas
        actual = self.head
        while actual:
            print(f"Ubicación: {actual.ubicacion}")
            ruta_actual = actual.rutas
            while ruta_actual:
                print(f"   -> Ruta a {ruta_actual.destino} con costo {ruta_actual.peso}")
                ruta_actual = ruta_actual.siguiente
            actual = actual.siguiente

    
    def encontrar_ruta(self, inicio, destino, visitados=None, camino=None, costo=0):
        # Buscar ruta entre dos ubicaciones, considerando rutas indirectas
        if visitados is None:
            visitados = set()
        if camino is None:
            camino = []

        nodo_inicio = self.buscar_ubicacion(inicio)

        if nodo_inicio is None:
            print("El nodo de inicio no existe.")
            return None, float('inf')

        # Si llegamos al destino, devolvemos el camino y el costo
        if inicio == destino:
            return camino + [inicio], costo

        # Marcar el nodo de inicio como visitado
        visitados.add(inicio)

        mejor_camino = None
        mejor_costo = float('inf')

        # Explorar los vecinos
        ruta_actual = nodo_inicio.rutas
        while ruta_actual:
            if ruta_actual.destino not in visitados:
                nuevo_camino, nuevo_costo = self.encontrar_ruta(ruta_actual.destino, destino, visitados, camino + [inicio], costo + ruta_actual.peso)

                # Si encontramos un mejor camino, lo almacenamos
                if nuevo_camino and nuevo_costo < mejor_costo:
                    mejor_camino = nuevo_camino
                    mejor_costo = nuevo_costo

            ruta_actual = ruta_actual.siguiente

        visitados.remove(inicio)
        return mejor_camino, mejor_costo

    def iterar_ubicaciones(self):
        # Generador para iterar sobre todas las ubicaciones
        actual = self.head
        while actual:
            yield actual
            actual = actual.siguiente

    def merge_sort(self, head):
        # Función para ordenar las ubicaciones usando Merge Sort
        if not head or not head.siguiente:
            return head

        medio = self.obtener_medio(head)
        siguiente_medio = medio.siguiente
        medio.siguiente = None

        izquierda = self.merge_sort(head)
        derecha = self.merge_sort(siguiente_medio)

        return self.merge(izquierda, derecha)

    def merge(self, izquierda, derecha):
        # Función para fusionar dos listas ordenadas de ubicaciones
        if not izquierda:
            return derecha
        if not derecha:
            return izquierda

        if izquierda.ubicacion < derecha.ubicacion:
            resultado = izquierda
            resultado.siguiente = self.merge(izquierda.siguiente, derecha)
        else:
            resultado = derecha
            resultado.siguiente = self.merge(izquierda, derecha.siguiente)

        return resultado

    def obtener_medio(self, head):
        # Encuentra el nodo medio de la lista
        lento = head
        rapido = head
        while rapido.siguiente and rapido.siguiente.siguiente:
            lento = lento.siguiente
            rapido = rapido.siguiente.siguiente
        return lento

    def merge_sort_rutas(self, head):
        # Función para ordenar las rutas usando Merge Sort
        if not head or not head.siguiente:
            return head

        medio = self.obtener_medio_rutas(head)
        siguiente_medio = medio.siguiente
        medio.siguiente = None

        izquierda = self.merge_sort_rutas(head)
        derecha = self.merge_sort_rutas(siguiente_medio)

        return self.merge_rutas(izquierda, derecha)

    def merge_rutas(self, izquierda, derecha):
        # Función para fusionar dos listas ordenadas de rutas
        if not izquierda:
            return derecha
        if not derecha:
            return izquierda

        if izquierda.destino < derecha.destino:
            resultado = izquierda
            resultado.siguiente = self.merge_rutas(izquierda.siguiente, derecha)
        else:
            resultado = derecha
            resultado.siguiente = self.merge_rutas(izquierda, derecha.siguiente)

        return resultado

    def obtener_medio_rutas(self, head):
        # Encuentra el nodo medio de la lista de rutas
        lento = head
        rapido = head
        while rapido.siguiente and rapido.siguiente.siguiente:
            lento = lento.siguiente
            rapido = rapido.siguiente.siguiente
        return lento


# Ejemplo de uso
if __name__ == "__main__":
    # Crear la red de ubicaciones
    red = RedDeUbicaciones()

    # Agregar ubicaciones
    red.agregar_ubicacion("Piedecuesta")
    red.agregar_ubicacion("Bucaramanga")
    red.agregar_ubicacion("Bogota")
    red.agregar_ubicacion("Medellin")
    red.agregar_ubicacion("La Guajira")
    red.agregar_ubicacion("Leticia")
    red.agregar_ubicacion("Cucuta")
    red.agregar_ubicacion("Caracas")

    # Ordenar las ubicaciones después de agregarlas
    red.ordenar_ubicaciones()

    # Agregar rutas entre las ubicaciones
    red.agregar_ruta("Piedecuesta", "Bucaramanga", 1.0)
    red.agregar_ruta("Piedecuesta", "Bogota", 8.0)
    red.agregar_ruta("Bucaramanga", "Medellin", 7.0)
    red.agregar_ruta("Bucaramanga", "Leticia", 15.0)
    red.agregar_ruta("Bogota", "Medellin", 6.5)
    red.agregar_ruta("Bogota", "Caracas", 24.0)
    red.agregar_ruta("Bogota", "La Guajira", 12.0)
    red.agregar_ruta("Medellin", "Piedecuesta", 9.0)
    red.agregar_ruta("Medellin", "Bogota", 9.5)
    red.agregar_ruta("La Guajira", "Medellin", 14.0)
    red.agregar_ruta("La Guajira", "Piedecuesta", 21.0)
    red.agregar_ruta("Leticia", "Bogota", 13.0)
    red.agregar_ruta("Leticia", "La Guajira", 19.0)
    red.agregar_ruta("Cucuta", "Bucaramanga", 9.0)
    red.agregar_ruta("Cucuta", "Leticia", 18.0)
    red.agregar_ruta("Caracas", "Bogota", 24.0)
    red.agregar_ruta("Caracas", "Piedecuesta", 22.0)

    # Ordenar las rutas de cada ubicación
    red.ordenar_rutas("Piedecuesta")
    red.ordenar_rutas("Bucaramanga")
    red.ordenar_rutas("Bogota")
    red.ordenar_rutas("Medellin")
    red.ordenar_rutas("La Guajira")

    # Imprimir la red de ubicaciones y rutas
    print("Red de ubicaciones y rutas ordenadas:")
    red.imprimir_red()

    # Medir el tiempo para encontrar la ruta más corta de Bucaramanga a Caracas
    inicio = "Bucaramanga"
    fin = "Caracas"
    print(f"\nBuscando la ruta más corta de {inicio} a {fin}...")

    start_time = time.time()  # Tomar tiempo de inicio
    camino, costo = red.encontrar_ruta(inicio, fin)
    end_time = time.time()  # Tomar tiempo de fin

    if camino:
        print(f"\nCamino más corto: {' -> '.join(camino)}")
        print(f"Costo total: {costo}")
    else:
        print(f"No se encontró un camino desde {inicio} a {fin}.")

    print(f"\nTiempo de búsqueda: {end_time - start_time} segundos.")

    print("")

    if fin == "Piedecuesta":
        print("##############################################")
        print("########## Bienvenido A Piedecuesta ##########")
        print("############ La Utopia Colombiana ############")
        print("##############################################")