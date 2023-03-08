#Proyecto para calcular comisiones por venta de empleados

vendedor = input("Ingresa tu nombre: ")
ingreso = int(input("Ingresa la cantidad que vendiste: "))

comision = round((ingreso * 13) / 100,2)

print(f"Saludos {vendedor} tus comisiones por venta son: ${comision}")