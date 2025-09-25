"""
ADT Polinomio (ESTÁTICO) — sin __init__, sin clases.
Representación: {"cap": max_grado+1, "coef": [0]*cap} ; coef[e] = coef de x^e
"""

from typing import Dict, Any, List, Tuple


# ---------- creación ----------
def crear_polinomio(max_grado: int = 20) -> Dict[str, Any]:
    cap = max(0, int(max_grado)) + 1
    return {"cap": cap, "coef": [0] * cap}


# ---------- helpers ----------
def _check_exp(P: Dict[str, Any], e: int) -> None:
    if e < 0 or e >= P["cap"]:
        raise ValueError("Exponente fuera de rango para estructura estática.")


def grado(P: Dict[str, Any]) -> int:
    for e in range(P["cap"] - 1, -1, -1):
        if P["coef"][e] != 0:
            return e
    return -1


def get_coef(P: Dict[str, Any], e: int) -> int | float:
    _check_exp(P, e)
    return P["coef"][e]


def set_coef(P: Dict[str, Any], e: int, c: int | float) -> None:
    _check_exp(P, e)
    P["coef"][e] = c


def evaluar(P: Dict[str, Any], x: int | float) -> int | float:
    res = 0
    for e in range(P["cap"] - 1, -1, -1):
        res = res * x + P["coef"][e]
    return res


def a_lista(P: Dict[str, Any]) -> List[Tuple[int | float, int]]:
    return [(P["coef"][e], e) for e in range(P["cap"]) if P["coef"][e] != 0]


# ---------- operaciones ----------
def sumar(A: Dict[str, Any], B: Dict[str, Any]) -> Dict[str, Any]:
    C = crear_polinomio(max(A["cap"], B["cap"]) - 1)
    m = min(A["cap"], B["cap"])
    for e in range(m):
        C["coef"][e] = A["coef"][e] + B["coef"][e]
    if A["cap"] > m:
        for e in range(m, A["cap"]):
            C["coef"][e] = A["coef"][e]
    if B["cap"] > m:
        for e in range(m, B["cap"]):
            C["coef"][e] += B["coef"][e]
    return C


def restar(A: Dict[str, Any], B: Dict[str, Any]) -> Dict[str, Any]:
    C = crear_polinomio(max(A["cap"], B["cap"]) - 1)
    m = min(A["cap"], B["cap"])
    for e in range(m):
        C["coef"][e] = A["coef"][e] - B["coef"][e]
    if A["cap"] > m:
        for e in range(m, A["cap"]):
            C["coef"][e] = A["coef"][e]
    if B["cap"] > m:
        for e in range(m, B["cap"]):
            C["coef"][e] -= B["coef"][e]
    return C


def multiplicar(A: Dict[str, Any], B: Dict[str, Any]) -> Dict[str, Any]:
    cap_c = A["cap"] + B["cap"] - 2  # grado máx = (cap-1)+(cap-1)
    C = crear_polinomio(cap_c)
    for i in range(A["cap"]):
        ai = A["coef"][i]
        if ai == 0:
            continue
        for j in range(B["cap"]):
            bj = B["coef"][j]
            if bj == 0:
                continue
            C["coef"][i + j] += ai * bj
    return C


# ---------- CLI simple ----------
def _leer_pares(prompt: str) -> List[Tuple[float, int]]:
    """
    Lee pares 'coef exp' separados por comas o espacios.
    Ej: 3 0, 2 2  ->  3*x^0 + 2*x^2
    """
    linea = input(prompt).strip()
    if not linea:
        return []
    piezas = linea.replace(",", " ").split()
    if len(piezas) % 2 != 0:
        raise ValueError("Cantidad impar de números; use pares 'coef exp'.")
    pares: List[Tuple[float, int]] = []
    for i in range(0, len(piezas), 2):
        c = float(piezas[i])
        e = int(piezas[i + 1])
        pares.append((c, e))
    return pares


def _formatear(pares: List[Tuple[float, int]]) -> str:
    if not pares:
        return "0"
    partes: List[str] = []
    for c, e in sorted(pares, key=lambda t: t[1], reverse=True):
        if e == 0:
            partes.append(f"{c:g}")
        elif e == 1:
            partes.append(f"{c:g}x")
        else:
            partes.append(f"{c:g}x^{e}")
    return " + ".join(partes).replace("+ -", "- ")


if __name__ == "__main__":
    print("Polinomio ESTÁTICO (sin __init__). Ingresa tus términos.")
    a_pares = _leer_pares("A como 'coef exp' (ej: 3 0, 2 2): ")
    b_pares = _leer_pares("B como 'coef exp' (ej: 1 1, -2 2): ")

    max_g = 0
    for _, e in a_pares + b_pares:
        max_g = max(max_g, e)
    A = crear_polinomio(max_g)
    B = crear_polinomio(max_g)

    for c, e in a_pares:
        set_coef(A, e, get_coef(A, e) + c)
    for c, e in b_pares:
        set_coef(B, e, get_coef(B, e) + c)

    S = sumar(A, B)
    R = restar(A, B)
    M = multiplicar(A, B)

    print("A(x) =", _formatear(a_lista(A)))
    print("B(x) =", _formatear(a_lista(B)))
    print("A+B  =", _formatear(a_lista(S)))
    print("A-B  =", _formatear(a_lista(R)))
    print("A*B  =", _formatear(a_lista(M)))
    x_val = float(input("Evalúa en x = ") or "0")
    print("A(x) =", evaluar(A, x_val))
