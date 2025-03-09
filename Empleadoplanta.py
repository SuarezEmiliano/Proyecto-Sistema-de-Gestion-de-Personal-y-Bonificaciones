from Empleado import Empleado


class Empleadoplanta(Empleado):
    def __init__(self, codigo, nombre, salario_base, antiguedad):
        super().__init__(codigo, nombre, salario_base)
        self.antiguedad = antiguedad

    def __str__(self):
        emptxt = super().__str__()
        txt = f"PLANTA ==> {emptxt} - ANTIGUEDAD: {self.antiguedad} - SALARIO TOTAL: {self.get_salario()}"
        return txt

    def get_salario(self):
        salario = self.salario_base
        if self.antiguedad > 5:
            salario *= 1.2
        return salario

