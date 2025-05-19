precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de productos: "))
descuento = float(input("Ingrese el descuento en %: "))

subtotal = precio_unitario * cantidad
subtotal_con_descuento = subtotal * (1 - descuento / 100)
iva = subtotal_con_descuento * 0.19
precio_neto = subtotal_con_descuento + iva

print("\n--- FACTURA ---")
print("Subtotal con descuento:", round(subtotal_con_descuento, 2))
print("IVA (19%):", round(iva, 2))
print("Precio neto:", round(precio_neto, 2))
