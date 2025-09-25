"""
ADT Polinomio (DINÁMICO) — lista enlazada ordenada por exponente descendente.
No se guardan términos con coeficiente 0.
"""

from typing import List, Tuple


class Polinomio:
    class _Node:
        __slots__ = ("c", "e", "nxt")

        def __init__(self, c: float, e: int, nxt: "Polinomio._Node" | None = None):
            self.c = c
            self.e = e
            self.nxt = nxt

    def __init__(self) -> None:
        self._head: Polinomio._Node | None = None

    # getters
    def grado(self) -> int:
        return self._head.e if self._head else -1

    # acceso
    def get_coef(self, e: int) -> float:
        p = self._head
        while p and p.e >= e:
            if p.e == e:
                return p.c
            p = p.nxt
        return 0.0

    def set_coef(self, e: int, c: float) -> None:
        if c == 0:
            self._del_exp(e)
            return
        pp: Polinomio._Node | None = None
        p = self._head
        while p and p.e > e:
            pp, p = p, p.nxt
        if p and p.e == e:
            p.c = c
        else:
            node = self._Node(c, e, p)
            if pp:
                pp.nxt = node
            else:
                self._head = node

    def _del_exp(self, e: int) -> bool:
        pp: Polinomio._Node | None = None
        p = self._head
        while p:
            if p.e == e:
                if pp:
                    pp.nxt = p.nxt
                else:
                    self._head = p.nxt
                return True
            pp, p = p, p.nxt
        return False

    # utilidades
    def evaluar(self, x: float) -> float:
        res = 0.0
        g = self.grado()
        p = self._head
        exp = g
        while exp >= 0:
            res *= x
            if p and p.e == exp:
                res += p.c
                p = p.nxt
            exp -= 1
        return res

    def a_lista(self) -> List[Tuple[float, int]]:
        out: List[Tuple[float, int]] = []
        p = self._head
        while p:
            out.append((p.c, p.e))
            p = p.nxt
        return out

    # operaciones
    def copiar(self) -> "Polinomio":
        q = Polinomio()
        for c, e in self.a_lista()[::-1]:
            q.set_coef(e, c)
        return q

    def sumar(self, b: "Polinomio" | List[Tuple[float, int]]) -> "Polinomio":
        if not isinstance(b, Polinomio):
            tmp = Polinomio()
            for c, e in b:
                tmp.set_coef(e, c)
            b = tmp
        c = Polinomio()
        p, q = self._head, b._head
        while p or q:
            if q is None or (p and p.e > q.e):
                c.set_coef(p.e, p.c)
                p = p.nxt
            elif p is None or (q and q.e > p.e):
                c.set_coef(q.e, q.c)
                q = q.nxt
            else:
                s = p.c + q.c
                if s != 0:
                    c.set_coef(p.e, s)
                p, q = p.nxt, q.nxt
        return c

    def restar(self, b: "Polinomio" | List[Tuple[float, int]]) -> "Polinomio":
        if not isinstance(b, Polinomio):
            tmp = Polinomio()
            for c, e in b:
                tmp.set_coef(e, c)
            b = tmp
        nb = Polinomio()
        for ccoef, eexp in b.a_lista():
            nb.set_coef(eexp, -ccoef)
        return self.sumar(nb)

    def multiplicar(self, b: "Polinomio" | List[Tuple[float, int]]) -> "Polinomio":
        if not isinstance(b, Polinomio):
            tmp = Polinomio()
            for c, e in b:
                tmp.set_coef(e, c)
            b = tmp
        c = Polinomio()
        p = self._head
        while p:
            q = b._head
            while q:
                e_sum = p.e + q.e
                c.set_coef(e_sum, c.get_coef(e_sum) + p.c * q.c)
                q = q.nxt
            p = p.nxt
        return c


# ---------- CLI simple ----------
def _leer_pares(prompt: str) -> list[tuple[float, int]]:
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
    pares: list[tuple[float, int]] = []
    for i in range(0, len(piezas), 2):
        c = float(piezas[i])
        e = int(piezas[i + 1])
        pares.append((c, e))
    return pares


def _formatear(pares: list[tuple[float, int]]) -> str:
    if not pares:
        return "0"
    partes: list[str] = []
    for c, e in sorted(pares, key=lambda t: t[1], reverse=True):
        if e == 0:
            partes.append(f"{c:g}")
        elif e == 1:
            partes.append(f"{c:g}x")
        else:
            partes.append(f"{c:g}x^{e}")
    return " + ".join(partes).replace("+ -", "- ")


if __name__ == "__main__":
    print("Polinomio DINÁMICO. Ingresa tus términos.")
    a_pares = _leer_pares("A como 'coef exp' (ej: 3 0, 2 2): ")
    b_pares = _leer_pares("B como 'coef exp' (ej: 1 1, -2 2): ")

    A = Polinomio()
    B = Polinomio()
    for c, e in a_pares:
        A.set_coef(e, A.get_coef(e) + c)
    for c, e in b_pares:
        B.set_coef(e, B.get_coef(e) + c)

    S = A.sumar(B)
    R = A.restar(B)
    M = A.multiplicar(B)

    print("A(x) =", _formatear(A.a_lista()))
    print("B(x) =", _formatear(B.a_lista()))
    print("A+B  =", _formatear(S.a_lista()))
    print("A-B  =", _formatear(R.a_lista()))
    print("A*B  =", _formatear(M.a_lista()))
    x_val = float(input("Evalúa en x = ") or "0")
    print("A(x) =", A.evaluar(x_val))
