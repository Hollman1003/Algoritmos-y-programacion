def CalculoEmpresa():
    VentasDepartamento1 = float(input("Ingrese las ventas del Departamento 1: "))
    VentasDepartamento2 = float(input("Ingrese las ventas del Departamento 2: "))
    VentasDepartamento3 = float(input("Ingrese las ventas del Departamento 3: "))
    SalarioBase = float(input("Ingrese el salario bruto de cada vendedor: "))

    VentasTotales = VentasDepartamento1 + VentasDepartamento2 + VentasDepartamento3
    UmbralVentas = VentasTotales * 0.33 

    def CalculoSalarioFinal(ventas_departamento):
        if ventas_departamento > UmbralVentas:
            return SalarioBase * 1.2
        return SalarioBase

    SalarioDepartamento1 = CalculoSalarioFinal(VentasDepartamento1)
    SalarioDepartamento2 = CalculoSalarioFinal(VentasDepartamento2)
    SalarioDepartamento3 = CalculoSalarioFinal(VentasDepartamento3)

    print("\n--- Salarios Finales ---")
    print(f"Vendedores del Departamento 1 tendran: ${SalarioDepartamento1:.2f}")
    print(f"Vendedores del Departamento 2 tendran: ${SalarioDepartamento2:.2f}")
    print(f"Vendedores del Departamento 3 tendran: ${SalarioDepartamento3:.2f}")

CalculoEmpresa()