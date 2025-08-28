# Simulación de Tráfico con Semáforos
import time
import random


class Semaforo:
    """Clase para representar un semáforo."""
    
    def __init__(self, id_semaforo):
        self.id = id_semaforo
        self.color = "rojo"
        self.tiempo_verde = 5
        self.tiempo_amarillo = 2
        self.tiempo_rojo = 4
    
    def cambiar_color(self):
        """Cambia el color del semáforo."""
        if self.color == "rojo":
            self.color = "verde"
            return self.tiempo_verde
        elif self.color == "verde":
            self.color = "amarillo"
            return self.tiempo_amarillo
        else:
            self.color = "rojo"
            return self.tiempo_rojo
    
    def __str__(self):
        """Representación en string del semáforo."""
        return f"Semaforo {self.id}: {self.color.upper()}"


class Auto:
    """Clase para representar un auto."""
    
    def __init__(self, id_auto):
        self.id = id_auto
        self.velocidad = random.randint(40, 80)
        self.en_movimiento = False
        self.avanza_amarillo = False
    
    def decidir_accion(self, semaforo):
        """Decide si avanzar o detenerse según el semáforo."""
        if semaforo.color == "verde":
            self.en_movimiento = True
            self.avanza_amarillo = False
        elif semaforo.color == "amarillo":
            # Autos más rápidos (>60 km/h) intentan pasar en amarillo
            if self.velocidad > 60:
                self.en_movimiento = True
                self.avanza_amarillo = True
            else:
                self.en_movimiento = False
                self.avanza_amarillo = False
        else:  # rojo
            self.en_movimiento = False
            self.avanza_amarillo = False
    
    def __str__(self):
        """Representación en string del auto."""
        estado = "EN MOVIMIENTO" if self.en_movimiento else "DETENIDO"
        mensaje = f"Auto {self.id}: {estado} ({self.velocidad} km/h)"
        
        if self.avanza_amarillo:
            mensaje += " ⚠️  PASA EN AMARILLO!"
        
        return mensaje


def simular_trafico():
    """Función principal de simulación."""
    print("🚦 SIMULADOR DE TRÁFICO INTELIGENTE")
    print("=" * 35)
    print("⚠️  Los autos >60 km/h intentan pasar en amarillo")
    print("=" * 35)
    
    # Crear semáforo y autos
    semaforo_principal = Semaforo(1)
    autos = [Auto(i) for i in range(1, 6)]  # 5 autos
    
    # Mostrar velocidades iniciales
    print("\nVelocidades de los autos:")
    for auto in autos:
        print(f"Auto {auto.id}: {auto.velocidad} km/h")
    
    # Simular 6 ciclos de semáforo
    for ciclo in range(1, 7):
        print(f"\n--- CICLO {ciclo} ---")
        
        # Cambiar semáforo y obtener duración
        duracion = semaforo_principal.cambiar_color()
        print(f"{semaforo_principal} (Duración: {duracion}s)")
        print("-" * 30)
        
        # Actualizar estado de autos
        for auto in autos:
            auto.decidir_accion(semaforo_principal)
            print(auto)
        
        # Pequeña pausa para ver la simulación
        time.sleep(1)
    
    print("\n🎯 Simulación completada!")
    print("📊 Resumen final:")
    for auto in autos:
        if auto.velocidad > 60:
            print(f"Auto {auto.id}: {auto.velocidad} km/h → CONDUCTOR AGRESIVO")
        else:
            print(f"Auto {auto.id}: {auto.velocidad} km/h → CONDUCTOR PRUDENTE")


def main():
    """Función principal del programa."""
    while True:
        print("\nOpciones:")
        print("1. Iniciar simulación de tráfico")
        print("2. Salir")
        
        opcion = input("Seleccione opción (1-2): ")
        
        if opcion == "1":
            simular_trafico()
        elif opcion == "2":
            print("¡Hasta luego! 🚗")
            break
        else:
            print("❌ Opción no válida")


if __name__ == '__main__':
    main()
