from Especialidad import Especialidad

class Medico:
    def __init__(self, nombre: str, matricula: str):
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = []

    def agregar_especialidad(self, especialidad: Especialidad):
        self.__especialidades.append(especialidad)

    def obtener_matricula(self) -> str:
        return self.__matricula

    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        for esp in self.__especialidades:
            if esp.atiende_el_dia(dia):
                return esp.nombre
        return None

    def __str__(self) -> str:
        especialidades_str = "\n  - ".join(str(e) for e in self.__especialidades)
        return f"Médico: {self.__nombre} | Matrícula: {self.__matricula}\n  - {especialidades_str}"

#Los atributos son privados
#obtener_especialidad_para_dia() devuelve el nombre de la especialidad que atiende ese día (o None)
#agregar_especialidad() carga una especialidad en el médico
#Se incluye una representación legible en __str__()