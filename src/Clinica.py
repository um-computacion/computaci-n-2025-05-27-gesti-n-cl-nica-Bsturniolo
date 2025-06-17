from datetime import datetime
from paciente import Paciente
from Historiaclinica import HistoriaClinica
from medicos import Medico
from excepcionesClinica import (MedicoNoExisteError, PacienteNoExisteError, TurnoDuplicadoError, EspecialidadNoDisponibleError)
from turnos import Turno
from receta import Receta
from excepcionesClinica import (PacienteNoEncontradoException, TurnoOcupadoException)

class Clinica:
    def __init__(self):
        self.__pacientes = {}
        self.__medicos = {}
        self.__turnos = []
        self.__historias_clinicas = {}

    # Registro y acceso
    def agregar_paciente(self, paciente: 'Paciente'):
        dni = paciente.obtener_dni()
        if dni not in self.__pacientes:
            self.__pacientes[dni] = paciente
            self.__historias_clinicas[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: 'Medico'):
        matricula = medico.obtener_matricula()
        if matricula not in self.__medicos:
            self.__medicos[matricula] = medico

    def obtener_pacientes(self) -> list['Paciente']:
        return list(self.__pacientes.values())

    def obtener_medicos(self) -> list['Medico']:
        return list(self.__medicos.values())

    def obtener_medico_por_matricula(self, matricula: str) -> 'Medico':
        if matricula not in self.__medicos:
            raise MedicoNoExisteError(f"El médico con matrícula {matricula} no existe.")
        return self.__medicos[matricula]

    # Validaciones
    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__pacientes:
            raise PacienteNoExisteError(f"El paciente con DNI {dni} no existe.")

    def validar_existencia_medico(self, matricula: str):
        if matricula not in self.__medicos:
            raise MedicoNoExisteError(f"El médico con matrícula {matricula} no existe.")

    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        for turno in self.__turnos:
            if (turno.obtener_medico().obtener_matricula() == matricula and 
                turno.obtener_fecha_hora() == fecha_hora):
                raise TurnoDuplicadoError(f"Ya existe un turno para el médico {matricula} en la fecha y hora {fecha_hora}.")

    def validar_especialidad_en_dia(self, medico: 'Medico', especialidad_solicitada: str, dia_semana: str):
        especialidad_disponible = self.obtener_especialidad_disponible(medico, dia_semana)
        if especialidad_disponible is None or especialidad_disponible.lower() != especialidad_solicitada.lower():
            raise EspecialidadNoDisponibleError(f"El médico no atiende la especialidad '{especialidad_solicitada}' el día {dia_semana}.")

    # Métodos auxiliares
    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
        return dias[fecha_hora.weekday()]

    def obtener_especialidad_disponible(self, medico: 'Medico', dia_semana: str) -> str | None:
        return medico.obtener_especialidad_para_dia(dia_semana)
    
    # Execepciones 
    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__pacientes__:
            raise PacienteNoEncontradoException(f"No existe paciente con DNI {dni}.")

    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        for turno in self.__turnos__:
            if turno.obtener_medico().obtener_matricula() == matricula and turno.obtener_fecha_hora() == fecha_hora:
                raise TurnoOcupadoException(f"El médico con matrícula {matricula} ya tiene un turno a esa hora.")
            
    # Gestión de turnos
    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        self.validar_turno_no_duplicado(matricula, fecha_hora)

        medico = self.obtener_medico_por_matricula(matricula)
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)

        paciente = self.__pacientes[dni]
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)

    def obtener_turnos(self) -> list['Turno']:
        return self.__turnos.copy()

    # Gestión de recetas
    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)

        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]

        receta = Receta(paciente, medico, medicamentos)
        self.__historias_clinicas[dni].agregar_receta(receta)

    def obtener_historia_clinica(self, dni: str) -> 'HistoriaClinica':
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas[dni]

#Al agregar paciente o médico, se guardan en diccionarios para acceso rápido.
#Antes de agendar un turno o emitir receta se validan que existan paciente y médico.
#Se valida que no haya turno duplicado para el mismo médico en fecha y hora.
#Se verifica que el médico atienda la especialidad ese día.
#Los turnos y recetas se agregan también a la historia clínica correspondiente.
#Metodos auxiliares sontareas específicas que no son directamente operaciones del negocio (como agregar pacientes o agendar turnos)