# Ejercicio 1: Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def exercise_1():
    def two():
        print('Executing two')

    def one():
        print('Executing one')
        two()

    one()

# Ejercicio 2: Experimente con el concepto de scope.

def exercise_2():
    # Intentando acceder a una variable local desde fuera de la función (esto no funcionará)
    local_var = 3
    # print(local_var)  # Esto causaría un error porque local_var es local a la función

exercise_2()

# Accediendo a una variable global desde una función y cambiando su valor
global_var = 4

def exercise_2_2():
    global global_var  # Usamos la palabra clave 'global' para modificar la variable global
    global_var = 5

exercise_2_2()
print(global_var)  # Ahora la variable global var ha sido cambiada a 5

# Ejercicio 3: Cree una función que retorne la suma de todos los números de una lista.

def exercise_3():
    def sum_list(numbers):
        result = 0
        for num in numbers:
            result += num
        return result

    print(sum_list([4, 6, 2, 29]))  # Debería imprimir 41

# Ejercicio 4: Cree una función que le de la vuelta a un string y lo retorne.

def exercise_4():
    def reverse(word):
        return word[::-1]
    
    print(reverse('Hola mundo'))  # Debería imprimir "odnum aloH"

# Ejercicio 5: Cree una función que imprima el número de mayúsculas y minúsculas en un string.

def exercise_5():
    def count_upper_lower(string):
        upper = 0
        lower = 0
        for letter in string:
            if letter.isupper():
                upper += 1
            elif letter.islower():
                lower += 1
        print(f"There's {upper} upper cases and {lower} lower cases")

    count_upper_lower('I love Nación Sushi')  # Debería imprimir "There's 3 upper cases and 13 lower cases"

# Ejercicio 6: Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.

def exercise_6():
    def sort_string(string):
        words = string.split('-')
        words.sort()
        return '-'.join(words)

    print(sort_string('python-variable-funcion-computadora-monitor'))  # Debería imprimir "computadora-funcion-monitor-python-variable"

# Ejercicio 7: Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def exercise_7():
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):  # Mejorar la eficiencia limitando la iteración
            if num % i == 0:
                return False
        return True
    
    def get_primes(numbers):
        primes = []
        for num in numbers:
            if is_prime(num):
                primes.append(num)
        return primes
    
    print(get_primes([1, 4, 6, 7, 13, 9, 67]))  # Debería imprimir [7, 13, 67]

# Función principal para ejecutar todos los ejercicios

def main():
    exercise_1()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()

if __name__ == '__main__':
    main()