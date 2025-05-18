# Lea la cantidad de dinero correspondiente a una compra y calcule el valor del IVA (19%), y el valor total de la factura, si al valor de la compra se le autoriza un descuento del 10% (antes de aplicarle el IVA).
IVA = 19 / 100
DESCUENTO = 10 / 100

compra = int(input("Ingrese el precio de la compra en COP: \n"))
iva_compra = (compra * IVA) 
total_iva = iva_compra + compra
descuento_compra = (compra * DESCUENTO) 
total_descuento = compra - descuento_compra  
total = total_descuento + iva_compra

print(f""" FACTURA
      Precio: {compra}COP
      IVA: {iva_compra}COP
      Total IVA: {total_iva}
      Descuento compra: {descuento_compra}
      Total descuento: {total_descuento}
      Total: {total}""")