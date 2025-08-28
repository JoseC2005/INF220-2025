# Estructura Dinámica - Carrito de Compras
carrito = []
""" programa que simula un carrito de compras 
    usando una lista dinámica.
"""

def agregar_producto():
    """Función para agregar productos al carrito."""
    producto = input("Producto a agregar: ")
    carrito.append(producto)
    print(f"✅ {producto} agregado")


def ver_carrito():
    """Función para mostrar el contenido del carrito."""
    print("\n🛒 Carrito:", carrito)


def main():
    """Función principal del programa."""
    while True:
        print("\n1. Agregar producto")
        print("2. Ver carrito")
        print("3. Salir")
        opcion = input("Opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_carrito()
        elif opcion == "3":
            break


if __name__ == '__main__':
    main()
