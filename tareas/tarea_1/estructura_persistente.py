# Estructura Persistente - Lista de Tareas
""" importamos la libreria json para manejar archivos JSON
    para mas simplicidad en la persistencia de datos y de
    paso os para poder eliminar el json porque no es un
    archivo que nos interese en realidad.
"""
import json
import os


""" Programa que simula una lista de tareas persistente
    usando un archivo JSON.
"""

def cargar_tareas():
    """Carga las tareas desde el archivo JSON."""
    try:
        with open('tareas.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def guardar_tareas(tareas):
    """Guarda las tareas en el archivo JSON."""
    with open('tareas.json', 'w') as archivo:
        json.dump(tareas, archivo, indent=4)


def eliminar_archivo():
    """Elimina el archivo JSON si existe."""
    if os.path.exists('tareas.json'):
        os.remove('tareas.json')
        print("🗑️ Archivo tareas.json eliminado")
    else:
        print("❌ El archivo no existe")


def agregar_tarea():
    """Agrega una nueva tarea a la lista."""
    tarea = input("Nueva tarea: ")
    tareas = cargar_tareas()
    tareas.append(tarea)
    guardar_tareas(tareas)
    print(f"✅ Tarea agregada: {tarea}")


def ver_tareas():
    """Muestra todas las tareas guardadas."""
    tareas = cargar_tareas()
    print("\n📝 Lista de Tareas:")
    print("=" * 30)
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea}")
    print("=" * 30)


def main():
    """Función principal del programa."""
    print("✅ SISTEMA DE TAREAS PERSISTENTE")
    print("=" * 35)
    
    while True:
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Eliminar archivo JSON")
        print("4. Salir")
        
        opcion = input("Seleccione opción (1-4): ")
        
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            eliminar_archivo()
        elif opcion == "4":
            print("¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción no válida")


if __name__ == '__main__':
    main()
