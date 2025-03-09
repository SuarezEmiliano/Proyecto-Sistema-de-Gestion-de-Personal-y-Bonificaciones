from Empleadocontrato import Empleadocontrato
from Empleadoplanta import Empleadoplanta
from Empleadovendedor import Empleadovendedor


class Empresa:
    def __init__(self):
        self.empleados = []
        self.cargar_datos_csv()

    def cargar_datos_csv(self):
        file = open('./empleados.csv', 'rt')
        for line in file:
            campos = line[:-1].split(',')
            tipo = int(campos[0])
            codigo = int(campos[1])
            nombre = campos[2] + " " + campos[3]
            salario_base = float(campos[4])
            if tipo == 1:
                antiguedad = int(campos[5])
                empleado = Empleadoplanta(codigo, nombre, salario_base, antiguedad)
            elif tipo == 2:
                proyectos = int(campos[5])
                empleado = Empleadocontrato(codigo, nombre, salario_base, proyectos)
            else:
                ventas = int(campos[5])
                empleado = Empleadovendedor(codigo, nombre, salario_base, ventas)
            self.empleados.append(empleado)
        file.close()

    def __str__(self):
        txt = '==========DATOS DEL ARCHIVO==============\n'
        for empleado in self.empleados:
            txt += str(empleado) + '\n'
        txt += '========================================\n'
        return txt

    def total_a_pagar(self):
        total = 0
        for empleado in self.empleados:
            total += empleado.get_salario()
        return total

    def empleado_salario_mas_bajo(self):
        menor = 0
        nombre_menor = ""
        primero = True
        for empleado in self.empleados:
            if primero:
                menor = empleado.get_salario()
                nombre_menor = empleado.nombre
                primero = False
            else:
                if empleado.get_salario() < menor:
                    menor = empleado.get_salario()
                    nombre_menor = empleado.nombre
        return nombre_menor

    def empleados_planta_mas_antiguedad(self):
        cantidad = 0
        for empleado in self.empleados:
            if isinstance(empleado, Empleadoplanta) and empleado.antiguedad > 5:
                cantidad += 1
        return cantidad

    def empleados_contrato_con_prima(self):
        cantidad = 0
        for empleado in self.empleados:
            if isinstance(empleado, Empleadocontrato) and empleado.proyectos > 3:
                cantidad += 1
        return cantidad

