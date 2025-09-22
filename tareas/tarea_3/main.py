from conjuntos_estaticos import *
from conjuntos_dinamicos import ConjuntoDinamico
from polinomios_estatico import *
from polinomios_dinamicos import PolinomioDinamico

def prueba_conjuntos_estaticos():
    print("=== Conjuntos Estáticos ===")
    conj1 = crear_conjunto(5)
    conj2 = crear_conjunto(5)
    
    agregar_elemento(conj1, 1)
    agregar_elemento(conj1, 2)
    agregar_elemento(conj1, 3)
    
    agregar_elemento(conj2, 3)
    agregar_elemento(conj2, 4)
    agregar_elemento(conj2, 5)
    
    print("Conjunto 1:", conjunto_a_string(conj1))
    print("Conjunto 2:", conjunto_a_string(conj2))
    print("Unión:", conjunto_a_string(union_conjuntos(conj1, conj2)))
    print("Intersección:", conjunto_a_string(interseccion_conjuntos(conj1, conj2)))

def prueba_polinomios_estaticos():
    print("\n=== Polinomios Estáticos ===")
    poly1 = crear_polinomio(3)
    set_coeficiente(poly1, 3, 2)  # 2x³
    set_coeficiente(poly1, 1, 4)  # + 4x
    
    poly2 = crear_polinomio(2)
    set_coeficiente(poly2, 2, 1)  # x²
    set_coeficiente(poly2, 0, 5)  # + 5
    
    print("Polinomio 1:", polinomio_a_string(poly1))
    print("Polinomio 2:", polinomio_a_string(poly2))
    print("Suma:", polinomio_a_string(sumar_polinomios(poly1, poly2)))

if __name__ == "__main__":
    prueba_conjuntos_estaticos()
    prueba_polinomios_estaticos()