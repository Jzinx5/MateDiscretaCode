# Importamos numpy
import numpy as np


# Clase para comparar modelos climaticos
class Comparador:

    # Constructor
    def __init__(self, Matriz1, Matriz2):

        self.Matriz1 = Matriz1
        self.Matriz2 = Matriz2

        self.Estados = [
            "Nublado",
            "P. Nublado",
            "P. Soleado",
            "Soleado"
        ]


    # Funcion principal para comparar matrices
    def CompararMatrices(self):

        # Colores
        CYAN = "\033[96m"
        GREEN = "\033[92m"
        MAGENTA = "\033[95m"
        RESET = "\033[0m"

        print(f"\n{CYAN}{'='*80}{RESET}")
        print(f"{MAGENTA}{'COMPARACION DE MATRICES CLIMATICAS':^80}{RESET}")
        print(f"{CYAN}{'='*80}{RESET}")

        # Recorremos filas y columnas
        for Fila in range(len(self.Matriz1)):

            print(f"\n{MAGENTA}Estado:{RESET} {self.Estados[Fila]}")

            for Columna in range(len(self.Matriz1[Fila])):

                Valor1 = self.Matriz1[Fila][Columna]
                Valor2 = self.Matriz2[Fila][Columna]

                Diferencia = Valor2 - Valor1

                print(
                    f"{GREEN}"
                    f"{self.Estados[Fila]:<15}"
                    f"-> "
                    f"{self.Estados[Columna]:<15}"
                    f"{RESET}"
                    f"Antes: {Valor1:.4f} | "
                    f"Despues: {Valor2:.4f} | "
                    f"Diferencia: {Diferencia:+.4f}"
                )

        print(f"\n{CYAN}{'='*80}{RESET}")


    # Funcion para mostrar cual cambio mas
    def MostrarCambioMayor(self):

        # Colores
        CYAN = "\033[96m"
        GREEN = "\033[92m"
        MAGENTA = "\033[95m"
        RESET = "\033[0m"

        CambioMayor = 0
        EstadoInicio = ""
        EstadoFinal = ""

        # Buscar mayor diferencia
        for Fila in range(len(self.Matriz1)):

            for Columna in range(len(self.Matriz1[Fila])):

                Valor1 = self.Matriz1[Fila][Columna]
                Valor2 = self.Matriz2[Fila][Columna]

                Diferencia = abs(Valor2 - Valor1)

                if Diferencia > CambioMayor:

                    CambioMayor = Diferencia

                    EstadoInicio = self.Estados[Fila]
                    EstadoFinal = self.Estados[Columna]

        print(f"\n{CYAN}{'='*80}{RESET}")
        print(f"{MAGENTA}{'CAMBIO MAS IMPORTANTE':^80}{RESET}")
        print(f"{CYAN}{'='*80}{RESET}")

        print(
            f"{GREEN}"
            f"{EstadoInicio}"
            f"{RESET} -> "
            f"{GREEN}"
            f"{EstadoFinal}"
            f"{RESET}"
            f" cambio "
            f"{MAGENTA}{CambioMayor:.4f}{RESET}"
        )

        print(f"{CYAN}{'='*80}{RESET}")