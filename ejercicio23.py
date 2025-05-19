altura_referencia = 7
tiempo_referencia = 5  

altura = float(input("Ingrese la altura que desea subir (en metros): "))
tiempo_estimado = (altura / altura_referencia) * tiempo_referencia

print("Tiempo estimado para subir:", round(tiempo_estimado, 2), "horas")
