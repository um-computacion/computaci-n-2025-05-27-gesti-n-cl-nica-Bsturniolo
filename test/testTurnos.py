import unittest
from datetime import datetime, timedelta
from Clinica import Clinica
from paciente import Paciente
from medicos import Medico
from Especialidad import Especialidad
from excepcionesClinica import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    TurnoDuplicadoError,
    EspecialidadInvalidaException,
    MedicoNoDisponibleException,
)

class TestTurnosClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()

        # Crear paciente y médico registrados
        self.paciente = Paciente("12345678", "Juan Pérez", "01/01/1990")
        self.clinica.agregar_paciente(self.paciente)

        self.medico = Medico("Dr. López", "M001")
        self.clinica.agregar_medico(self.medico)

        # Especialidad válida para lunes y miércoles
        self.especialidad = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.clinica.agregar_especialidad_a_medico("M001", self.especialidad)

    def test_agendar_turno_exitoso(self):
        # Fecha un lunes
        fecha_turno = datetime.now() + timedelta(days=(7 - datetime.now().weekday()))  # próximo lunes
        fecha_turno = fecha_turno.replace(hour=10, minute=0, second=0, microsecond=0)

        self.clinica.agendar_turno(
            dni="12345678",
            matricula="M001",
            especialidad="Cardiología",
            fecha_hora=fecha_turno,
        )
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0].obtener_medico().obtener_matricula(), "M001")

    def test_evitar_turno_duplicado(self):
        fecha_turno = datetime.now() + timedelta(days=(7 - datetime.now().weekday()))
        fecha_turno = fecha_turno.replace(hour=10, minute=0, second=0, microsecond=0)

        self.clinica.agendar_turno("12345678", "M001", "Cardiología", fecha_turno)
        with self.assertRaises(TurnoDuplicadoError):
            self.clinica.agendar_turno("12345678", "M001", "Cardiología", fecha_turno)

    def test_paciente_no_existente(self):
        fecha_turno = datetime.now() + timedelta(days=(7 - datetime.now().weekday()))
        fecha_turno = fecha_turno.replace(hour=10, minute=0, second=0, microsecond=0)

        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("00000000", "M001", "Cardiología", fecha_turno)

    def test_medico_no_existente(self):
        fecha_turno = datetime.now() + timedelta(days=(7 - datetime.now().weekday()))
        fecha_turno = fecha_turno.replace(hour=10, minute=0, second=0, microsecond=0)

        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.agendar_turno("12345678", "M999", "Cardiología", fecha_turno)

    def test_especialidad_no_atendida_por_medico(self):
        fecha_turno = datetime.now() + timedelta(days=(7 - datetime.now().weekday()))
        fecha_turno = fecha_turno.replace(hour=10, minute=0, second=0, microsecond=0)

        with self.assertRaises(EspecialidadInvalidaException):
            self.clinica.agendar_turno("12345678", "M001", "Pediatría", fecha_turno)

    def test_medico_no_trabaja_dia(self):
        fecha_turno = datetime.now() + timedelta(days=(4 - datetime.now().weekday()) % 7)
        fecha_turno = fecha_turno.replace(hour=10, minute=0, second=0, microsecond=0)

        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "M001", "Cardiología", fecha_turno)
