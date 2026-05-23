# Importamos numpy para generar datos aleatorios
import numpy as np


# Funcion para generar datos climaticos
def GenerarDatosClimaticos(CantidadDias=60):

    # Validamos el rango permitido
    if not (60 <= CantidadDias <= 90):
        print("Cantidad invalida. Debe estar entre 60 y 90 dias")
        return None

    

    # Estados climaticos
    # 0 = Nublado
    # 1 = Parcialmente Nublado
    # 2 = Parcialmente Soleado
    # 3 = Soleado

    Datos = np.random.choice([0, 1, 2, 3], size=CantidadDias)

    return Datos


# Funcion para agregar mas dias
def GenerarMasDatos(DatosActuales, DiasExtra):

    # Validamos dias extra
    if DiasExtra <= 0:
        print("Los dias extra deben ser mayores a 0")
        return DatosActuales

    # Generamos nuevos datos
    NuevosDatos = np.random.choice([0, 1, 2, 3], size=DiasExtra)

    # Unimos datos antiguos con nuevos
    DatosFinales = np.concatenate((DatosActuales, NuevosDatos))

    return DatosFinales


# Pruebas internas
if __name__ == "__main__":

    DatosPrueba = GenerarDatosClimaticos(60)

    print("Datos generados:")
    print(DatosPrueba)