class Jugador:
    def __init__(self, nombre: str, ficha: str):
        ficha = ficha.upper()
        if ficha not in ("X", "O"):
            raise ValueError("La ficha debe ser 'X' u 'O'")
        self.nombre = nombre
        self.ficha = ficha

    def obtener_nombre(self) -> str:
        return self.nombre

    def obtener_ficha(self) -> str:
        return self.ficha

    def __repr__(self) -> str:
        return f"Jugador({self.nombre!r}, {self.ficha!r})"