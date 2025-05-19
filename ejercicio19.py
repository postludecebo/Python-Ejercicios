nombre = input("Ingrese el nombre del estudiante: ")
programa = input("Ingrese el programa de formación: ")
ficha = input("Ingrese la ficha del curso: ")

notas = []
for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)

print("\n--- RESULTADOS ---")
print("Nombre:", nombre)
print("Programa:", programa)
print("Promedio final:", round(promedio, 2))
