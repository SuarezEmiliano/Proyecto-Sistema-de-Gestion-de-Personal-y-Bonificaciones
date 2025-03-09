from Empleado import Empleado


class Empleadocontrato(Empleado):
    def __init__(self, codigo, nombre, salario_base, proyectos):
        super().__init__(codigo, nombre, salario_base)
        self.proyectos = proyectos

    def __str__(self):
        emptxt = super().__str__()
        txt = f"CONTRATO ==> {emptxt} - PROYECTOS: {self.proyectos} - SALARIO TOTAL: {self.get_salario()} - RECIBE PRIMA?: {self.recibe_prima()}"
        return txt

    def get_salario(self):
        return self.salario_base

    def recibe_prima(self):
        if self.proyectos > 3:
            return "SI"
        return "NO"
