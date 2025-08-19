from tablero import Tablero

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()
        self.estado = "en_curso" 

    def ocupar_una_de_las_casillas(self, fil, col):
        
        ficha_actual = self.turno
        self.tablero.poner_la_ficha(fil, col, ficha_actual)

        if self.tablero.hay_linea(ficha_actual):
            self.estado = f"ganó {ficha_actual}"
            return

        if self.tablero.lleno():
            self.estado = "empate"
            return

        if self.turno == "X":
            self.turno = "O"   
        else:
            self.turno = "X"

    def termino(self) -> bool:
        return self.estado != "en_curso"