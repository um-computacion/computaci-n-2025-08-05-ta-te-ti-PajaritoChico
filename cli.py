from tateti import Tateti
from jugador import Jugador

def leer_posicion():
    """Lee fila y columna en formato 1–3 y devuelve índices 0–2."""
    while True:
        try:
            fil = int(input("Fila (1-3): "))
            col = int(input("Columna (1-3): "))
            if fil not in (1, 2, 3) or col not in (1, 2, 3):
                print(" Deben ser números entre 1 y 3. Probá de nuevo.")
                continue
            return fil - 1, col - 1
        except ValueError:
            print(" Ingresá números válidos (1, 2 o 3).")

def main():
    print("Bienvenidos al Tatetí")

    nombre_x = input("Nombre del jugador X (enter para 'Jugador X'): ").strip() or "Jugador X"
    nombre_o = input("Nombre del jugador O (enter para 'Jugador O'): ").strip() or "Jugador O"
    jx = Jugador(nombre_x, "X")
    jo = Jugador(nombre_o, "O")
    jugadores = {"X": jx, "O": jo}

    juego = Tateti()

    while not juego.termino():
        print(juego.tablero) 
        jugador_actual = jugadores[juego.turno]
        print(f"Turno de: {jugador_actual.obtener_nombre()} ({jugador_actual.obtener_ficha()})")

        fil, col = leer_posicion()
        try:
            juego.ocupar_una_de_las_casillas(fil, col)
        except Exception as e:
            print(f" {e}")

    print(juego.tablero)
    if juego.estado.startswith("ganó "):
        ficha_ganadora = juego.estado.split()[-1]
        ganador = jugadores[ficha_ganadora]
        print(f" Ganó {ganador.obtener_nombre()} ({ganador.obtener_ficha()})")
    else:
        print(" Empate")

if __name__ == '__main__':
    main()