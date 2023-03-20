""" nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65,29,42]
ciudades = ['Caracas', 'Maracay', 'Baquisimeto']

combinados = list(zip(nombres,edades,ciudades))
print(combinados)

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} y vive en {ciudad}") """

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinados = list(zip(capitales,paises))

for capital, pais in combinados:
    print(f"{capital} es la capital de {pais}")    
