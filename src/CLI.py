from Clinica import Clinica
from paciente import Paciente
from medicos import Medico
from Especialidad import Especialidad
from excepcionesClinica import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException)
from datetime import datetime

class CLI:
    def __init__(self):
        self.clinica = Clinica()

    def mostrar_menu(self):
        print("\n--- Menú Clínica ---")
        print("1) Agregar paciente")
        print("2) Agregar médico")
        print("3) Agendar turno")
        print("4) Agregar especialidad a médico")
        print("5) Emitir receta")
        print("6) Ver historia clínica")
        print("7) Ver todos los turnos")
        print("8) Ver todos los pacientes")
        print("9) Ver todos los médicos")
        print("0) Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "0":
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            elif opcion == "1":
                self.agregar_paciente()
            elif opcion == "2":
                self.agregar_medico()
            elif opcion == "3":
                self.agendar_turno()
            elif opcion == "4":
                self.agregar_especialidad()
            elif opcion == "5":
                self.emitir_receta()
            elif opcion == "6":
                self.ver_historia_clinica()
            elif opcion == "7":
                self.ver_todos_los_turnos()
            elif opcion == "8":
                self.ver_todos_los_pacientes()
            elif opcion == "9":
                self.ver_todos_los_medicos()
            else:
                print("Opción inválida. Intente de nuevo")

    # Métodos
    def agregar_paciente(self):
        pass

    def agregar_medico(self):
        pass

    def agendar_turno(self):
        pass

    def agregar_especialidad(self):
        pass

    def emitir_receta(self):
        pass

    def ver_historia_clinica(self):
        pass

    def ver_todos_los_turnos(self):
        pass

    def ver_todos_los_pacientes(self):
        pass

    def ver_todos_los_medicos(self):
        pass

def agregar_paciente(self):
    try:
        nombre = input("Nombre del paciente: ").strip()
        dni = input("DNI del paciente: ").strip()
        fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()
        paciente = Paciente(nombre, dni, fecha_nacimiento)
        self.clinica.agregar_paciente(paciente)
        print("Paciente agregado correctamente")
    except Exception as e:
        print(f"Error al agregar paciente: {e}")

def agregar_medico(self):
    try:
        nombre = input("Nombre del médico: ").strip()
        matricula = input("Matrícula del médico: ").strip()
        medico = Medico(nombre, matricula)
        self.clinica.agregar_medico(medico)
        print("Médico agregado correctamente")
    except Exception as e:
        print(f"Error al agregar médico: {e}")

def agendar_turno(self):
    try:
        dni = input("DNI del paciente: ").strip()
        matricula = input("Matrícula del médico: ").strip()
        especialidad = input("Especialidad: ").strip()
        fecha_str = input("Fecha y hora del turno (dd/mm/aaaa HH:MM): ").strip()
        fecha_hora = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")

        self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
        print("Turno agendado correctamente")
    except (PacienteNoEncontradoException, MedicoNoDisponibleException, TurnoOcupadoException) as e:
        print(f"Error, no se cumple con algunos de los requisitos: {e}")
    except ValueError:
        print("Formato de fecha inválido. Usa dd/mm/aaaa HH:MM.")

def agregar_especialidad(self):
    try:
        matricula = input("Matrícula del médico: ").strip()
        tipo = input("Nombre de la especialidad: ").strip()
        dias_str = input("Días de atención (separados por coma, ej: lunes,miércoles): ").strip()
        dias = [dia.strip().lower() for dia in dias_str.split(",")]

        especialidad = Especialidad(tipo, dias)
        medico = self.clinica.obtener_medico_por_matricula(matricula)
        medico.agregar_especialidad(especialidad)
        print("Especialidad agregada correctamente")
    except Exception as e:
        print(f"Error al agregar especialidad: {e}")

def emitir_receta(self):
    try:
        dni = input("DNI del paciente: ").strip()
        matricula = input("Matrícula del médico: ").strip()
        medicamentos_str = input("Medicamentos (separados por coma): ").strip()
        medicamentos = [m.strip() for m in medicamentos_str.split(",")]

        self.clinica.emitir_receta(dni, matricula, medicamentos)
        print("Receta emitida correctamente")
    except (PacienteNoEncontradoException, MedicoNoDisponibleException, RecetaInvalidaException) as e:
        print(f"Error, no se cumple con algunos de los requisitos: {e}")

def ver_historia_clinica(self):
    try:
        dni = input("DNI del paciente: ").strip()
        historia = self.clinica.obtener_historia_clinica(dni)
        print(historia)
    except PacienteNoEncontradoException as e:
        print(f"Error, no se cumple con algunos de los requisitos: {e}")

def ver_historia_clinica(self):
    try:
        dni = input("DNI del paciente: ").strip()
        historia = self.clinica.obtener_historia_clinica(dni)
        print(historia)
    except PacienteNoEncontradoException as e:
        print(f"Error, no se cumple con algunos de los requisitos: {e}")

def ver_todos_los_turnos(self):
    turnos = self.clinica.obtener_turnos()
    if turnos:
        for turno in turnos:
            print(turno)
    else:
        print("No hay turnos agendados")

def ver_todos_los_pacientes(self):
    pacientes = self.clinica.obtener_pacientes()
    if pacientes:
        for paciente in pacientes:
            print(paciente)
    else:
        print("No hay pacientes registrados")

def ver_todos_los_medicos(self):
    medicos = self.clinica.obtener_medicos()
    if medicos:
        for medico in medicos:
            print(medico)
    else:
        print("No hay médicos registrados")
