"""Ahora vamos a implementar las estructuras
    dinamicas vistas en clase. 
    Usaremos setters y getter e instanciamos
    las clases.
"""

class Auto:
    """ADT Dinámico simple para Automóvil."""
    
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
    
    def get_marca(self):
        """Obtiene la marca del automóvil."""
        return self.marca
    
    def get_modelo(self):
        """Obtiene el modelo del automóvil."""
        return self.modelo
    
    def get_año(self):
        """Obtiene el año del automóvil."""
        return self.año
    
    def get_precio(self):
        """Obtiene el precio del automóvil."""
        return self.precio
    
    def set_marca(self, nueva_marca):
        """Modifica la marca del automóvil."""
        self.marca = nueva_marca
    
    def set_modelo(self, nuevo_modelo):
        """Modifica el modelo del automóvil."""
        self.modelo = nuevo_modelo
    
    def set_año(self, nuevo_año):
        """Modifica el año del automóvil."""
        self.año = nuevo_año
    
    def set_precio(self, nuevo_precio):
        """Modifica el precio del automóvil."""
        self.precio = nuevo_precio
    
    def mostrar_info(self):
        """Muestra información del automóvil."""
        return f"{self.marca} {self.modelo} ({self.año}) - ${self.precio}"


def main():
    """Función principal para demostrar el ADT dinámico."""
    mi_auto = Auto("Toyota", "Corolla", 2023, 25000)
    
    print("Auto original:")
    print(mi_auto.mostrar_info())
    
    # Usando setters (modifican el objeto)
    mi_auto.set_precio(23000)
    mi_auto.set_modelo("Camry")
    
    print("\nAuto modificado:")
    print(mi_auto.mostrar_info())
    
    # Usando getters
    print(f"\nMarca: {mi_auto.get_marca()}")
    print(f"Precio actual: ${mi_auto.get_precio()}")


if __name__ == '__main__':
    main()
