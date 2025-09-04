"""
ADT Conjunto implementado con Estructura Estática
Solo funciones puras - Sin instanciación de objetos
"""

# ==================== OPERACIONES BÁSICAS ====================

def crear_conjunto(elementos=None):
    """
    Crea un nuevo conjunto estático.
    
    Args:
        elementos (list): Lista inicial de elementos (opcional)
    
    Returns:
        list: Conjunto representado como lista
    """
    if elementos is None:
        return []
    
    conjunto = []
    for elemento in elementos:
        if elemento not in conjunto:
            conjunto.append(elemento)
    return conjunto


def agregar_elemento(conjunto, elemento):
    """
    Agrega un elemento al conjunto si no existe.
    
    Args:
        conjunto (list): Conjunto existente
        elemento: Elemento a agregar
    
    Returns:
        list: Nuevo conjunto con el elemento agregado
    """
    if elemento not in conjunto:
        return conjunto + [elemento]
    return conjunto


def eliminar_elemento(conjunto, elemento):
    """
    Elimina un elemento del conjunto si existe.
    
    Args:
        conjunto (list): Conjunto existente
        elemento: Elemento a eliminar
    
    Returns:
        list: Nuevo conjunto sin el elemento
    """
    if elemento in conjunto:
        nuevo_conjunto = conjunto.copy()
        nuevo_conjunto.remove(elemento)
        return nuevo_conjunto
    return conjunto


def contiene_elemento(conjunto, elemento):
    """
    Verifica si un elemento está en el conjunto.
    
    Args:
        conjunto (list): Conjunto a verificar
        elemento: Elemento a buscar
    
    Returns:
        bool: True si el elemento está en el conjunto
    """
    return elemento in conjunto


def obtener_tamano(conjunto):
    """
    Obtiene el número de elementos en el conjunto.
    
    Args:
        conjunto (list): Conjunto a medir
    
    Returns:
        int: Número de elementos
    """
    return len(conjunto)


def esta_vacio(conjunto):
    """
    Verifica si el conjunto está vacío.
    
    Args:
        conjunto (list): Conjunto a verificar
    
    Returns:
        bool: True si el conjunto está vacío
    """
    return len(conjunto) == 0


# ==================== OPERACIONES DE CONJUNTO ====================

def union(conjunto_a, conjunto_b):
    """
    Realiza la unión de dos conjuntos.
    
    Args:
        conjunto_a (list): Primer conjunto
        conjunto_b (list): Segundo conjunto
    
    Returns:
        list: Conjunto resultante de la unión
    """
    resultado = conjunto_a.copy()
    for elemento in conjunto_b:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado


def interseccion(conjunto_a, conjunto_b):
    """
    Realiza la intersección de dos conjuntos.
    
    Args:
        conjunto_a (list): Primer conjunto
        conjunto_b (list): Segundo conjunto
    
    Returns:
        list: Conjunto resultante de la intersección
    """
    resultado = []
    for elemento in conjunto_a:
        if elemento in conjunto_b:
            resultado.append(elemento)
    return resultado


def diferencia(conjunto_a, conjunto_b):
    """
    Realiza la diferencia entre dos conjuntos (A - B).
    
    Args:
        conjunto_a (list): Primer conjunto
        conjunto_b (list): Segundo conjunto
    
    Returns:
        list: Conjunto resultante de la diferencia
    """
    resultado = []
    for elemento in conjunto_a:
        if elemento not in conjunto_b:
            resultado.append(elemento)
    return resultado


def es_subconjunto(conjunto_a, conjunto_b):
    """
    Verifica si conjunto_a es subconjunto de conjunto_b.
    
    Args:
        conjunto_a (list): Posible subconjunto
        conjunto_b (list): Conjunto principal
    
    Returns:
        bool: True si A es subconjunto de B
    """
    for elemento in conjunto_a:
        if elemento not in conjunto_b:
            return False
    return True


# ==================== FUNCIÓN DE DEMOSTRACIÓN ====================

def demostrar_conjunto_estatico():
    """
    Demuestra el uso del ADT Conjunto con estructura estática.
    """
    print("=== ADT CONJUNTO - ESTRUCTURA ESTÁTICA ===")
    print("(Sin instanciación de objetos)\n")
    
    # Crear conjuntos
    print("1. CREACIÓN DE CONJUNTOS:")
    conjunto_a = crear_conjunto([1, 2, 3, 4])
    conjunto_b = crear_conjunto([3, 4, 5, 6])
    
    print(f"Conjunto A: {conjunto_a}")
    print(f"Conjunto B: {conjunto_b}")
    
    # Operaciones básicas
    print("\n2. OPERACIONES BÁSICAS:")
    print(f"Tamaño de A: {obtener_tamano(conjunto_a)}")
    print(f"¿A contiene 3? {contiene_elemento(conjunto_a, 3)}")
    print(f"¿A está vacío? {esta_vacio(conjunto_a)}")
    
    # Modificar conjuntos
    print("\n3. MODIFICACIÓN DE CONJUNTOS:")
    conjunto_a = agregar_elemento(conjunto_a, 5)
    print(f"A después de agregar 5: {conjunto_a}")
    
    conjunto_a = eliminar_elemento(conjunto_a, 2)
    print(f"A después de eliminar 2: {conjunto_a}")
    
    # Operaciones de conjunto
    print("\n4. OPERACIONES DE CONJUNTO:")
    print(f"Unión A ∪ B: {union(conjunto_a, conjunto_b)}")
    print(f"Intersección A ∩ B: {interseccion(conjunto_a, conjunto_b)}")
    print(f"Diferencia A - B: {diferencia(conjunto_a, conjunto_b)}")
    print(f"¿A es subconjunto de B? {es_subconjunto(conjunto_a, conjunto_b)}")
    
    # Crear conjunto vacío
    print("\n5. CONJUNTO VACÍO:")
    conjunto_vacio = crear_conjunto()
    print(f"Conjunto vacío: {conjunto_vacio}")
    print(f"¿Está vacío? {esta_vacio(conjunto_vacio)}")


if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    """
    demostrar_conjunto_estatico()
    print("\n=== DEMOSTRACIÓN COMPLETADA ===")