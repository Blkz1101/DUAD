# Cree una calculadora por linea de comando. Esta debe de tener un número actual, 
# y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, 
# restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo número actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción inválida, 
# o si ingresa un número inválido a la hora de hacer la operación.

import os

def main():
    actual = 0; option = 0
    while True:
        print("1. Suma \n2. Resta \n3. Multiplicación \n4. División \n5. Borrar resultado \n6. Ver resultado \n")
        try:
            option = int(input())
            if option < 1 or option > 6:
                raise Exception    
        except:
            print("Ingrese un número entero dentro de las opciones")
        if option == 1:
            try:
                num = int(input("n: "))
                actual += num
            except:
                print("Ingrese un número válido")
        elif option == 2:
            try:
                num = int(input("n: "))
                actual -= num
            except:
                print("Ingrese un número válido")
        elif option == 3:
            try:
                num = int(input("n: "))
                actual *= num
            except:
                print("Ingrese un número válido")
        elif option == 4:
            try:
                num = int(input("n: "))
                actual /= num
            except:
                print("Ingrese un número válido")
        elif option == 5:
            actual = 0
        elif option == 6:
            print("Resultado: ", actual)
        input()
        os.system("cls")
    
if __name__ == '__main__':
    main()
