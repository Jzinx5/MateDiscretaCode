# Importamos numpy para trabajar con matrices
import numpy as np


# Clase principal del modelo de Markov
class ModeloMarkov:

    # Constructor
    def __init__(self, DatosClimaticos):

        # Guardamos datos
        self.Datos = DatosClimaticos

        # Nombres de estados
        self.Estados = [
            "Nublado",
            "P. Nublado",
            "P. Soleado",
            "Soleado"
        ]

        # Cantidad de estados
        self.TotalEstados = len(self.Estados)

        # Matriz vacia inicialmente
        self.Matriz = None


    # Funcion para calcular matriz
    def CalcularMatriz(self):

        # Creamos matriz llena de ceros
        Conteo = np.zeros((self.TotalEstados, self.TotalEstados))

        # Recorremos los datos
        for i in range(len(self.Datos) - 1):

            EstadoActual = self.Datos[i]
            EstadoSiguiente = self.Datos[i + 1]

            Conteo[EstadoActual][EstadoSiguiente] += 1

        # Convertimos conteos en probabilidades
        SumaFilas = Conteo.sum(axis=1, keepdims=True)
        SumaFilas[SumaFilas == 0] = 1
        self.Matriz = Conteo / SumaFilas

        return self.Matriz


    # Mostrar matriz bonita
    def MostrarMatriz(self):

        # Validamos existencia
        if self.Matriz is None:
            print("Primero debes calcular la matriz")
            return

        # Colores
        CYAN = "\033[96m"
        GREEN = "\033[92m"
        MAGENTA = "\033[95m"
        RESET = "\033[0m"

        print(f"\n{CYAN}{'='*75}{RESET}")
        print(f"{MAGENTA}{'MATRIZ DE TRANSICION CLIMATICA':^75}{RESET}")
        print(f"{CYAN}{'='*75}{RESET}")

        Encabezado = " " * 18

        for Estado in self.Estados:
            Encabezado += f"{Estado:^14}"

        print(f"{MAGENTA}{Encabezado}{RESET}")

        for i, Fila in enumerate(self.Matriz):

            Valores = ""

            for Probabilidad in Fila:
                Valores += f"{Probabilidad:^14.4f}"

            print(f"{GREEN}{self.Estados[i]:<18}{RESET}{Valores}")

        print(f"{CYAN}{'='*75}{RESET}")


    # Prediccion futura
    def PredecirFuturo(self, CantidadDias):

        # Validamos matriz
        if self.Matriz is None:
            print("Primero debes calcular la matriz")
            return

        # Colores
        CYAN = "\033[96m"
        GREEN = "\033[92m"
        MAGENTA = "\033[95m"
        RESET = "\033[0m"

        # Ultimo estado registrado
        UltimoEstado = self.Datos[-1]

        # Vector inicial
        VectorActual = np.zeros(self.TotalEstados)
        VectorActual[UltimoEstado] = 1

        print(f"\n{CYAN}{'='*75}{RESET}")
        print(f"{MAGENTA}{'PREDICCION CLIMATICA':^75}{RESET}")
        print(f"{CYAN}{'='*75}{RESET}")

        print(f"{MAGENTA}Estado actual:{RESET} {self.Estados[UltimoEstado]}")

        for Dia in range(1, CantidadDias + 1):

            MatrizElevada = np.linalg.matrix_power(self.Matriz, Dia)

            Resultado = np.dot(VectorActual, MatrizElevada)

            EstadoMasProbable = np.argmax(Resultado)

            Probabilidad = Resultado[EstadoMasProbable] * 100

            print(
                f"{GREEN}Dia {Dia:<3}{RESET}"
                f"-> {self.Estados[EstadoMasProbable]:<20}"
                f"{Probabilidad:>6.2f}%"
            )