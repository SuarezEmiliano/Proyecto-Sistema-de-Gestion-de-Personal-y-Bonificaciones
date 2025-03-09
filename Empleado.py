class Empleado:
    def __init__(self, codigo, nombre, salario_base):
        self.codigo = codigo
        self.nombre = nombre
        self.salario_base = salario_base

    def __str__(self):
        return f"CÓDIGO: {self.codigo} - NOMBRE: {self.nombre} - SALARIO BASE: {self.salario_base}"

