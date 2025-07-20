'''
  Ejercicios

1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
    1. Si le salen errores, no se asuste. Lealos e intente comprender que significan.
    Los errores son oportunidades de aprendizaje.
    2. Por ejemplo:
        1. string + string ?
        2. string + int ?
        3. int + string ?
        4. list + list ?
        5. string + list ?
        6. float + int ?
        7. bool + bool ?'''

string_1, string_2 = "Hello", "World"
int_1 = 9
list_1, list_2 = [1, 2, 3], [4, 5, 6]
float_1 = 3.14
bool_1, bool_2 = True, False

print(string_1 + string_2)  # HelloWorld
#print(string_1 + int_1)  # Error
#print(int_1 + string_1)  # Error
print(list_1 + list_2)  # [1, 2, 3, 4, 5, 6]
#print(string_1 + list_1)  # Error
print(float_1 + int_1)  # 12.14
print(bool_1 + bool_2)  # 1

'''2. Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé,
niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.'''

nombre = input("Ingrese su nombre: "); apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
if edad <= 5:
    print(f"{nombre} {apellido} es un bebé.")
elif edad <= 13:
    print(f"{nombre} {apellido} es un niño.")
elif edad <= 17:
    print(f"{nombre} {apellido} es un adolescente.")
elif edad <= 35:
    print(f"{nombre} {apellido} es un adulto joven.")
elif edad <= 64:
    print(f"{nombre} {apellido} es un adulto.")
else:
    print(f"{nombre} {apellido} es un adulto mayor.")

'''3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse 
hasta que el usuario adivine el numero.'''

from random import randint
secret_number = randint(1, 10)
guess = 0
while guess != secret_number:
    guess = int(input("Adivina el número: "))
print("Â¡Adivinaste!")

'''4. Cree un programa que le pida tres números al usuario y muestre el mayor.'''

numbers = [int(i) for i in input("Ingrese los números separados por espacios: ").split()]
print(f"El número mayor es {max(numbers)}")

'''5. Dada `n` cantidad de notas de un estudiante, calcular:
    1. Cuantas notas tiene aprobadas (mayor a 70).
    2. Cuantas notas tiene desaprobadas (menor a 70).
    3. El promedio de todas.
    4. El promedio de las aprobadas.
    5. El promedio de las desaprobadas.'''

notas = [int(i) for i in input("Ingrese las notas separadas por espacios: ").split()]
promedio_aprobadas = 0; promedio_desaprobadas = 0
aprobadas = [i for i in notas if i >= 70]
desaprobadas = [i for i in notas if i < 70]
promedio_todas = sum(notas) / len(notas)
if len(aprobadas) >= 1:
    promedio_aprobadas = sum(aprobadas) / len(aprobadas)
if len(desaprobadas) >= 1:
    promedio_desaprobadas = sum(desaprobadas) / len(desaprobadas)

print(f"Notas aprobadas: {len(aprobadas)} \nNotas desaprobadas: {len(desaprobadas)}")
print(f"Promedio de todas las notas: {promedio_todas} \nPromedio de las notas aprobadas: {promedio_aprobadas}")
print(f"Promedio de las notas desaprobadas: {promedio_desaprobadas}")

'''
Ejercicios Extra

1. Pasa los [Ejercicios de Pseudocódigo] previamente creados a código.
2. Pasa los [Ejercicios de Diagramas de Flujo] previamente creados a código.'''

# Ejercicios de Pseudocódigo

precio = int(input("Ingrese el precio: "))
if precio < 100:
    descuento = 0.02
else:
    descuento = 0.1
print(f"El precio final es {precio - precio * descuento}")

tiempo = int(input("Ingrese el tiempo en segundos: "))
if tiempo > 600:
    print("El tiempo es mayor a 10 minutos.")
else:
    print(f"El tiempo restante para los 10 minutos es de {600 - tiempo} segundos.")

n = int(input("Ingrese el número: "))
print(f"La suma de los números del 1 al {n} es {n * (n + 1) / 2}")

nums = [int(i) for i in input("Ingrese los dos números separados por espacios: ").split()]
print("Los números en orden ascendente son: ", end="")
for i in sorted(nums):
    print(i, end=" ")
print()

velocidad = int(input("Ingrese la velocidad en km/h: "))
print(f"{velocidad}km/h son {velocidad / 3.6}m/s")

mujer = 0; hombre = 0
nums = [int(i) for i in input("Ingrese los sexos separados por espacios (1s y 2s): ").split()]
for i in nums:
    mujer = mujer + 1 if i == 1 else mujer
    hombre = hombre + 1 if i == 2 else hombre
print(f"{round(100 / len(nums) * mujer, 2)}% son de sexo femenino y {round(100 / len(nums) * hombre, 2)}% son de sexo masculino.")

# Ejercicios de Diagramas de Flujo

secret_number = randint(1, 10)
guess = 0
while guess != secret_number:
    guess = int(input("Adivina el número: "))
print("¡Adivinaste!")

list = [int(i) for i in input("Ingrese los números separados por espacios: ").split()]
for i in list:
    if i == 30:
        print("Correcto")
        list = 0
        break
if list:
    if sum(list) == 30:
        print("Correcto")
        list = 0
if list:
    print("Incorrecto")

list = [int(i) for i in input("Ingrese los números separados por espacios: ").split()]
print(f" el mayor número es {max(list)}")

n = int(input("Ingrese el número: ")); text = ""
if n % 3 == 0:
    text += "Fizz"
if n % 5 == 0:
    text += "Buzz"
print(text)

list = [int(i) for i in input("Ingrese los números separados por espacios: ").split()]
print(f"La suma de los números es {sum(list)}")

list = [int(i) for i in input("Ingrese los números separados por espacios: ").split()]
print(f" el mayor número es {max(list)}")