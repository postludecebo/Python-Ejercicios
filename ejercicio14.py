articulos = []
for i in range(1, 5):
    nombre = input(f"Ingrese el nombre del artículo {i}: ")
    cantidad = int(input(f"Ingrese la cantidad de '{nombre}': "))
    precio = float(input(f"Ingrese el precio unitario de '{nombre}': "))
    articulos.append({
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio,
        "total": cantidad * precio
    })

subtotal = sum(item["total"] for item in articulos)
iva = subtotal * 0.19
total = subtotal + iva

print("\n--- FACTURA ---")
for item in articulos:
    print(f"{item['nombre']}: {item['cantidad']} x {item['precio']:.0f} = {item['total']:.0f}")
print(f"Subtotal: {subtotal:.0f}")
print(f"IVA (19%): {iva:.0f}")
print(f"Total a pagar: {total:.0f}")