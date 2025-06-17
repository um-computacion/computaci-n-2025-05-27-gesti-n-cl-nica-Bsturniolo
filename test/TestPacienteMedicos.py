import unittest
from Clinica import Clinica
from paciente import Paciente
from medicos import Medico
from excepcionesClinica import (PacienteDuplicadoException, MedicoDuplicadoException)

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()

    def test_agregar_paciente_exitoso(self):
        p = Paciente("12345678", "Juan Perez", "01/01/1980")
        self.clinica.agregar_paciente(p)
        self.assertIn("12345678", self.clinica.obtener_pacientes_dnis())

    def test_agregar_paciente_duplicado(self):
        p = Paciente("12345678", "Juan Perez", "01/01/1980")
        self.clinica.agregar_paciente(p)
        with self.assertRaises(PacienteDuplicadoException):
            self.clinica.agregar_paciente(p)

    def test_agregar_medico_exitoso(self):
        m = Medico("Dr. Ana", "MAT123")
        self.clinica.agregar_medico(m)
        self.assertIn("MAT123", self.clinica.obtener_medicos_matriculas())

    def test_agregar_medico_duplicado(self):
        m = Medico("Dr. Ana", "MAT123")
        self.clinica.agregar_medico(m)
        with self.assertRaises(MedicoDuplicadoException):
            self.clinica.agregar_medico(m)

