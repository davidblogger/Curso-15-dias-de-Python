#conversiones implicitas

num1 = 20
num2 = 30.5

num1 = num1 + num2

#print(type(num1))
#print(type(num2))


#Conversiones explicitas

num1 = 5.8
print(num1)
print(type(num1))

num2 = int(num1)
print(num2)
print(type(num2))

edad = int(input("Dime tu edad: "))
print(edad)
print(type(edad))

nueva_edad = 1 + edad
print(f"Tu nueva es: {nueva_edad}")