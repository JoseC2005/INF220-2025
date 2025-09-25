"""
ADT Conjunto (DINÁMICO) — lista enlazada con clase (usa __init__).
"""

from typing import Iterable, List


class ConjuntoDinamico:
    class _Node:
        __slots__ = ("val", "nxt")

        def __init__(self, val: int, nxt: "ConjuntoDinamico._Node" | None = None):
            self.val = val
            self.nxt = nxt

    def __init__(self) -> None:
        self._head: ConjuntoDinamico._Node | None = None
        self._n: int = 0

    # getters
    def cardinal(self) -> int:
        return self._n

    def vacio(self) -> bool:
        return self._n == 0

    # primitivas
    def contiene(self, x: int) -> bool:
        p = self._head
        while p:
            if p.val == x:
                return True
            p = p.nxt
        return False

    def insertar(self, x: int) -> bool:
        if self.contiene(x):
            return False
        self._head = self._Node(x, self._head)
        self._n += 1
        return True

    def eliminar(self, x: int) -> bool:
        pp: ConjuntoDinamico._Node | None = None
        p = self._head
        while p:
            if p.val == x:
                if pp:
                    pp.nxt = p.nxt
                else:
                    self._head = p.nxt
                self._n -= 1
                return True
            pp, p = p, p.nxt
        return False

    def limpiar(self) -> None:
        self._head = None
        self._n = 0

    def a_vector(self) -> List[int]:
        v: List[int] = []
        p = self._head
        while p:
            v.append(p.val)
            p = p.nxt
        return v

    # operaciones
    def union(self, B: Iterable[int] | "ConjuntoDinamico") -> "ConjuntoDinamico":
        C = ConjuntoDinamico()
        for v in self.a_vector():
            C.insertar(v)
        vals = B.a_vector() if isinstance(B, ConjuntoDinamico) else list(B)
        for v in vals:
            C.insertar(v)
        return C

    def interseccion(self, B: Iterable[int] | "ConjuntoDinamico") -> "ConjuntoDinamico":
        C = ConjuntoDinamico()
        sB = set(B.a_vector() if isinstance(B, ConjuntoDinamico) else list(B))
        for v in self.a_vector():
            if v in sB:
                C.insertar(v)
        return C

    def diferencia(self, B: Iterable[int] | "ConjuntoDinamico") -> "ConjuntoDinamico":
        C = ConjuntoDinamico()
        sB = set(B.a_vector() if isinstance(B, ConjuntoDinamico) else list(B))
        for v in self.a_vector():
            if v not in sB:
                C.insertar(v)
        return C


# ---------- CLI simple ----------
def _leer_lista_enteros(prompt: str) -> list[int]:
    linea = input(prompt).strip()
    if not linea:
        return []
    return [int(tok) for tok in linea.replace(",", " ").split()]


def _formatear(v: Iterable[int]) -> str:
    return "{" + ", ".join(map(str, sorted(set(v)))) + "}"


if __name__ == "__main__":
    print("Conjunto DINÁMICO. Ingresa tus elementos.")
    a_vals = _leer_lista_enteros("A (ej: 1 2 3 4): ")
    b_vals = _leer_lista_enteros("B (ej: 3 4 5): ")

    A = ConjuntoDinamico()
    for x in a_vals:
        A.insertar(x)

    print(f"A = {_formatear(A.a_vector())} |A|={A.cardinal()}")
    print(f"B = {_formatear(b_vals)}")

    U = A.union(b_vals)
    I = A.interseccion(b_vals)
    D = A.diferencia(b_vals)

    print("A ∪ B =", _formatear(U.a_vector()))
    print("A ∩ B =", _formatear(I.a_vector()))
    print("A \\ B =", _formatear(D.a_vector()))
