# Importamos funciones y clases
from DatosClimaticos.GenerarDatosClimaticos import GenerarDatosClimaticos
from DatosClimaticos.GenerarDatosClimaticos import GenerarMasDatos
from Logica.Comparador import Comparador
from Visualizacion.Graficos import Graficas
from Exportacion.Excel import Excel
from Visualizacion.Mermaid import Mermaid
from Logica.ModeloMarkov import ModeloMarkov


# Funcion principal del menu
def IniciarMenu():

    # Variables principales
    Datos = None
    Modelo = None

    # Colores
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"

    # Bucle infinito del menu
    while True:

        print(f"\n{CYAN}{'='*75}{RESET}")
        print(f"{MAGENTA}{'PROYECTO PREDICCION CLIMATICA MARKOV':^75}{RESET}")
        print(f"{CYAN}{'='*75}{RESET}")

        print(f"{GREEN}[1]{RESET} Generar Datos Climaticos")
        print(f"{GREEN}[2]{RESET} Generar Mas Datos")
        print(f"{GREEN}[3]{RESET} Calcular Matriz")
        print(f"{GREEN}[4]{RESET} Mostrar Matriz")
        print(f"{GREEN}[5]{RESET} Predecir Futuro")
        print(f"{GREEN}[6]{RESET} Comparar Modelos")
        print(f"{GREEN}[7]{RESET} Graficar Frecuencias")
        print(f"{GREEN}[8]{RESET} Graficar Evolucion")
        print(f"{GREEN}[9]{RESET} Graficar Probabilidades")
        print(f"{GREEN}[10]{RESET} Mostrar Estadisticas")
        print(f"{GREEN}[11]{RESET} Exportar Excel")
        print(f"{GREEN}[12]{RESET} Generar Mermaid")
        print(f"{GREEN}[0]{RESET} Salir")

        Opcion = input("\nSeleccione una opcion: ")


        # OPCION 1
        if Opcion == "1":

            CantidadDias = int(input("Ingrese cantidad de dias (60 a 90): "))

            Datos = GenerarDatosClimaticos(CantidadDias)

            if Datos is not None:

                Modelo = ModeloMarkov(Datos)

                print(f"{GREEN}Datos generados correctamente{RESET}")


        # OPCION 2
        elif Opcion == "2":

            if Datos is None:
                print("Primero debes generar datos")
                continue

            DiasExtra = int(input("Cuantos dias extra desea agregar: "))

            Datos = GenerarMasDatos(Datos, DiasExtra)

            Modelo = ModeloMarkov(Datos)

            print(f"{GREEN}Datos agregados correctamente{RESET}")
            print(f"Total actual de dias: {len(Datos)}")


        # OPCION 3
        elif Opcion == "3":

            if Modelo is None:
                print("Primero debes generar datos")
                continue

            Modelo.CalcularMatriz()

            print(f"{GREEN}Matriz calculada correctamente{RESET}")


        # OPCION 4
        elif Opcion == "4":

            if Modelo is None:
                print("Primero debes generar datos")
                continue

            Modelo.MostrarMatriz()


        # OPCION 5
        elif Opcion == "5":

            if Modelo is None:
                print("Primero debes generar datos")
                continue

            CantidadDias = int(input("Cuantos dias desea predecir: "))

            Modelo.PredecirFuturo(CantidadDias)

        # OPCION 6
        elif Opcion == "6":
            print(f"\nPrimer modelo")

            Dias1 = int(input("Ingrese cantidad de dias: "))

            Datos1 = GenerarDatosClimaticos(Dias1)

            Modelo1 = ModeloMarkov(Datos1)

            Modelo1.CalcularMatriz()
            print(f"\nSegundo modelo")

            Dias2 = int(input("Ingrese cantidad de dias: "))

            Datos2 = GenerarDatosClimaticos(Dias2)

            Modelo2 = ModeloMarkov(Datos2)

            Modelo2.CalcularMatriz()


            # Creamos comparador
            Comparacion = Comparador(
            Modelo1.Matriz,
            Modelo2.Matriz
            )

            # Mostramos comparaciones
            Comparacion.CompararMatrices()

            Comparacion.MostrarCambioMayor()

        # OPCION 7
        elif Opcion == "7":

            if Datos is None:
                print("Primero debes generar datos")
                continue
            Grafica= Graficas(Datos)
            Grafica.GraficarFrecuencias()

        # OPCION 8
        elif Opcion == "8":

            if Datos is None:
                print("Primero debes generar datos")
                continue
            Grafica = Graficas(Datos)
            Grafica.GraficarEvolucion()
        
        # OPCION 9
        elif Opcion == "9":

            if Modelo is None or Modelo.Matriz is None:
                print("Primero debes calcular la matriz")
                continue

            Grafica = Graficas(Datos, Modelo.Matriz)
            Grafica.GraficarProbabilidades()
        # OPCION 10 (Asegúrate de tener esta lógica o cámbiala por una función de resumen)
        elif Opcion == "10":
            if Datos is None:
                print("Primero debes generar datos")
                continue
            # Si no tienes una clase de estadísticas aún, puedes usar un Counter simple aquí
            from collections import Counter
            conteo = Counter(map(int, Datos))
            print(f"ESTADISTICAS CLIMATICAS")
            Estados = {0: "Nublado", 1: "P. Nublado", 2: "P. Soleado", 3: "Soleado"}
            for estado, cantidad in conteo.items():
                print(f"{Estados[estado]}: {cantidad}")

        # OPCION 11 - IMPORTANTE: Añadir 'elif'
        elif Opcion == "11":
            if Datos is None:
                print("Primero debes generar datos")
                continue
            ArchivoExcel = Excel(Datos, Modelo.Matriz if Modelo else None)
            ArchivoExcel.ExportarDatosExcel()
            if Modelo and Modelo.Matriz is not None:
                ArchivoExcel.ExportarMatrizExcel()


        # OPCION 12
        elif Opcion =="12": 
            if Modelo is None or Modelo.Matriz is None:
                print("Primero debes calcular la matriz")
                continue
            Diagrama = Mermaid(Modelo.Matriz)
            Diagrama.GenerarMermaid()
        # OPCION 0
        elif Opcion == "0":

            print(f"{MAGENTA}Saliendo del sistema...{RESET}")
            break


        # Opcion invalida
        else:
            print("Opcion invalida")