# Sistema de Gestión de Clínica

Este proyecto implementa un sistema de gestión médica para una clínica, permitiendo administrar pacientes, médicos, turnos, recetas y sus historias clínicas a través de una interfaz de consola.

---

## Cómo ejecutar el sistema

### Requisitos

* Python 3.10 o superior

### Ejecución

1. Abrí la terminal.
2. Navegá hasta la carpeta del proyecto.
3. Ejecutá:

   ```bash python main.py```
   
4. Se abrirá un menú interactivo para operar la clínica.

---

## Cómo ejecutar las pruebas

1. Asegurate de estar en la carpeta del proyecto.
2. Ejecutá:

   ```bash python -m unittest test_modelo.py```
3. Se correrán todas las pruebas unitarias y verás los resultados en consola.

---

## Diseño General

### 1. Modelo (clases principales)

* `Paciente`, `Medico`, `Turno`, `Receta`, `Especialidad`, `HistoriaClinica`
* Cada clase encapsula atributos y comportamientos propios.

### 2. Excepciones Personalizadas

* Definidas en `excepcionesClinica.py`
* Permiten controlar errores del dominio, como:

  * `PacienteNoEncontradoException`
  * `TurnoOcupadoException`
  * `MedicoNoDisponibleException`
  * `RecetaInvalidaException`

### 3. Clase `Clinica`

* Es el núcleo del sistema.
* Maneja el registro y validación de:

  * Pacientes
  * Médicos
  * Turnos
  * Recetas

### 4. Interfaz CLI (Consola)

* Proporciona un menú interactivo al usuario.
* Solicita datos y llama a la lógica de `Clinica`.
* Captura excepciones y muestra mensajes amigables.

### 5. Pruebas Unitarias

* Realizadas con `unittest`
* Validan:

  * Casos exitosos de registro y operaciones
  * Casos de error (duplicados, inexistencias, validaciones)

---


