from paciente import Paciente
from turnos import Turno
from receta import Receta

class HistoriaClinica:
    def __init__(self, paciente: 'Paciente'):
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []

    def agregar_turno(self, turno: 'Turno'):
        self.__turnos.append(turno)

    def agregar_receta(self, receta: 'Receta'):
        self.__recetas.append(receta)

    def obtener_turnos(self) -> list['Turno']:
        return self.__turnos.copy()

    def obtener_recetas(self) -> list['Receta']:
        return self.__recetas.copy()

    def __str__(self) -> str:
        turnos_str = "\n".join(str(turno) for turno in self.__turnos) or "No hay turnos registrados."
        recetas_str = "\n".join(str(receta) for receta in self.__recetas) or "No hay recetas registradas."
        return (f"Historia Clínica del paciente: {self.__paciente}\n"
                f"Turnos:\n{turnos_str}\n\n"
                f"Recetas:\n{recetas_str}")

#__turnos y __recetas son listas privadas.
#obtener_turnos() y obtener_recetas() devuelven copias para evitar manipulación directa.
#El método __str__ incluye la información de turnos y recetas, o indica si no hay datos