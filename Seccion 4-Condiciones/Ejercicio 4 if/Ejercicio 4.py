#Ejercicio 4
"""
Crear un programa que simule un cajero automatico 
con un saldo inicial de $2000, con el siguiente menu:

1. Ingreso de dinero
2. Retirar dinero 
3. Mostrar dinero
4. Salir
"""
#La F es para unir cadenas y bool y int
saldo = 2000

print("1. Ingreso de dinero")
print("2. Retirar dinero ")
print("3. Mostrar dinero")
print("4. Salir")

seleccion = int(input("Elija una opcion: "))

if seleccion==1:
    ingreso=float(input("Dinero a ingresar: "))
    saldo += ingreso
    print(f"Nuevo saldo en la cuenta: {saldo}")
elif seleccion==2:
    salida=float(input("Dinero a retirar: "))
    if salida > saldo: 
        print("Saldo insuficiente")
    else:
        saldo-=salida
        print(f"Nuevo saldo disponible: {saldo}")
elif seleccion==3:
    print(f"Saldo disponible: {saldo}")
elif seleccion==4:
    print("Fin")
else:
    print("Erro de entrada de dato")
