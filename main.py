from Empresa import Empresa


def main():
    empresa = Empresa()
    print(empresa)
    total_a_pagar = empresa.total_a_pagar()
    empleado_menor_salario = empresa.empleado_salario_mas_bajo()
    cant_empleados_mas_antiguedad = empresa.empleados_planta_mas_antiguedad()
    cant_empleados_con_prima = empresa.empleados_contrato_con_prima()

    print(f"EL TOTAL A PAGAR EN SALARIOS ES: {total_a_pagar}")
    print(f"EL EMPLEADO CON EL SALARIO MÁS BAJO ES: {empleado_menor_salario}")
    print(f"LA CANTIDAD DE EMPLEADOS DE PLANTA CON BONIFICACIÓN POR TENER MÁS DE 5 AÑOS DE ANTIGUEDAD ES: {cant_empleados_mas_antiguedad}")
    print(f"LA CANTIDAD DE EMPLEADOS POR CONTRATO CON PRIMA ES: {cant_empleados_con_prima}")


if __name__ == '__main__':
    main()
