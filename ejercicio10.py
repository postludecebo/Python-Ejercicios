total_compra = float(input("Ingrese el total de la compra: $"))
descuento = total_compra * 0.15
total_pagar = total_compra - descuento
print(f"El total a pagar con el 15% de descuento es: ${total_pagar:.0f}")
