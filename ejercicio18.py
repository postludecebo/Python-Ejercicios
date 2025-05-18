matricula = float(input("Ingrese el valor total de la matrícula: "))

cuota1 = matricula * 0.40
cuota2 = matricula * 0.25
cuota3 = matricula * 0.20
cuota4 = matricula * 0.15

print("\n--- VALOR DE CADA CUOTA ---")
print(f"Primera cuota (40%): {cuota1:.0f}")
print(f"Segunda cuota (25%): {cuota2:.0f}")
print(f"Tercera cuota (20%): {cuota3:.0f}")
print(f"Cuarta cuota (15%): {cuota4:.0f}")