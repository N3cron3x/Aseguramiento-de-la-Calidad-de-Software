import pytest
from datetime import datetime, timedelta

class SistemaSaludConecta:
    def __init__(self):
        self.citas_programadas = []
        self.historias_clinicas = {}

    def programar_cita(self, paciente_id, fecha_hora):
        if fecha_hora < datetime.now():
            return {"status": "error", "mensaje": "Fecha invalida"}
        if fecha_hora in self.citas_programadas:
            return {"status": "error", "mensaje": "Horario no disponible"}
        self.citas_programadas.append(fecha_hora)
        return {"status": "exito", "mensaje": "Cita confirmada"}

    def registrar_historia_clinica(self, paciente_id, datos):
        if not paciente_id:
            return {"status": "error", "mensaje": "ID de paciente requerido"}
        self.historias_clinicas[paciente_id] = datos
        return {"status": "exito", "mensaje": "Historia guardada"}

@pytest.fixture
def sistema():
    return SistemaSaludConecta()

def test_programar_cita_exitosa(sistema):
    fecha_futura = datetime.now() + timedelta(days=1)
    resultado = sistema.programar_cita("PAC-001", fecha_futura)
    assert resultado["status"] == "exito"

def test_programar_cita_error_pasado(sistema):
    fecha_pasada = datetime.now() - timedelta(days=1)
    resultado = sistema.programar_cita("PAC-001", fecha_pasada)
    assert resultado["status"] == "error"

def test_registro_historia_exitoso(sistema):
    datos = {"diagnostico": "Consulta General", "tratamiento": "Medicamento X"}
    resultado = sistema.registrar_historia_clinica("PAC-123", datos)
    assert resultado["status"] == "exito"