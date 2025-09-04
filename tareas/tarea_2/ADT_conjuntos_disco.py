"""
ADT Conjunto implementado con Almacenamiento en Disco
Los datos se guardan persistentemente en archivos JSON
"""

import json
import os

# ==================== OPERACIONES BÁSICAS ====================

def crear_conjunto_disco(nombre_archivo, elementos=None):
    """
    Crea un nuevo conjunto en disco.
    
    Args:
        nombre_archivo (str): Nombre del archivo para guardar
        elementos (list): Elementos iniciales (opcional)
    
    Returns:
        bool: True si se creó correctamente
    """
    try:
        datos = elementos if elementos else []
        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos, archivo)
        return True
    except Exception as e:
        print(f"Error creando conjunto: {e}")
        return False

def cargar_conjunto_disco(nombre_archivo):
    """
    Carga un conjunto desde disco.
    
    Args:
        nombre_archivo (str): Nombre del archivo a cargar
    
    Returns:
        list: Elementos del conjunto o lista vacía si error
    """
    try:
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'r') as archivo:
                return json.load(archivo)
        return []
    except Exception as e:
        print(f"Error cargando conjunto: {e}")
        return []

def guardar_conjunto_disco(nombre_archivo, elementos):
    """
    Guarda un conjunto en disco.
    
    Args:
        nombre_archivo (str): Nombre del archivo
        elementos (list): Elementos a guardar
    
    Returns:
        bool: True si se guardó correctamente
    """
    try:
        with open(nombre_archivo, 'w') as archivo:
            json.dump(elementos, archivo)
        return True
    except Exception as e:
        print(f"Error guardando conjunto: {e}")
        return False

# ==================== OPERACIONES DEL CONJUNTO ====================

def agregar_elemento_disco(nombre_archivo, elemento):
    """
    Agrega un elemento al conjunto en disco.
    
    Args:
        nombre_archivo (str): Nombre del archivo
        elemento: Elemento a agregar
    
    Returns:
        bool: True si se agregó correctamente
    """
    elementos = cargar_conjunto_disco(nombre_archivo)
    if elemento not in elementos:
        elementos.append(elemento)
        return guardar_conjunto_disco(nombre_archivo, elementos)
    return False

def eliminar_elemento_disco(nombre_archivo, elemento):
    """
    Elimina un elemento del conjunto en disco.
    
    Args:
        nombre_archivo (str): Nombre del archivo
        elemento: Elemento a eliminar
    
    Returns:
        bool: True si se eliminó correctamente
    """
    elementos = cargar_conjunto_disco(nombre_archivo)
    if elemento in elementos:
        elementos.remove(elemento)
        return guardar_conjunto_disco(nombre_archivo, elementos)
    return False

def contiene_elemento_disco(nombre_archivo, elemento):
    """
    Verifica si un elemento está en el conjunto del disco.
    
    Args:
        nombre_archivo (str): Nombre del archivo
        elemento: Elemento a verificar
    
    Returns:
        bool: True si el elemento existe
    """
    elementos = cargar_conjunto_disco(nombre_archivo)
    return elemento in elementos

def obtener_tamano_disco(nombre_archivo):
    """
    Obtiene el tamaño del conjunto en disco.
    
    Args:
        nombre_archivo (str): Nombre del archivo
    
    Returns:
        int: Número de elementos
    """
    elementos = cargar_conjunto_disco(nombre_archivo)
    return len(elementos)

def esta_vacio_disco(nombre_archivo):
    """
    Verifica si el conjunto en disco está vacío.
    
    Args:
        nombre_archivo (str): Nombre del archivo
    
    Returns:
        bool: True si está vacío
    """
    elementos = cargar_conjunto_disco(nombre_archivo)
    return len(elementos) == 0

# ==================== OPERACIONES AVANZADAS ====================

def union_disco(archivo_a, archivo_b, archivo_resultado):
    """
    Realiza la unión de dos conjuntos en disco.
    
    Args:
        archivo_a (str): Primer conjunto
        archivo_b (str): Segundo conjunto
        archivo_resultado (str): Archivo para el resultado
    
    Returns:
        bool: True si la operación fue exitosa
    """
    conjunto_a = cargar_conjunto_disco(archivo_a)
    conjunto_b = cargar_conjunto_disco(archivo_b)
    
    resultado = conjunto_a.copy()
    for elemento in conjunto_b:
        if elemento not in resultado:
            resultado.append(elemento)
    
    return guardar_conjunto_disco(archivo_resultado, resultado)

def limpiar_conjunto_disco(nombre_archivo):
    """
    Elimina todos los elementos del conjunto en disco.
    
    Args:
        nombre_archivo (str): Nombre del archivo
    
    Returns:
        bool: True si se limpió correctamente
    """
    return guardar_conjunto_disco(nombre_archivo, [])

# ==================== FUNCIÓN DE DEMOSTRACIÓN ====================

def demostrar_conjunto_disco():
    """
    Demuestra el uso del ADT Conjunto con almacenamiento en disco.
    """
    print("=== ADT CONJUNTO - ALMACENAMIENTO EN DISCO ===")
    print("Los datos se guardan persistentemente en archivos JSON\n")
    
    # Nombres de archivos
    archivo_a = "conjunto_a.json"
    archivo_b = "conjunto_b.json"
    archivo_union = "conjunto_union.json"
    
    # Crear conjuntos iniciales
    print("1. CREANDO CONJUNTOS EN DISCO:")
    crear_conjunto_disco(archivo_a, [1, 2, 3, 4])
    crear_conjunto_disco(archivo_b, [3, 4, 5, 6])
    
    print(f"Conjunto A creado en: {archivo_a}")
    print(f"Conjunto B creado en: {archivo_b}")
    
    # Mostrar contenidos
    print(f"\n2. CONTENIDOS INICIALES:")
    print(f"A: {cargar_conjunto_disco(archivo_a)}")
    print(f"B: {cargar_conjunto_disco(archivo_b)}")
    
    # Operaciones básicas
    print(f"\n3. OPERACIONES BÁSICAS:")
    print(f"Tamaño de A: {obtener_tamano_disco(archivo_a)}")
    print(f"¿A contiene 3? {contiene_elemento_disco(archivo_a, 3)}")
    print(f"¿A está vacío? {esta_vacio_disco(archivo_a)}")
    
    # Modificar conjuntos
    print(f"\n4. MODIFICANDO CONJUNTOS:")
    agregar_elemento_disco(archivo_a, 7)
    eliminar_elemento_disco(archivo_a, 2)
    
    print(f"A después de modificar: {cargar_conjunto_disco(archivo_a)}")
    
    # Operación de unión
    print(f"\n5. OPERACIÓN DE UNIÓN:")
    union_disco(archivo_a, archivo_b, archivo_union)
    print(f"Unión A ∪ B: {cargar_conjunto_disco(archivo_union)}")
    
    # Persistencia de datos
    print(f"\n6. PERSISTENCIA DE DATOS:")
    print("Los datos permanecen en disco después de cerrar el programa")
    print("Puedes ver los archivos .json creados en el directorio actual")

def explicacion_adt_disco():
    """
    Explica cómo funciona el ADT Conjunto en disco.
    """
    print("\n" + "="*60)
    print("¿CÓMO FUNCIONA EL ADT CONJUNTO EN DISCO?")
    print("="*60)
    
    print("""
1. ALMACENAMIENTO PERSISTENTE:
   - Los datos se guardan en archivos JSON
   - Sobreviven al cierre del programa
   - Se pueden acceder desde múltiples ejecuciones

2. VENTAJAS:
   - Persistencia: Los datos no se pierden
   - Escalabilidad: Puede manejar grandes conjuntos
   - Portabilidad: Los archivos se pueden mover entre sistemas

3. DESVENTAJAS:
   - Más lento que memoria RAM
   - Mayor complejidad de implementación
   - Gestión de archivos necesaria

4. FLUJO DE OPERACIONES:
   - Para cada operación: CARGAR → PROCESAR → GUARDAR
   - Ejemplo al agregar elemento:
     1. Cargar lista desde archivo JSON
     2. Agregar elemento a la lista (si no existe)
     3. Guardar lista actualizada en el archivo

5. USOS TÍPICOS:
   - Bases de datos simples
   - Cache de datos
   - Configuraciones persistentes
   - Historial de operaciones
""")

# ==================== PROGRAMA PRINCIPAL ====================

if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    """
    # Demostración práctica
    demostrar_conjunto_disco()
    
    # Explicación teórica
    explicacion_adt_disco()
    
    print("\n=== DEMOSTRACIÓN COMPLETADA ===")
    print("Revisa los archivos .json creados en tu directorio")