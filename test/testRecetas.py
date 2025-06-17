import unittest
from datetime import datetime
from Clinica import Clinica
from paciente import Paciente
from medicos import Medico
from excepcionesClinica import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    RecetaInvalidaException,
)

class TestRecetasClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("12345678", "Ana Gómez", "02/02/1985")
        self.medico = Medico("Dr. Ramírez", "M100")
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_emitir_receta_exitosamente(self):
        medicamentos = ["Paracetamol", "Ibuprofeno"]
        self.clinica.emitir_receta("12345678", "M100", medicamentos)
        
        historia = self.clinica.obtener_historia_clinica("12345678")
        recetas = historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertEqual(recetas[0]._Receta__medicamentos__, medicamentos)  # acceso directo al atributo privado

    def test_emitir_receta_paciente_no_existe(self):
        medicamentos = ["Paracetamol"]
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("00000000", "M100", medicamentos)

    def test_emitir_receta_medico_no_existe(self):
        medicamentos = ["Paracetamol"]
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.emitir_receta("12345678", "M999", medicamentos)

    def test_emitir_receta_sin_medicamentos(self):
        medicamentos = []
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("12345678", "M100", medicamentos)
