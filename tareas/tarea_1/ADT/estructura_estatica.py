"""Aqui estoy presentando un ejemplo de ADT 
    de estrucutura estatica en python
    Módulo: estructura_estatica.py
"""

# ADT Estático para Automóvil con getters y setters

# ==================== OPERACIONES ====================

def crear_auto(marca, modelo, año, color, precio):
    """Crea la estructura de un automóvil"""
    return {
        'marca': marca,
        'modelo': modelo, 
        'año': año,
        'color': color,
        'precio': precio
    }

# GETTERS (obtener valores)
def get_marca(auto):
    return auto['marca']

def get_modelo(auto):
    return auto['modelo']

def get_año(auto):
    return auto['año']

def get_color(auto):
    return auto['color']

def get_precio(auto):
    return auto['precio']

# SETTERS (modificar valores - retornan NUEVO auto)
def set_marca(auto, nueva_marca):
    nuevo_auto = auto.copy()
    nuevo_auto['marca'] = nueva_marca
    return nuevo_auto

def set_modelo(auto, nuevo_modelo):
    nuevo_auto = auto.copy()
    nuevo_auto['modelo'] = nuevo_modelo
    return nuevo_auto

def set_año(auto, nuevo_año):
    nuevo_auto = auto.copy()
    nuevo_auto['año'] = nuevo_año
    return nuevo_auto

def set_color(auto, nuevo_color):
    nuevo_auto = auto.copy()
    nuevo_auto['color'] = nuevo_color
    return nuevo_auto

def set_precio(auto, nuevo_precio):
    nuevo_auto = auto.copy()
    nuevo_auto['precio'] = nuevo_precio
    return nuevo_auto

def mostrar_info(auto):
    """Muestra información del automóvil"""
    return f"{get_marca(auto)} {get_modelo(auto)} ({get_año(auto)}) - {get_color(auto)} - ${get_precio(auto)}"

# ==================== EJEMPLO DE USO ====================

def ejemplo_uso():
    """Ejemplo de uso con getters y setters"""
    
    # Crear automóvil
    mi_auto = crear_auto("Toyota", "Corolla", 2023, "Rojo", 25000.0)
    
    print("=== AUTO ORIGINAL ===")
    print(mostrar_info(mi_auto))
    
    # Usar getters
    print(f"\nUsando getters:")
    print(f"Marca: {get_marca(mi_auto)}")
    print(f"Modelo: {get_modelo(mi_auto)}")
    print(f"Precio: ${get_precio(mi_auto)}")
    
    # Usar setters (crean nuevo auto)
    print(f"\n=== MODIFICANDO AUTO ===")
    mi_auto = set_color(mi_auto, "Azul")
    mi_auto = set_precio(mi_auto, 23000.0)
    mi_auto = set_modelo(mi_auto, "Camry")
    
    print(mostrar_info(mi_auto))
    print(f"Nuevo modelo: {get_modelo(mi_auto)}")

# Ejecutar ejemplo
if __name__ == "__main__":
    ejemplo_uso()
