class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ConjuntoDinamico:
    def __init__(self):
        self.cabeza = None
        self.contador = 0

    # Getter para obtener el número de elementos
    def get_tamano(self):
        return self.contador

    # Setter para agregar un elemento
    def agregar(self, elemento):
        if not self.contiene(elemento):
            nuevo_nodo = Nodo(elemento)
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            self.contador += 1
            return True
        return False

    # Getter para verificar si un elemento está en el conjunto
    def contiene(self, elemento):
        actual = self.cabeza
        while actual is not None:
            if actual.dato == elemento:
                return True
            actual = actual.siguiente
        return False

    # Setter para eliminar un elemento
    def eliminar(self, elemento):
        actual = self.cabeza
        anterior = None
        
        while actual is not None:
            if actual.dato == elemento:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.contador -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    # Getter para obtener todos los elementos
    def get_elementos(self):
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

    # Getter para la unión de conjuntos
    def union(self, otro_conjunto):
        nuevo_conjunto = ConjuntoDinamico()
        
        actual = self.cabeza
        while actual is not None:
            nuevo_conjunto.agregar(actual.dato)
            actual = actual.siguiente
        
        actual_otro = otro_conjunto.cabeza
        while actual_otro is not None:
            nuevo_conjunto.agregar(actual_otro.dato)
            actual_otro = actual_otro.siguiente
        
        return nuevo_conjunto

    # Getter para la intersección de conjuntos
    def interseccion(self, otro_conjunto):
        nuevo_conjunto = ConjuntoDinamico()
        
        actual = self.cabeza
        while actual is not None:
            if otro_conjunto.contiene(actual.dato):
                nuevo_conjunto.agregar(actual.dato)
            actual = actual.siguiente
        
        return nuevo_conjunto

    # Getter para la diferencia de conjuntos
    def diferencia(self, otro_conjunto):
        nuevo_conjunto = ConjuntoDinamico()
        
        actual = self.cabeza
        while actual is not None:
            if not otro_conjunto.contiene(actual.dato):
                nuevo_conjunto.agregar(actual.dato)
            actual = actual.siguiente
        
        return nuevo_conjunto

    # Getter para verificar si es subconjunto
    def es_subconjunto(self, otro_conjunto):
        actual = self.cabeza
        while actual is not None:
            if not otro_conjunto.contiene(actual.dato):
                return False
            actual = actual.siguiente
        return True

    # Representación en string
    def __str__(self):
        return str(self.get_elementos())