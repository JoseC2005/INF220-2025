"""
ADT Conjunto implementado con Estructuras Dinámicas
Autor: Jose Carlos Justiniano Montaño
GitHub: https://github.com/[tu_usuario]/adt-conjunto-dinamico
"""

class ConjuntoDinamico:
    """
    Implementación de un ADT Conjunto usando estructura dinámica (clases y objetos).
    Utiliza listas internamente pero encapsula la implementación.
    """
    
    def __init__(self, elementos=None):
        """
        Inicializa el conjunto con elementos opcionales.
        
        Args:
            elementos (list, optional): Lista de elementos iniciales. Defaults to None.
        """
        self._elementos = []
        if elementos is not None:
            for elemento in elementos:
                self.agregar(elemento)
    
    # ==================== MÉTODOS GETTER ====================
    
    def get_elementos(self):
        """
        Devuelve una copia de los elementos del conjunto.
        
        Returns:
            list: Copia de los elementos del conjunto.
        """
        return self._elementos.copy()
    
    def get_tamano(self):
        """
        Devuelve el tamaño del conjunto.
        
        Returns:
            int: Número de elementos en el conjunto.
        """
        return len(self._elementos)
    
    def contiene(self, elemento):
        """
        Verifica si un elemento está en el conjunto.
        
        Args:
            elemento: Elemento a verificar.
            
        Returns:
            bool: True si el elemento está en el conjunto, False en caso contrario.
        """
        return elemento in self._elementos
    
    def esta_vacio(self):
        """
        Verifica si el conjunto está vacío.
        
        Returns:
            bool: True si el conjunto está vacío, False en caso contrario.
        """
        return len(self._elementos) == 0
    
    # ==================== MÉTODOS SETTER ====================
    
    def agregar(self, elemento):
        """
        Agrega un elemento al conjunto si no existe.
        
        Args:
            elemento: Elemento a agregar.
            
        Returns:
            bool: True si se agregó el elemento, False si ya existía.
        """
        if elemento not in self._elementos:
            self._elementos.append(elemento)
            return True
        return False
    
    def eliminar(self, elemento):
        """
        Elimina un elemento del conjunto si existe.
        
        Args:
            elemento: Elemento a eliminar.
            
        Returns:
            bool: True si se eliminó el elemento, False si no existía.
        """
        if elemento in self._elementos:
            self._elementos.remove(elemento)
            return True
        return False
    
    def limpiar(self):
        """Elimina todos los elementos del conjunto."""
        self._elementos = []
    
    # ==================== OPERACIONES DE CONJUNTO ====================
    
    def union(self, otro_conjunto):
        """
        Devuelve la unión con otro conjunto.
        
        Args:
            otro_conjunto (ConjuntoDinamico): Otro conjunto para la operación.
            
        Returns:
            ConjuntoDinamico: Nuevo conjunto con la unión.
        """
        resultado = ConjuntoDinamico(self._elementos)
        for elemento in otro_conjunto.get_elementos():
            resultado.agregar(elemento)
        return resultado
    
    def interseccion(self, otro_conjunto):
        """
        Devuelve la intersección con otro conjunto.
        
        Args:
            otro_conjunto (ConjuntoDinamico): Otro conjunto para la operación.
            
        Returns:
            ConjuntoDinamico: Nuevo conjunto con la intersección.
        """
        resultado = ConjuntoDinamico()
        for elemento in self._elementos:
            if otro_conjunto.contiene(elemento):
                resultado.agregar(elemento)
        return resultado
    
    def diferencia(self, otro_conjunto):
        """
        Devuelve la diferencia con otro conjunto.
        
        Args:
            otro_conjunto (ConjuntoDinamico): Otro conjunto para la operación.
            
        Returns:
            ConjuntoDinamico: Nuevo conjunto con la diferencia.
        """
        resultado = ConjuntoDinamico(self._elementos)
        for elemento in otro_conjunto.get_elementos():
            resultado.eliminar(elemento)
        return resultado
    
    def es_subconjunto(self, otro_conjunto):
        """
        Verifica si este conjunto es subconjunto de otro.
        
        Args:
            otro_conjunto (ConjuntoDinamico): Conjunto a verificar.
            
        Returns:
            bool: True si es subconjunto, False en caso contrario.
        """
        for elemento in self._elementos:
            if not otro_conjunto.contiene(elemento):
                return False
        return True
    
    # ==================== MÉTODOS ESPECIALES ====================
    
    def __str__(self):
        """
        Representación en string del conjunto.
        
        Returns:
            str: Representación del conjunto.
        """
        return f"Conjunto({self._elementos})"
    
    def __len__(self):
        """
        Devuelve el tamaño del conjunto.
        
        Returns:
            int: Número de elementos.
        """
        return self.get_tamano()
    
    def __contains__(self, elemento):
        """
        Permite usar el operador 'in' con el conjunto.
        
        Args:
            elemento: Elemento a verificar.
            
        Returns:
            bool: True si el elemento está en el conjunto.
        """
        return self.contiene(elemento)


def demostrar_conjunto_dinamico():
    """
    Función de demostración del ADT Conjunto Dinámico.
    """
    print("=" * 60)
    print("DEMOSTRACIÓN ADT CONJUNTO - ESTRUCTURA DINÁMICA")
    print("=" * 60)
    
    # Crear conjuntos
    print("\n1. CREACIÓN DE CONJUNTOS:")
    conjunto_a = ConjuntoDinamico([1, 2, 3, 4, 5])
    conjunto_b = ConjuntoDinamico([4, 5, 6, 7, 8])
    
    print(f"Conjunto A: {conjunto_a}")
    print(f"Conjunto B: {conjunto_b}")
    
    # Operaciones con getters
    print("\n2. OPERACIONES GETTER:")
    print(f"Tamaño de A: {conjunto_a.get_tamano()}")
    print(f"Tamaño de B: {conjunto_b.get_tamano()}")
    print(f"¿El 3 está en A? {conjunto_a.contiene(3)}")
    print(f"¿El 9 está en B? {conjunto_b.contiene(9)}")
    print(f"¿A está vacío? {conjunto_a.esta_vacio()}")
    
    # Operaciones con setters
    print("\n3. OPERACIONES SETTER:")
    print(f"Agregar 6 a A: {conjunto_a.agregar(6)}")
    print(f"Agregar 3 a A (duplicado): {conjunto_a.agregar(3)}")
    print(f"Eliminar 2 de A: {conjunto_a.eliminar(2)}")
    print(f"Eliminar 10 de A (no existe): {conjunto_a.eliminar(10)}")
    print(f"Conjunto A después de operaciones: {conjunto_a}")
    
    # Operaciones de conjunto
    print("\n4. OPERACIONES DE CONJUNTO:")
    union_ab = conjunto_a.union(conjunto_b)
    interseccion_ab = conjunto_a.interseccion(conjunto_b)
    diferencia_ab = conjunto_a.diferencia(conjunto_b)
    
    print(f"Unión A ∪ B: {union_ab}")
    print(f"Intersección A ∩ B: {interseccion_ab}")
    print(f"Diferencia A - B: {diferencia_ab}")
    print(f"¿A es subconjunto de B? {conjunto_a.es_subconjunto(conjunto_b)}")
    
    # Métodos especiales
    print("\n5. MÉTODOS ESPECIALES:")
    print(f"Tamaño usando len(): {len(conjunto_a)}")
    print(f"¿4 in A? {4 in conjunto_a}")
    print(f"¿10 in A? {10 in conjunto_a}")
    
    # Limpiar conjunto
    print("\n6. OPERACIÓN LIMPIAR:")
    conjunto_temp = ConjuntoDinamico([1, 2, 3])
    print(f"Conjunto temporal: {conjunto_temp}")
    conjunto_temp.limpiar()
    print(f"Después de limpiar: {conjunto_temp}")
    print(f"¿Está vacío? {conjunto_temp.esta_vacio()}")


if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    """
    demostrar_conjunto_dinamico()
    print("\n" + "=" * 60)
    print("DEMOSTRACIÓN COMPLETADA")
    print("=" * 60)