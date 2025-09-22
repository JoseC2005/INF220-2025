def crear_conjunto(capacidad_maxima):
    """Crea un conjunto estático"""
    return {
        'capacidad': capacidad_maxima,
        'elementos': [None] * capacidad_maxima,
        'contador': 0
    }

def get_capacidad(conjunto):
    return conjunto['capacidad']

def get_tamano(conjunto):
    return conjunto['contador']

def agregar_elemento(conjunto, elemento):
    """Agrega un elemento al conjunto si no existe y hay espacio"""
    if conjunto['contador'] < conjunto['capacidad'] and not contiene_elemento(conjunto, elemento):
        conjunto['elementos'][conjunto['contador']] = elemento
        conjunto['contador'] += 1
        return True
    return False

def contiene_elemento(conjunto, elemento):
    """Verifica si un elemento está en el conjunto"""
    for i in range(conjunto['contador']):
        if conjunto['elementos'][i] == elemento:
            return True
    return False

def eliminar_elemento(conjunto, elemento):
    """Elimina un elemento del conjunto"""
    for i in range(conjunto['contador']):
        if conjunto['elementos'][i] == elemento:
            # Mover el último elemento a la posición eliminada
            conjunto['elementos'][i] = conjunto['elementos'][conjunto['contador'] - 1]
            conjunto['elementos'][conjunto['contador'] - 1] = None
            conjunto['contador'] -= 1
            return True
    return False

def get_elementos(conjunto):
    """Retorna la lista de elementos"""
    return conjunto['elementos'][:conjunto['contador']]

def union_conjuntos(conjunto1, conjunto2):
    """Unión de dos conjuntos"""
    nueva_capacidad = conjunto1['capacidad'] + conjunto2['capacidad']
    nuevo_conjunto = crear_conjunto(nueva_capacidad)
    
    # Agregar elementos del primer conjunto
    for i in range(conjunto1['contador']):
        agregar_elemento(nuevo_conjunto, conjunto1['elementos'][i])
    
    # Agregar elementos del segundo conjunto
    for i in range(conjunto2['contador']):
        agregar_elemento(nuevo_conjunto, conjunto2['elementos'][i])
    
    return nuevo_conjunto

def interseccion_conjuntos(conjunto1, conjunto2):
    """Intersección de dos conjuntos"""
    nueva_capacidad = min(conjunto1['capacidad'], conjunto2['capacidad'])
    nuevo_conjunto = crear_conjunto(nueva_capacidad)
    
    for i in range(conjunto1['contador']):
        elemento = conjunto1['elementos'][i]
        if contiene_elemento(conjunto2, elemento):
            agregar_elemento(nuevo_conjunto, elemento)
    
    return nuevo_conjunto

def diferencia_conjuntos(conjunto1, conjunto2):
    """Diferencia conjunto1 - conjunto2"""
    nueva_capacidad = conjunto1['capacidad']
    nuevo_conjunto = crear_conjunto(nueva_capacidad)
    
    for i in range(conjunto1['contador']):
        elemento = conjunto1['elementos'][i]
        if not contiene_elemento(conjunto2, elemento):
            agregar_elemento(nuevo_conjunto, elemento)
    
    return nuevo_conjunto

def es_subconjunto(conjunto1, conjunto2):
    """Verifica si conjunto1 es subconjunto de conjunto2"""
    for i in range(conjunto1['contador']):
        if not contiene_elemento(conjunto2, conjunto1['elementos'][i]):
            return False
    return True

def conjunto_a_string(conjunto):
    """Convierte el conjunto a string"""
    return str(get_elementos(conjunto))