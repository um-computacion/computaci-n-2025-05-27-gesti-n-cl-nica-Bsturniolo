from Clinica import Clinica
from CLI import CLI

def main():
    clinica = Clinica()
    interfaz = CLI(clinica)
    interfaz.mostrar_menu()

if __name__ == "__main__":
    main()
