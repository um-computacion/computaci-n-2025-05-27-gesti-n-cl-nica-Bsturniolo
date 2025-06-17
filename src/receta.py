from datetime import datetime
from paciente import Paciente
from medicos import Medico

class Receta:
    def __init__(self, paciente: 'Paciente', medico: 'Medico', medicamentos: list[str]):
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self) -> str:
        medicamentos_str = ", ".join(self.__medicamentos)
        return (f"Receta médica:\n"
                f"  Paciente: {self.__paciente}\n"
                f"  Médico: {self.__medico}\n"
                f"  Medicamentos: {medicamentos_str}\n"
                f"  Fecha de emisión: {self.__fecha.strftime('%d/%m/%Y %H:%M')}")

#medicamentos es una lista de strings con los nombres de los medicamentos
#La fecha se asigna automáticamente en la creación de la receta con la fecha y hora actuales
#El método __str__ imprime la receta