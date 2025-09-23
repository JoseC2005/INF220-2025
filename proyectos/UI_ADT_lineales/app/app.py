from flask import Flask, render_template, request
import os
from modelos import (
    Polinomio, 
    Conjunto, 
    set_operation_filter, 
    ultimo_resultado_polinomio
)

app = Flask(__name__)

# Registrar filtro personalizado
app.jinja_env.filters['set_operation'] = set_operation_filter


# ========== RUTAS ==========
@app.route('/')
def index():
    """Página principal."""
    return render_template('index.html')


@app.route('/operacion_polinomio', methods=['POST'])
def operacion_polinomio():
    """Procesa operaciones con polinomios."""
    global ultimo_resultado_polinomio

    polinomio_p_str = request.form['polinomioP']
    polinomio_q_str = request.form['polinomioQ']
    operacion = request.form['operacion']
    valor_x = request.form.get('valorX')

    try:
        # Crear objetos Polinomio (Modelo)
        pol_p = Polinomio(polinomio_p_str)
        pol_q = Polinomio(polinomio_q_str)

        resultado = ""
        polinomio_resultado = None

        if operacion == "suma":
            polinomio_resultado = pol_p.suma(pol_q)
            resultado = polinomio_resultado.to_string()

        elif operacion == "resta":
            polinomio_resultado = pol_p.resta(pol_q)
            resultado = polinomio_resultado.to_string()

        elif operacion == "multiplicacion":
            polinomio_resultado = pol_p.multiplicar(pol_q)
            resultado = polinomio_resultado.to_string()

        elif operacion == "evaluacion":
            if valor_x and valor_x.strip():
                x_val = float(valor_x)
                if ultimo_resultado_polinomio:
                    polinomio_a_evaluar = Polinomio(
                        coeficientes=ultimo_resultado_polinomio
                    )
                else:
                    polinomio_a_evaluar = pol_p
                valor = polinomio_a_evaluar.evaluar(x_val)
                resultado = f"Evaluación en x={x_val}: {valor}"
            else:
                resultado = "Por favor ingrese un valor para x."

        # Guardar último resultado
        if polinomio_resultado and operacion != "evaluacion":
            ultimo_resultado_polinomio = polinomio_resultado.coeficientes

    except Exception as e:
        resultado = f"Error: {str(e)}"

    # Preparar polinomioR para mostrar
    polinomio_r = None
    if ultimo_resultado_polinomio:
        polinomio_r = Polinomio(
            coeficientes=ultimo_resultado_polinomio
        ).to_string()

    return render_template(
        'index.html',
        resultado_polinomios=resultado,
        polinomioP=polinomio_p_str,
        polinomioQ=polinomio_q_str,
        valorX=valor_x,
        polinomioR=polinomio_r
    )


@app.route('/operacion_conjunto', methods=['POST'])
def operacion_conjunto():
    """Procesa operaciones con conjuntos."""
    conjunto_a_str = request.form['conjuntoA']
    conjunto_b_str = request.form['conjuntoB']
    operacion = request.form['operacion']

    try:
        # Crear objetos Conjunto (Modelo)
        conjunto_a = Conjunto.desde_string(conjunto_a_str)
        conjunto_b = Conjunto.desde_string(conjunto_b_str)

        if operacion == "union":
            resultado_conjunto = conjunto_a.union(conjunto_b)
        elif operacion == "interseccion":
            resultado_conjunto = conjunto_a.interseccion(conjunto_b)
        elif operacion == "diferencia":
            resultado_conjunto = conjunto_a.diferencia(conjunto_b)
        elif operacion == "diferencia_simetrica":
            resultado_conjunto = conjunto_a.diferencia_simetrica(conjunto_b)
        else:
            resultado_conjunto = "Operación no válida"

        if hasattr(resultado_conjunto, 'to_list'):
            resultado = resultado_conjunto.to_list()
        else:
            resultado = resultado_conjunto

    except ValueError as e:
        resultado = str(e)
    except Exception as e:
        resultado = f"Error: {str(e)}"

    # Preparar conjuntos para mostrar en template
    set_a = []
    set_b = []
    if 'conjunto_a' in locals():
        set_a = conjunto_a.to_list()
    if 'conjunto_b' in locals():
        set_b = conjunto_b.to_list()

    return render_template(
        'index.html',
        resultado_conjuntos=resultado,
        conjuntoA=conjunto_a_str,
        conjuntoB=conjunto_b_str,
        set_a=set_a,
        set_b=set_b,
        operacion=operacion
    )


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)