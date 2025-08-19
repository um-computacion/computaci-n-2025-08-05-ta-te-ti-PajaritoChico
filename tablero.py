class PosOcupadaException(Exception):
    ...


class PosFueraDeRangoException(Exception):
    ...


class Tablero:
    def __init__(self):

        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def en_rango(self, fil, col) -> bool:
        return 0 <= fil < 3 and 0 <= col < 3

    def celda_vacia(self, fil, col) -> bool:
        return self.contenedor[fil][col] == ""

    def poner_la_ficha(self, fil, col, ficha):
    
        if not self.en_rango(fil, col):
            raise PosFueraDeRangoException("fuera de rango (use 0, 1 o 2)")
        if not self.celda_vacia(fil, col):
            raise PosOcupadaException("pos ocupada!")
    
        self.contenedor[fil][col] = ficha

    def hay_linea(self, ficha) -> bool:
        c = self.contenedor
    
        for f in range(3):
            if c[f][0] == c[f][1] == c[f][2] == ficha:
                return True
    
        for col in range(3):
            if c[0][col] == c[1][col] == c[2][col] == ficha:
                return True
    
        if c[0][0] == c[1][1] == c[2][2] == ficha:
            return True
        if c[0][2] == c[1][1] == c[2][0] == ficha:
            return True
        return False

    def lleno(self) -> bool:
    
        return all(self.contenedor[f][c] != "" for f in range(3) for c in range(3))

    def __str__(self) -> str:
    
        def show(x): return x if x != "" else " "
        filas = [' {} | {} | {} '.format(*(show(v) for v in self.contenedor[r])) for r in range(3)]
        return f"\n{filas[0]}\n---+---+---\n{filas[1]}\n---+---+---\n{filas[2]}\n"