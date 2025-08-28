#estructuras estaticas
#listas,tuplas y diccionarios
""" Ejemplo de estructura estatica: usando
    listas, tuplas y diccionarios.
    En esta ocacion solamente usare algunos
    elementos de cada estructura.
    Diccionario de 3 libros con su autor,titulo
    y stock.
"""
Libro = {
        '001':{'autor':'Mollo Alberto Mamani',
                'titulo':'Programacion 1',
                'stock': 4},
        '002':{'autor':'Juan Carlos Contreras',
                'titulo':'programacion 2',
                'stock': 6},
        '003':{'autor':'Vallet Corrado',
                'titulo':'Ensamblador',
                'stock': 2}
        }


def mostrar_libros():
    """funcion para mostrar los libros"""
    print('\n Los libros disponibles son:')
    print('#'*30)
    for clave,valor in Libro.items():
        print(f'clave: {clave}')
        print(f'  autor: {valor["autor"]}')
        print(f'  titulo: {valor["titulo"]}')
        print(f'  stock: {valor["stock"]}')
        print('-' * 30)


def comprar_libro():
    """funcion para comprar un libro"""
    codigo = input("Ingresa el código del libro a comprar: ")
    
    if codigo in Libro:
        if Libro[codigo]['stock'] > 0:
            Libro[codigo]['stock'] -= 1
            print(f"✅ Compra exitosa de: {Libro[codigo]['titulo']}")
            print(f"   Stock restante: {Libro[codigo]['stock']}")
        else:
            print("❌ No hay stock disponible")
    else:
        print("❌ Código no válido")


def main():
    """funcion principal donde voy a elegir el libro
    que quiero comprar y luego mostrar el stock
    """
    print("📚 SISTEMA DE LIBROS")
    print("=" * 20)
    
    while True:
        print("\nOpciones:")
        print("1. Ver libros")
        print("2. Comprar libro") 
        print("3. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            mostrar_libros()
        elif opcion == "2":
            comprar_libro()
        elif opcion == "3":
            print("¡Hasta luego! 👋")
            break
        else:
            print("Opción no válida")


if __name__ == '__main__':
    main()
