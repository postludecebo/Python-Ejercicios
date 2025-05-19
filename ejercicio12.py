total = int(input("Ingrese el número total de alumnos: "))
hombres = int(input("Ingrese el número de hombres: "))
mujeres = int(input("Ingrese el número de mujeres: "))
porcentaje_hombres = (hombres / total) * 100
porcentaje_mujeres = (mujeres / total) * 100
print(f"Porcentaje de hombres: {porcentaje_hombres:.2f}%")
print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")