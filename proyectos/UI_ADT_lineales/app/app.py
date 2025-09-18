from flask import Flask, render_template, request
import re
import os
from jinja2 import Environment

app = Flask(__name__)

@app.template_filter('set_operation')
def set_operation_filter(data):
    "set_operation_filter realiza operaciones de conjuntos."
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

# Variable global para almacenar el último resultado de operaciones con polinomios
ultimo_resultado = None


def parse_polinomio(expr: str) -> dict:
    """
    Convierte un polinomio en forma string a un diccionario {grado: coeficiente}.
    
    Args:
        expr (str): Expresión del polinomio (ej: '3x^2+2x-5')
        
    Returns:
        dict: Diccionario con los grados como claves y coeficientes como valores
    """
    expr = expr.replace(" ", "")  # Eliminar espacios
    # Asegurar que todos los términos tengan signo
    if expr[0] not in "+-":
        expr = "+" + expr

    # Expresión regular para separar coeficientes, x y potencias
    patron = re.findall(r'([+-]?\d*)(x(?:\^(\d+))?)?', expr)
    polinomio = {}

    for coef, x_term, exp in patron:
        if not coef and not x_term:
            continue
            
        # Procesar coeficiente
        if coef in ["", "+", "-"]:
            coef = 1 if coef != "-" else -1
        else:
            coef = int(coef)

        # Procesar exponente
        if x_term == "":
            grado = 0
        elif exp == "":
            grado = 1
        else:
            grado = int(exp)

        polinomio[grado] = polinomio.get(grado, 0) + coef

    return polinomio


def polinomio_to_str(p: dict) -> str:
    """
    Convierte un polinomio en diccionario a string ordenado.
    
    Args:
        p (dict): Diccionario con grados como claves y coeficientes como valores
        
    Returns:
        str: Representación en string del polinomio
    """
    if not p:
        return "0"
        
    terminos = []
    for grado in sorted(p.keys(), reverse=True):
        coef = p[grado]
        if coef == 0:
            continue
        if grado == 0:
            terminos.append(f"{coef}")
        elif grado == 1:
            terminos.append(f"{coef}x")
        else:
            terminos.append(f"{coef}x^{grado}")

    # Limpiar signos
    resultado = " + ".join(terminos)
    resultado = resultado.replace("+ -", "- ")
    return resultado


def suma_polinomios(p: dict, q: dict) -> dict:
    """
    Realiza la suma de dos polinomios.
    
    Args:
        p (dict): Primer polinomio
        q (dict): Segundo polinomio
        
    Returns:
        dict: Resultado de la suma
    """
    r = p.copy()
    for grado, coef in q.items():
        r[grado] = r.get(grado, 0) + coef
    return r


def resta_polinomios(p: dict, q: dict) -> dict:
    """
    Realiza la resta de dos polinomios (p - q).
    
    Args:
        p (dict): Primer polinomio
        q (dict): Segundo polinomio
        
    Returns:
        dict: Resultado de la resta
    """
    r = p.copy()
    for grado, coef in q.items():
        r[grado] = r.get(grado, 0) - coef
    return r


def multiplicar_polinomios(p: dict, q: dict) -> dict:
    """
    Realiza la multiplicación de dos polinomios.
    
    Args:
        p (dict): Primer polinomio
        q (dict): Segundo polinomio
        
    Returns:
        dict: Resultado de la multiplicación
    """
    r = {}
    for g1, c1 in p.items():
        for g2, c2 in q.items():
            r[g1 + g2] = r.get(g1 + g2, 0) + c1 * c2
    return r


def evaluar_polinomio(p: dict, x: float) -> float:
    """
    Evalúa un polinomio en un valor específico de x.
    
    Args:
        p (dict): Polinomio a evaluar
        x (float): Valor en el que evaluar el polinomio
        
    Returns:
        float: Resultado de la evaluación
    """
    return sum(coef * (x ** grado) for grado, coef in p.items())


@app.route('/')
def index():
    """Renderiza la página principal con los formularios para operaciones."""
    return render_template('index.html')


@app.route('/operacion_polinomio', methods=['POST'])
def operacion_polinomio():
    """
    Procesa las operaciones con polinomios.
    
    Operaciones soportadas:
    - suma: Suma de dos polinomios
    - resta: Resta de dos polinomios
    - multiplicacion: Multiplicación de dos polinomios
    - evaluacion: Evaluación de un polinomio en un valor específico de x
    
    Returns:
        Renderizado de la plantilla con los resultados
    """
    global ultimo_resultado
    
    # Obtener datos del formulario
    polinomio_p = request.form['polinomioP']
    polinomio_q = request.form['polinomioQ']
    operacion = request.form['operacion']
    valor_x = request.form.get('valorX')

    # Variables para la evaluación
    evaluando_polinomio = None
    valor_evaluacion = None
    resultado_evaluacion = None

    try:
        # Parsear los polinomios
        pol_p = parse_polinomio(polinomio_p)
        pol_q = parse_polinomio(polinomio_q)

        if operacion == "suma":
            resultado_polinomio = suma_polinomios(pol_p, pol_q)
            ultimo_resultado = resultado_polinomio
            resultado = polinomio_to_str(resultado_polinomio)
            
        elif operacion == "resta":
            resultado_polinomio = resta_polinomios(pol_p, pol_q)
            ultimo_resultado = resultado_polinomio
            resultado = polinomio_to_str(resultado_polinomio)
            
        elif operacion == "multiplicacion":
            resultado_polinomio = multiplicar_polinomios(pol_p, pol_q)
            ultimo_resultado = resultado_polinomio
            resultado = polinomio_to_str(resultado_polinomio)
            
        elif operacion == "evaluacion":
            if valor_x:
                x_val = float(valor_x)
                # Si ya hubo una operación antes, evaluamos ese resultado
                polinomio_a_evaluar = ultimo_resultado if ultimo_resultado else pol_p
                valor = evaluar_polinomio(polinomio_a_evaluar, x_val)
                resultado = f"Evaluación en x={x_val}: {valor}"
                
                # Guardar información específica para la evaluación
                evaluando_polinomio = polinomio_to_str(polinomio_a_evaluar)
                valor_evaluacion = x_val
                resultado_evaluacion = valor
            else:
                resultado = "Por favor ingrese un valor para x."
        else:
            resultado = "Operación no válida"

    except Exception as e:
        resultado = f"Error al procesar polinomio: {str(e)}"

    return render_template(
        'index.html',
        resultado_polinomios=resultado,
        polinomioP=polinomio_p,
        polinomioQ=polinomio_q,
        valorX=valor_x,
        polinomioR=polinomio_to_str(ultimo_resultado) if operacion != "evaluacion" else None,
        evaluando_polinomio=evaluando_polinomio,
        valor_evaluacion=valor_evaluacion,
        resultado_evaluacion=resultado_evaluacion
    )


@app.route('/operacion_conjunto', methods=['POST'])
def operacion_conjunto():
    """
    Procesa las operaciones con conjuntos.
    
    Operaciones soportadas:
    - union: Unión de dos conjuntos
    - interseccion: Intersección de dos conjuntos
    - diferencia: Diferencia entre dos conjuntos
    - diferencia_simetrica: Diferencia simétrica entre dos conjuntos
    
    Returns:
        Renderizado de la plantilla con los resultados
    """
    conjunto_a = request.form['conjuntoA']
    conjunto_b = request.form['conjuntoB']
    operacion = request.form['operacion']

    # Convertir strings a conjuntos de enteros
    try:
        set_a = list(map(int, conjunto_a.split(',')))
        set_b = list(map(int, conjunto_b.split(',')))
    except ValueError:
        return render_template(
            'index.html',
            resultado_conjuntos="Error: Los conjuntos deben contener solo números separados por comas",
            conjuntoA=conjunto_a,
            conjuntoB=conjunto_b
        )
    
    # Realizar la operación solicitada
    if operacion == "union":
        resultado = set(set_a).union(set_b)
    elif operacion == "interseccion":
        resultado = set(set_a).intersection(set_b)
    elif operacion == "diferencia":
        resultado = set(set_a).difference(set_b)
    elif operacion == "diferencia_simetrica":
        resultado = set(set_a).symmetric_difference(set_b)
    else:
        resultado = "Operación no válida"

    return render_template(
        'index.html',
        resultado_conjuntos=resultado,
        conjuntoA=conjunto_a,
        conjuntoB=conjunto_b,
        # Enviar datos para el diagrama
        set_a=set_a,
        set_b=set_b,
        operacion=operacion
    )


if __name__ == '__main__':
    # Obtener el puerto de las variables de entorno o usar 5000 por defecto
    port = int(os.environ.get("PORT", 5000))
    # Ejecutar la aplicación Flask
    app.run(host="0.0.0.0", port=port, debug=True)
