def crear_polinomio(grado_maximo):
    """Crea un polinomio estático"""
    return {
        'grado_maximo': grado_maximo,
        'coeficientes': [0] * (grado_maximo + 1)
    }

def set_coeficiente(polinomio, grado, coeficiente):
    """Establece el coeficiente para un grado específico"""
    if 0 <= grado <= polinomio['grado_maximo']:
        polinomio['coeficientes'][grado] = coeficiente
        return True
    return False

def get_coeficiente(polinomio, grado):
    """Obtiene el coeficiente de un grado específico"""
    if 0 <= grado <= polinomio['grado_maximo']:
        return polinomio['coeficientes'][grado]
    return 0

def get_grado_real(polinomio):
    """Obtiene el grado real del polinomio"""
    for i in range(polinomio['grado_maximo'], -1, -1):
        if polinomio['coeficientes'][i] != 0:
            return i
    return 0

def evaluar_polinomio(polinomio, x):
    """Evalúa el polinomio en un punto x"""
    resultado = 0
    for grado in range(polinomio['grado_maximo'] + 1):
        resultado += polinomio['coeficientes'][grado] * (x ** grado)
    return resultado

def sumar_polinomios(polinomio1, polinomio2):
    """Suma dos polinomios"""
    nuevo_grado = max(polinomio1['grado_maximo'], polinomio2['grado_maximo'])
    nuevo_polinomio = crear_polinomio(nuevo_grado)
    
    for i in range(nuevo_grado + 1):
        coef1 = get_coeficiente(polinomio1, i)
        coef2 = get_coeficiente(polinomio2, i)
        set_coeficiente(nuevo_polinomio, i, coef1 + coef2)
    
    return nuevo_polinomio

def multiplicar_polinomios(polinomio1, polinomio2):
    """Multiplica dos polinomios"""
    nuevo_grado = polinomio1['grado_maximo'] + polinomio2['grado_maximo']
    nuevo_polinomio = crear_polinomio(nuevo_grado)
    
    for i in range(polinomio1['grado_maximo'] + 1):
        for j in range(polinomio2['grado_maximo'] + 1):
            coef_actual = get_coeficiente(polinomio1, i) * get_coeficiente(polinomio2, j)
            nuevo_coef = get_coeficiente(nuevo_polinomio, i + j) + coef_actual
            set_coeficiente(nuevo_polinomio, i + j, nuevo_coef)
    
    return nuevo_polinomio

def derivar_polinomio(polinomio):
    """Deriva el polinomio"""
    if polinomio['grado_maximo'] == 0:
        return crear_polinomio(0)
    
    nuevo_polinomio = crear_polinomio(polinomio['grado_maximo'] - 1)
    for i in range(1, polinomio['grado_maximo'] + 1):
        nuevo_coef = polinomio['coeficientes'][i] * i
        set_coeficiente(nuevo_polinomio, i - 1, nuevo_coef)
    
    return nuevo_polinomio

def polinomio_a_string(polinomio):
    """Convierte el polinomio a string"""
    terms = []
    for grado in range(polinomio['grado_maximo'], -1, -1):
        coef = polinomio['coeficientes'][grado]
        if coef != 0:
            if grado == 0:
                terms.append(f"{coef}")
            elif grado == 1:
                terms.append(f"{coef}x")
            else:
                terms.append(f"{coef}x^{grado}")
    return " + ".join(terms) if terms else "0"