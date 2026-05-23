import os


# Clase para generar diagramas Mermaid
class Mermaid:

    # Constructor
    def __init__(self, Matriz):

        self.Matriz = Matriz

        self.Estados = [
            "Nublado",
            "P_Nublado",
            "P_Soleado",
            "Soleado"
        ]


    # Funcion para generar archivo Mermaid
    def GenerarMermaid(self):

        Texto = "graph TD\n\n"

        # Recorremos matriz
        for Fila in range(len(self.Matriz)):

            for Columna in range(len(self.Matriz[Fila])):

                Probabilidad = self.Matriz[Fila][Columna]

                # Solo mostrar probabilidades mayores a 0.25
                if Probabilidad > 0.25:

                    Texto += (
                        f"    {self.Estados[Fila]} "
                        f"-->|{Probabilidad:.2f}| "
                        f"{self.Estados[Columna]}\n"
                    )

        # Ruta de la carpeta actual
        RutaActual = os.path.dirname(os.path.abspath(__file__))

        # Nombre del archivo .mermaid
        RutaArchivo = os.path.join(
            RutaActual,
            "DiagramaClimatico.mermaid"
        )

        # Crear archivo
        with open(RutaArchivo, "w", encoding="utf-8") as Archivo:

            Archivo.write(Texto)

        print("Archivo Mermaid generado correctamente")

        