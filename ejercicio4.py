nota_uno = float(input("Ingrese la nota número 1:\n"))
nota_dos = float(input("Ingrese la nota número 2:\n"))
nota_tres = float(input("Ingrese la nota número 3:\n"))

nota_uno *= 0.2
nota_dos *= 0.3
nota_tres *= 0.5

definitiva = (nota_uno + nota_dos + nota_tres)
print(f"La definitiva es: {definitiva}")