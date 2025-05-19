from datetime import datetime

nombre = input("Nombre: ")
direccion = input("Dirección: ")
anio_nacimiento = int(input("Año de nacimiento: "))

anio_actual = datetime.now().year
edad = anio_actual - anio_nacimiento

print("\n--- INFORMACIÓN ---")
print(f"Nombre: {nombre}")
print(f"Dirección: {direccion}")
print(f"Edad: {edad} años")
