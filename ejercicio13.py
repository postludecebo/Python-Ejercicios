try:
    horas = int(input("Ingrese las horas trabajadas: \n"))
    if horas < 0:
        raise Exception("Ingrese un número de horas positivo.")
except Exception as a:
    print(a)
else:
    try:
        valor_hora = int(input("Ingrese el valor de la hora: \n"))
        if valor_hora < 0:
            raise Exception("Ingrese el valor de hora positivo.")
    except Exception as a:
        print(a)
    else:
        salario = horas * valor_hora
        print(f"Su salario es de {salario}")

