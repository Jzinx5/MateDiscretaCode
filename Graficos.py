# Importamos matplotlib para crear graficas
import matplotlib.pyplot as plt

# Importamos Counter para contar estados climaticos
from collections import Counter


# Clase para manejar las graficas
class Graficas:

    # Constructor
    def __init__(self, Datos, Matriz=None):

        self.Datos = Datos
        self.Matriz = Matriz

        # Nombres de estados climaticos
        self.Estados = [
            "Nublado",
            "P. Nublado",
            "P. Soleado",
            "Soleado"
        ]


    # Grafica de frecuencia de climas
    def GraficarFrecuencias(self):

        # Contamos ocurrencias
        Conteo = Counter(self.Datos)

        # Valores
        Valores = [
            Conteo.get(0, 0),
            Conteo.get(1, 0),
            Conteo.get(2, 0),
            Conteo.get(3, 0)
        ]

        # Creamos grafica
        plt.figure(figsize=(8, 5))

        plt.bar(self.Estados, Valores)

        plt.title("Frecuencia de Estados Climaticos")

        plt.xlabel("Estados")

        plt.ylabel("Cantidad de Dias")

        plt.grid(axis="y")

        plt.show()
        plt.close()


    # Grafica de evolucion climatica
    def GraficarEvolucion(self):

        # Dias
        Dias = list(range(1, len(self.Datos) + 1))

        # Creamos grafica
        plt.figure(figsize=(10, 5))

        plt.plot(Dias, self.Datos, marker="o")

        plt.title("Evolucion Climatico por Dias")

        plt.xlabel("Dias")

        plt.ylabel("Estado Climatico")

        # Etiquetas de estados
        plt.yticks(
            [0, 1, 2, 3],
            [
                "Nublado",
                "P. Nublado",
                "P. Soleado",
                "Soleado"
            ]
        )

        plt.grid()

        plt.show()
        plt.close()


    # Grafica de probabilidades promedio
    def GraficarProbabilidades(self):

        # Validamos matriz
        if self.Matriz is None:

            print("Primero debes calcular la matriz")

            return

        # Calculamos promedio de probabilidades
        Promedios = self.Matriz.mean(axis=0)

        # Creamos grafica
        plt.figure(figsize=(8, 5))

        plt.bar(self.Estados, Promedios)

        plt.title("Probabilidades Promedio")

        plt.xlabel("Estados")

        plt.ylabel("Probabilidad")

        plt.grid(axis="y")

        plt.show()
        plt.close()