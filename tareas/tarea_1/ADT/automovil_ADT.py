"""
Módulo: automovil_ADT.py
Ejemplo simplificado de ADT Híbrido en Python.
Incluye atributos estáticos (marca, modelo, color, año)
y dinámicos (historial de mantenimientos).
"""


class Automovil:
    """
    Clase que representa un automóvil.
    - Atributos estáticos: marca, modelo, color, año.
    - Atributos dinámicos: historial de mantenimientos.
    """

    def __init__(self, marca, modelo, color, anio):
        """Constructor del automóvil."""
        self.marca = marca            # Público
        self._modelo = modelo         # Protegido
        self._color = color           # Protegido
        self._anio = anio             # Protegido
        self.__historial = []         # Privado

    # ----- Métodos tipo GET -----
    def mostrar_info(self):
        return f"{self.marca} {self._modelo} ({self._color}, {self._anio})"

    def mostrar_historial(self):
        if not self.__historial:
            return "Sin mantenimientos."
        return "\n".join([f"- {m['fecha']}: {m['descripcion']}" for m in self.__historial])

    # ----- Métodos tipo SET -----
    def cambiar_color(self, nuevo_color):
        self._color = nuevo_color

    # ----- Métodos dinámicos -----
    def registrar_mantenimiento(self, fecha, descripcion):
        self.__historial.append({"fecha": fecha, "descripcion": descripcion})


# --------------------- PROGRAMA PRINCIPAL ---------------------
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar auto")
    print("2. Listar autos")
    print("3. Registrar mantenimiento")
    print("4. Salir")


if __name__ == "__main__":
    autos = []

    while True:
        mostrar_menu()
        opcion = input("Opción: ")

        if opcion == "1":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            color = input("Color: ")
            anio = int(input("Año: "))
            autos.append(Automovil(marca, modelo, color, anio))
            print("✅ Auto agregado.")

        elif opcion == "2":
            if not autos:
                print("⚠️ No hay autos.")
            else:
                for i, auto in enumerate(autos, 1):
                    print(f"{i}. {auto.mostrar_info()}")

        elif opcion == "3":
            if not autos:
                print("⚠️ No hay autos.")
            else:
                for i, auto in enumerate(autos, 1):
                    print(f"{i}. {auto.mostrar_info()}")
                idx = int(input("Seleccione auto: ")) - 1
                fecha = input("Fecha (YYYY-MM-DD): ")
                descripcion = input("Descripción: ")
                autos[idx].registrar_mantenimiento(fecha, descripcion)
                print("✅ Mantenimiento registrado.")
                print(autos[idx].mostrar_historial())

        elif opcion == "4":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida.")
