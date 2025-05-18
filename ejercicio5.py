# Lea la distancia (en kilómetros) recorrida por un auto, el tiempo (en horas) en que la recorrió y calcule la velocidad a la cual se desplazaba el auto (V=D/T).
distancia = float(input("Ingrese los kilometros recorridos: \n"))
tiempo = float(input("Ingrese las horas: \n"))

velocidad = distancia / tiempo

print(f"La velocidad fue {velocidad}Km/H")