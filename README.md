
DIAZ JUAN JESUS

# 🎮 Tatetí (Tres en Línea)
---

## 📌 Descripción
El programa permite jugar una partida de Tatetí en consola entre dos jugadores humanos.  
Cada jugador elige un nombre y se le asigna una ficha (**X** u **O**).  
El juego alterna turnos, valida jugadas y determina automáticamente si hubo un **ganador** o un **empate**.

---

## 📂 Estructura del proyecto
- **`jugador.py`** → Clase `Jugador`. Representa a un jugador con su nombre y ficha.  
- **`tablero.py`** → Clase `Tablero`. Maneja la grilla 3x3, valida posiciones y detecta ganadores o empate.  
- **`tateti.py`** → Clase `Tateti`. Coordina los turnos, controla el estado de la partida y usa al `Tablero`.  
- **`cli.py`** → Interfaz por consola. Pide nombres, recibe jugadas y muestra el tablero y resultados.

---

## ▶️ Ejecución del juego
1. Clonar este repositorio:
   ```bash
   git clone <URL-del-repo>
   cd <nombre-del-repo>
````

2. Ejecutar el juego desde la consola:

   ```bash
   python cli.py
   ```

3. Seguir las instrucciones:

   * Ingresar los nombres de los jugadores.
   * Indicar la posición con **fila y columna del 1 al 3**.
   * El tablero se actualiza en pantalla después de cada jugada.
   * El programa finaliza cuando hay un **ganador** o se declara **empate**.


---

## ✨ Ejemplo de tablero en juego

```
 X | O |  
---+---+---
   | X |  
---+---+---
 O |   | X
```

---

