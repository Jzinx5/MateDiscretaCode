CYAN = "\033[96m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RESET = "\033[0m"



# Mostrar linea decorativa
def MostrarLinea():

    print(f"{CYAN}{'='*75}{RESET}")


# Mostrar titulo centrado
def MostrarTitulo(Texto):

    MostrarLinea()

    print(f"{MAGENTA}{Texto:^75}{RESET}")

    MostrarLinea()


# Mensaje correcto
def MostrarCorrecto(Texto):

    print(f"{GREEN}{Texto}{RESET}")


# Mensaje error
def MostrarError(Texto):

    print(f"{MAGENTA}{Texto}{RESET}")