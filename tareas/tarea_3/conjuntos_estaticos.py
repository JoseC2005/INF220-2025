"""
ADT Conjunto (ESTÁTICO) — sin __init__, sin clases.
Representación: dict {"cap": C, "datos": [None]*C, "n": k}
"""

from typing import Iterable, List, Dict, Any


# ---------- creación ----------
def crear_conjunto(cap: int = 128) -> Dict[str, Any]:
    return {"cap": cap, "datos": [None] * cap, "n": 0}


# ---------- getters ----------
def cardinal(A: Dict[str, Any]) -> int:
    return A["n"]


def vacio(A: Dict[str, Any]) -> bool:
    return A["n"] == 0


def capacidad(A: Dict[str, Any]) -> int:
    return A["cap"]


# ---------- primitivas ----------
def contiene(A: Dict[str, Any], x: int) -> bool:
    for i in range(A["n"]):
        if A["datos"][i] == x:
            return True
    return False


def insertar(A: Dict[str, Any], x: int) -> bool:
    if contiene(A, x) or A["n"] >= A["cap"]:
        return False
    A["datos"][A["n"]] = x
    A["n"] += 1
    return True


def eliminar(A: Dict[str, Any], x: int) -> bool:
    n = A["n"]
    for i in range(n):
        if A["datos"][i] == x:
            A["datos"][i] = A["datos"][n - 1]
            A["datos"][n - 1] = None
            A["n"] -= 1
            return True
    return False


def limpiar(A: Dict[str, Any]) -> None:
    A["datos"] = [None] * A["cap"]
    A["n"] = 0


def a_vector(A: Dict[str, Any]) -> List[int]:
    return [A["datos"][i] for i in range(A["n"])]


# ---------- operaciones ----------
def union(A: Dict[str, Any], B: Iterable[int]) -> Dict[str, Any]:
    elems = list(dict.fromkeys(list(a_vector(A)) + list(B)))
    C = crear_conjunto(max(len(elems), A["cap"]))
    for v in elems:
        insertar(C, v)
    return C


def interseccion(A: Dict[str, Any], B: Iterable[int]) -> Dict[str, Any]:
    C = crear_conjunto(A["cap"])
    sB = set(B)
    for v in a_vector(A):
        if v in sB:
            insertar(C, v)
    return C


def diferencia(A: Dict[str, Any], B: Iterable[int]) -> Dict[str, Any]:
    C = crear_conjunto(A["cap"])
    sB = set(B)
    for v in a_vector(A):
        if v not in sB:
            insertar(C, v)
    return C


# ---------- CLI simple ----------
def _leer_lista_enteros(prompt: str) -> List[int]:
    linea = input(prompt).strip()
    if not linea:
        return []
    return [int(tok) for tok in linea.replace(",", " ").split()]


def _formatear(v: Iterable[int]) -> str:
    return "{" + ", ".join(map(str, sorted(set(v)))) + "}"


if __name__ == "__main__":
    print("Conjunto ESTÁTICO (sin __init__). Ingresa tus elementos.")
    a_vals = _leer_lista_enteros("A (ej: 1 2 3 4): ")
    b_vals = _leer_lista_enteros("B (ej: 3 4 5): ")

    A = crear_conjunto(cap=max(8, len(set(a_vals))))
    for x in a_vals:
        insertar(A, x)

    print(f"A = {_formatear(a_vector(A))} |A|={cardinal(A)} cap={capacidad(A)}")
    print(f"B = {_formatear(b_vals)}")

    U = union(A, b_vals)
    I = interseccion(A, b_vals)
    D = diferencia(A, b_vals)

    print("A ∪ B =", _formatear(a_vector(U)))
    print("A ∩ B =", _formatear(a_vector(I)))
    print("A \\ B =", _formatear(a_vector(D)))
