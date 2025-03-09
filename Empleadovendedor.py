from Empleado import Empleado


class Empleadovendedor(Empleado):
    def __init__(self, codigo, nombre, salario_base, ventas):
        super().__init__(codigo, nombre, salario_base)
        self.ventas = ventas

    def __str__(self):
        emptxt = super().__str__()
        txt = f"VENDEDOR ==> {emptxt} - VENTAS: {self.ventas} - SALARIO TOTAL: {self.get_salario()}"
        return txt

    def get_salario(self):
        return self.salario_base + (self.ventas * 0.05)

