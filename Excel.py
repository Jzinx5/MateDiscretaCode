# Importamos pandas
import pandas as pd
import os

# Clase para exportar informacion a Excel
class Excel:

    # Constructor
    def __init__(self, Datos, Matriz=None):

        self.Datos = Datos
        self.Matriz = Matriz


    # Exportar datos climaticos
    def ExportarDatosExcel(self):

        Tabla = pd.DataFrame({
            "Dia": range(1, len(self.Datos) + 1),
            "Estado": self.Datos
        })
        RutaActual = os.path.dirname(os.path.abspath(__file__))
        RutaArchivo = os.path.join(RutaActual, "DatosClimaticos.xlsx")

        Tabla.to_excel(RutaArchivo, index=False)

        print("Datos exportados correctamente")


    # Exportar matriz
    def ExportarMatrizExcel(self):

        if self.Matriz is None:
            print("Primero debes calcular la matriz")
            return

        Tabla = pd.DataFrame(self.Matriz)

        RutaActual = os.path.dirname(os.path.abspath(__file__))
        RutaArchivo = os.path.join(RutaActual, "MatrizMarkov.xlsx")

        Tabla.to_excel(RutaArchivo, index=False)

        print("Matriz exportada correctamente")