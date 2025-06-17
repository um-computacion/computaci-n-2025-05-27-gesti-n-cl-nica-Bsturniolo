from datetime import datetime

class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        self.__nombre = nombre
        self.__dni = dni
        try:
            datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        except ValueError:
            raise ValueError("La fecha de nacimiento debe tener el formato dd/mm/aaaa")
        self.__fecha_nacimiento = fecha_nacimiento

    def obtener_dni(self) -> str:
        return self.__dni

    def __str__(self) -> str:
        return f"Paciente: {self.__nombre} | DNI: {self.__dni} | Nacido el: {self.__fecha_nacimiento}"

#Los atributos son privados (__nombre, __dni, __fecha_nacimiento)
#Se valido que la fecha esté en formato dd/mm/aaaa usando datetime.strptime
#Se implemento obtener_dni() y __str__()