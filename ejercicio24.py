monto = float(input("Ingrese el monto del préstamo: "))
interes_anual = 0.05
años = 5

interes_anio = monto * interes_anual
interes_trimestre3 = interes_anio / 4  
interes_mes1 = interes_anio / 12
total_pagado = monto + (interes_anio * años)

print("\n--- INFORMACIÓN DEL PRÉSTAMO ---")
print("Interés por año:", round(interes_anio, 2))
print("Interés tercer trimestre:", round(interes_trimestre3, 2))
print("Interés primer mes:", round(interes_mes1, 2))
print("Total a pagar al final del préstamo:", round(total_pagado, 2))
