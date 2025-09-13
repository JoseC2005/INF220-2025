from flask import Flask, render_template, request
import re
import os

app = Flask(__name__)

# -------------------------------
# 🔹 Funciones auxiliares para polinomios
# -------------------------------

def parse_polinomio(expr: str) -> dict:
    """
    Convierte un polinomio en forma string (ej: '3x^2+2x-5')
    a un diccionario {grado: coeficiente}.
    """
    expr = expr.replace(" ", "")  # quitar espacios
    # Asegurar que todos los términos tengan signo
    if expr[0] not in "+-":
        expr = "+" + expr

    # Expresión regular para separar coeficientes, x y potencias
    patron = re.findall(r'([+-]?\d*)(x(?:\^(\d+))?)?', expr)
    polinomio = {}

    for coef, x_term, exp in patron:
        if not coef and not x_term:
            continue
        # coeficiente
        if coef in ["", "+", "-"]:
            coef = 1 if coef != "-" else -1
        else:
            coef = int(coef)

        # exponente
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
    Convierte un polinomio en dict {grado: coef} a string ordenado.
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

    # limpiar signos
    resultado = " + ".join(terminos)
    resultado = resultado.replace("+ -", "- ")
    return resultado


def suma_polinomios(p, q):
    r = p.copy()
    for grado, coef in q.items():
        r[grado] = r.get(grado, 0) + coef
    return r


def resta_polinomios(p, q):
    r = p.copy()
    for grado, coef in q.items():
        r[grado] = r.get(grado, 0) - coef
    return r


def multiplicar_polinomios(p, q):
    r = {}
    for g1, c1 in p.items():
        for g2, c2 in q.items():
            r[g1+g2] = r.get(g1+g2, 0) + c1*c2
    return r


def evaluar_polinomio(p, x: float):
    return sum(coef * (x**grado) for grado, coef in p.items())

# -------------------------------
# 🔹 Rutas Flask
# -------------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/operacion_polinomio', methods=['POST'])
def operacion_polinomio():
    global ultimo_resultado
    polinomioP = request.form['polinomioP']
    polinomioQ = request.form['polinomioQ']
    operacion = request.form['operacion']
    valorX = request.form.get('valorX')

    try:
        P = parse_polinomio(polinomioP)
        Q = parse_polinomio(polinomioQ)

        if operacion == "suma":
            R = suma_polinomios(P, Q)
            ultimo_resultado = R
            resultado = polinomio_to_str(R)
        elif operacion == "resta":
            R = resta_polinomios(P, Q)
            ultimo_resultado = R
            resultado = polinomio_to_str(R)
        elif operacion == "multiplicacion":
            R = multiplicar_polinomios(P, Q)
            ultimo_resultado = R
            resultado = polinomio_to_str(R)
        elif operacion == "evaluacion":
            if valorX:
                x = float(valorX)
                # Si ya hubo una operación antes, evaluamos ese resultado
                pol_a_eval = ultimo_resultado if ultimo_resultado else P
                valor = evaluar_polinomio(pol_a_eval, x)
                resultado = f"Evaluación en x={x}: {valor}"
            else:
                resultado = "Por favor ingrese un valor para x."
        else:
            resultado = "Operación no válida"

    except Exception as e:
        resultado = f"Error al procesar polinomio: {str(e)}"

    return render_template(
        'index.html',
        resultado_polinomios=resultado,
        polinomioP=polinomioP,
        polinomioQ=polinomioQ,
        valorX=valorX
    )

@app.route('/operacion_conjunto', methods=['POST'])
def operacion_conjunto():
    conjuntoA = request.form['conjuntoA']
    conjuntoB = request.form['conjuntoB']
    operacion = request.form['operacion']

    A = set(map(int, conjuntoA.split(',')))
    B = set(map(int, conjuntoB.split(',')))

    if operacion == "union":
        resultado = A.union(B)
    elif operacion == "interseccion":
        resultado = A.intersection(B)
    elif operacion == "diferencia":
        resultado = A.difference(B)
    elif operacion == "diferencia_simetrica":
        resultado = A.symmetric_difference(B)
    else:
        resultado = "Operación no válida"

    return render_template(
        'index.html',
        resultado_conjuntos=resultado,
        conjuntoA=conjuntoA,
        conjuntoB=conjuntoB
    )

# -------------------------------
# 🔹 Punto de entrada
# -------------------------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)