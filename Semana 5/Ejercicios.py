# 1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
# Ejemplo:
first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']
for i in range(len(first_list)):
    print(first_list[i], second_list[i])

# 2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
# Ejemplo:
my_string = 'Pizza con piña'
for i in range(len(my_string)-1, -1, -1):
    print(my_string[i])

# 3. Cree un programa que intercambie el primer y ultimo elemento de una lista.
# Ejemplo:
my_list = [4, 3, 6, 1, 7]
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)

# 4. Cree un programa que elimine todos los números impares de una lista.
# Ejemplo:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
modified_numbers = [i for i in numbers if i % 2 == 0]
print(modified_numbers)

# 5. Cree un programa que le pida al usuario 10 números y al final le muestre todos los números que ingresó, seguido del número ingresado más alto.
# Ejemplo:
numbers = [int(i) for i in input('Ingrese 10 números separados por coma: ').split(',')]
print(f"{numbers}. El número más alto fue {max(numbers)}")

# **Ejercicios**

# 1. Cree un diccionario que guarde la siguiente información sobre un hotel:
hotel = {
    'nombre': 'Las Nevadas',
    'numero_de_estrellas': 5,
    'habitaciones': [
        {'numero': 101, 'piso': 1, 'precio_por_noche': 200},
        {'numero': 102, 'piso': 1, 'precio_por_noche': 200},
        {'numero': 103, 'piso': 2, 'precio_por_noche': 270},
        {'numero': 104, 'piso': 2, 'precio_por_noche': 270}
    ]
}

# 2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys y la otra para sus values.
# Ejemplo:
def create_dict(a, b):
    dictionary = {}
    for i in range(len(a)):
        dictionary[a[i]] = b[i]
    return dictionary

list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']
print(create_dict(list_a, list_b))

# 3. Cree un programa que use una lista para eliminar keys de un diccionario.
# Ejemplo:
def delete_element(keys, d):
    for key in keys:
        d.pop(key, None)
    return d

list_of_keys = ['access_level', 'age']
employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}
print(delete_element(list_of_keys, employee))