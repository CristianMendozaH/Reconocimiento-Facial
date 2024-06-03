#Ejercicio 4

"""
Obtener el precio final que se tiene que pagar si seaplica el 36% de 
descuento del total de la compra.
"""
precioinicial = float(input("Ingrese el precio: "))

descuento = precioinicial * (36/100)

precioinicial = precioinicial-descuento

print(f"El precio final es: Q{precioinicial:.2f}")