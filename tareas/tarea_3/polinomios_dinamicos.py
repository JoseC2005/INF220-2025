class Termino:
    def __init__(self, coeficiente, grado):
        self.coeficiente = coeficiente
        self.grado = grado
        self.siguiente = None

class PolinomioDinamico:
    def __init__(self):
        self.cabeza = None
    
    # Setter para agregar término
    def agregar_termino(self, coeficiente, grado):
        if coeficiente == 0:
            return
        
        # Buscar si ya existe término de ese grado
        actual = self.cabeza
        anterior = None
        while actual is not None:
            if actual.grado == grado:
                actual.coeficiente += coeficiente
                if actual.coeficiente == 0:
                    # Eliminar término si coeficiente queda en 0
                    if anterior is None:
                        self.cabeza = actual.siguiente
                    else:
                        anterior.siguiente = actual.siguiente
                return
            anterior = actual
            actual = actual.siguiente
        
        # Insertar nuevo término en orden descendente
        nuevo_termino = Termino(coeficiente, grado)
        if self.cabeza is None or grado > self.cabeza.grado:
            nuevo_termino.siguiente = self.cabeza
            self.cabeza = nuevo_termino
        else:
            actual = self.cabeza
            while actual.siguiente is not None and actual.siguiente.grado > grado:
                actual = actual.siguiente
            nuevo_termino.siguiente = actual.siguiente
            actual.siguiente = nuevo_termino
    
    # Getter para obtener coeficiente de un grado
    def get_coeficiente(self, grado):
        actual = self.cabeza
        while actual is not None:
            if actual.grado == grado:
                return actual.coeficiente
            actual = actual.siguiente
        return 0
    
    # Getter para obtener el grado máximo
    def get_grado(self):
        if self.cabeza is None:
            return 0
        return self.cabeza.grado
    
    # Evaluar el polinomio en un punto x
    def evaluar(self, x):
        resultado = 0
        actual = self.cabeza
        while actual is not None:
            resultado += actual.coeficiente * (x ** actual.grado)
            actual = actual.siguiente
        return resultado
    
    # Sumar dos polinomios
    def sumar(self, otro_polinomio):
        resultado = PolinomioDinamico()
        
        # Agregar términos del primer polinomio
        actual = self.cabeza
        while actual is not None:
            resultado.agregar_termino(actual.coeficiente, actual.grado)
            actual = actual.siguiente
        
        # Agregar términos del segundo polinomio
        actual_otro = otro_polinomio.cabeza
        while actual_otro is not None:
            resultado.agregar_termino(actual_otro.coeficiente, actual_otro.grado)
            actual_otro = actual_otro.siguiente
        
        return resultado
    
    # Multiplicar dos polinomios
    def multiplicar(self, otro_polinomio):
        resultado = PolinomioDinamico()
        
        actual1 = self.cabeza
        while actual1 is not None:
            actual2 = otro_polinomio.cabeza
            while actual2 is not None:
                coef = actual1.coeficiente * actual2.coeficiente
                grado = actual1.grado + actual2.grado