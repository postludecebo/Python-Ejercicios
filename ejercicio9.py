sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))

venta1 = float(input("Ingrese el monto de la primera venta: "))
venta2 = float(input("Ingrese el monto de la segunda venta: "))
venta3 = float(input("Ingrese el monto de la tercera venta: "))
comision = 0.10 * (venta1 + venta2 + venta3)


total = sueldo_base + comision

print(f"Comisión por las tres ventas: ${comision:.2f}")
print(f"Total a recibir en el mes: ${total:.2f}")