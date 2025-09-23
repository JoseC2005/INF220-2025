# models.py
import re


# ========== FILTROS PARA JINJA2 ==========
def set_operation_filter(data):
    """Realiza operaciones de conjuntos para templates."""
    set_a, set_b, operation = data
    set_a = set(set_a)
    set_b = set(set_b)
    
    if operation == "union":
        return list(set_a.union(set_b))
    elif operation == "interseccion":
        return list(set_a.intersection(set_b))
    elif operation == "diferencia":
        return list(set_a.difference(set_b))
    elif operation == "diferencia_simetrica":
        return list(set_a.symmetric_difference(set_b))
    return []


# ========== CLASE POLINOMIO ==========
class Polinomio:
    """Clase para manejar operaciones con polinomios."""
    
    def __init__(self, expresion=None, coeficientes=None):
        if expresion:
            self.coeficientes = self._parse_polinomio(expresion)
        elif coeficientes:
            self.coeficientes = coeficientes
        else:
            self.coeficientes = {}
    
    def _parse_polinomio(self, expr: str) -> dict:
        """Convierte string a diccionario {grado: coeficiente}."""
        expr = expr.replace(" ", "")
        if expr[0] not in "+-":
            expr = "+" + expr

        patron = re.findall(r'([+-]?\d*)(x(?:\^(\d+))?)?', expr)
        polinomio = {}

        for coef, x_term, exp in patron:
            if not coef and not x_term:
                continue
                
            if coef in ["", "+", "-"]:
                coef_val = 1 if coef != "-" else -1
            else:
                coef_val = int(coef)

            if x_term == "":
                grado = 0
            elif exp == "":
                grado = 1
            else:
                grado = int(exp)

            polinomio[grado] = polinomio.get(grado, 0) + coef_val

        return polinomio
    
    def to_string(self) -> str:
        """Convierte el polinomio a string."""
        if not self.coeficientes:
            return "0"
            
        terminos = []
        for grado in sorted(self.coeficientes.keys(), reverse=True):
            coef = self.coeficientes[grado]
            if coef == 0:
                continue
                
            if grado == 0:
                terminos.append(f"{coef}")
            elif grado == 1:
                terminos.append(f"{coef}x")
            else:
                terminos.append(f"{coef}x^{grado}")

        resultado = " + ".join(terminos)
        return resultado.replace("+ -", "- ")
    
    def suma(self, otro_polinomio):
        """Suma dos polinomios."""
        resultado = self.coeficientes.copy()
        for grado, coef in otro_polinomio.coeficientes.items():
            resultado[grado] = resultado.get(grado, 0) + coef
        return Polinomio(coeficientes=resultado)
    
    def resta(self, otro_polinomio):
        """Resta dos polinomios."""
        resultado = self.coeficientes.copy()
        for grado, coef in otro_polinomio.coeficientes.items():
            resultado[grado] = resultado.get(grado, 0) - coef
        return Polinomio(coeficientes=resultado)
    
    def multiplicar(self, otro_polinomio):
        """Multiplica dos polinomios."""
        resultado = {}
        for grado1, coef1 in self.coeficientes.items():
            for grado2, coef2 in otro_polinomio.coeficientes.items():
                nuevo_grado = grado1 + grado2
                resultado[nuevo_grado] = (
                    resultado.get(nuevo_grado, 0) + coef1 * coef2
                )
        return Polinomio(coeficientes=resultado)
    
    def evaluar(self, x: float) -> float:
        """Evalúa el polinomio en un valor x."""
        return sum(
            coef * (x ** grado) 
            for grado, coef in self.coeficientes.items()
        )


# ========== CLASE CONJUNTO ==========
class Conjunto:
    """Clase para manejar operaciones con conjuntos."""
    
    def __init__(self, elementos=None):
        if elementos:
            self.elementos = set(elementos)
        else:
            self.elementos = set()
    
    @classmethod
    def desde_string(cls, cadena: str):
        """Crea un conjunto desde string '1,2,3'."""
        try:
            elementos = list(map(int, cadena.split(',')))
            return cls(elementos)
        except ValueError:
            raise ValueError(
                "Los conjuntos deben contener solo números separados por comas"
            )
    
    def union(self, otro_conjunto):
        """Unión de conjuntos."""
        return Conjunto(self.elementos.union(otro_conjunto.elementos))
    
    def interseccion(self, otro_conjunto):
        """Intersección de conjuntos."""
        return Conjunto(self.elementos.intersection(otro_conjunto.elementos))
    
    def diferencia(self, otro_conjunto):
        """Diferencia de conjuntos."""
        return Conjunto(self.elementos.difference(otro_conjunto.elementos))
    
    def diferencia_simetrica(self, otro_conjunto):
        """Diferencia simétrica de conjuntos."""
        return Conjunto(
            self.elementos.symmetric_difference(otro_conjunto.elementos)
        )
    
    def to_list(self):
        """Convierte a lista ordenada."""
        return sorted(list(self.elementos))
    
    def __str__(self):
        return str(self.to_list())


# Variable global para polinomios (podría mejorarse con sesiones)
ultimo_resultado_polinomio = None