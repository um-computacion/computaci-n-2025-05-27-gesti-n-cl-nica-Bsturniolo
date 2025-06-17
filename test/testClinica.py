import unittest
from datetime import datetime
from Clinica import Clinica
from medicos import Medico
from Especialidad import Especialidad
from excepcionesClinica import (EspecialidadDuplicadaException, EspecialidadInvalidaException, MedicoNoEncontradoException)

class TestEspecialidadesClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.medico = Medico(nombre="Dr. Pérez", matricula="M123")
        self.clinica.agregar_medico(self.medico)

    def test_agregar_especialidad_nueva(self):
        esp = Especialidad(tipo="Cardiología", dias=["lunes", "miércoles"])
        self.clinica.agregar_especialidad_a_medico("M123", esp)
        especialidades = self.medico.obtener_especialidades()
        self.assertIn(esp, especialidades)
    
    def test_evitar_duplicado_especialidad(self):
        esp = Especialidad(tipo="Cardiología", dias=["lunes", "miércoles"])
        self.clinica.agregar_especialidad_a_medico("M123", esp)
        with self.assertRaises(EspecialidadDuplicadaException):
            self.clinica.agregar_especialidad_a_medico("M123", esp)

    def test_especialidad_con_dias_invalidos(self):
        esp = Especialidad(tipo="Neurología", dias=["lunes", "funday"])
        with self.assertRaises(EspecialidadInvalidaException):
            self.clinica.agregar_especialidad_a_medico("M123", esp)

    def test_agregar_especialidad_medico_no_registrado(self):
        esp = Especialidad(tipo="Pediatría", dias=["martes"])
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.agregar_especialidad_a_medico("M999", esp)

