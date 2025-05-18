salario = float(input("Ingrese el salario del empleado: "))
ahorro_mensual = float(input("Ingrese el valor de ahorro mensual programado: "))

deduccion_salud = salario * 0.125
deduccion_pension = salario * 0.16
total_deducciones = deduccion_salud + deduccion_pension + ahorro_mensual
total_recibir = salario - total_deducciones

print("\n--- COLILLA DE PAGO ---")
print(f"Salario del Empleado: {salario:.0f}")
print(f"Valor de Ahorro mensual programado: {ahorro_mensual:.0f}")
print(f"Aporte a la Salud (EPS 12.5%): {deduccion_salud:.0f}")
print(f"Aporte al Fondo de Pensiones (16%): {deduccion_pension:.0f}")
print(f"Total a Recibir: {total_recibir:.0f}")