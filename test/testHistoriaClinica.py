import unittest
from datetime import datetime
from Clinica import Clinica
from paciente import Paciente
from medicos import Medico
from Especialidad import Especialidad
from turnos import Turno
from receta import Receta

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("12345678", "Carlos Pérez", "15/03/1990")
        self.medico = Medico("Dra. Martínez", "M200")
        self.especialidad = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(self.especialidad)
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_agregar_turno_a_historia_clinica(self):
        fecha_hora = datetime(2025, 6, 20, 10, 30)
        turno = Turno(self.paciente, self.medico, fecha_hora, self.especialidad.obtener_especialidad())
        self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), self.especialidad.obtener_especialidad(), fecha_hora)

        historia = self.clinica.obtener_historia_clinica(self.paciente.obtener_dni())
        turnos = historia.obtener_turnos()

        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0].obtener_medico().obtener_matricula(), self.medico.obtener_matricula())
        self.assertEqual(turnos[0].obtener_fecha_hora(), fecha_hora)

    def test_agregar_receta_a_historia_clinica(self):
        medicamentos = ["Aspirina", "Atorvastatina"]
        self.clinica.emitir_receta(self.paciente.obtener_dni(), self.medico.obtener_matricula(), medicamentos)

        historia = self.clinica.obtener_historia_clinica(self.paciente.obtener_dni())
        recetas = historia.obtener_recetas()

        self.assertEqual(len(recetas), 1)
        self.assertEqual(recetas[0]._Receta__medicamentos__, medicamentos)
