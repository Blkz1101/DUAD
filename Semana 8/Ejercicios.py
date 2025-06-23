import csv, json
from time import sleep
from os import system

def ordenar_canciones(entrada, salida):
    try:
        with open(entrada, 'r', encoding='utf-8') as f:
            lineas = f.readlines()

        canciones = []
        for l in lineas:
            if l.strip() != '':
                canciones.append(l.strip())

        canciones.sort()

        with open(salida, 'w', encoding='utf-8') as f:
            for c in canciones:
                f.write(c + '\n')
    except:
        print("Ocurrió un error al procesar los archivos")

def informacion_juegos():
    archivo = open('videojuegos.csv', 'w', newline='', encoding='utf-8')
    escritor = csv.writer(archivo)

    escritor.writerow(['nombre', 'genero', 'desarrollador', 'clasificacion'])

    seguir = 's'
    while seguir == 's':
        nombre = input("Nombre del videojuego: ")
        genero = input("Género: ")
        desarrollador = input("Desarrollador: ")
        clasificacion = input("Clasificación ESRB: ")

        escritor.writerow([nombre, genero, desarrollador, clasificacion])

        seguir = input("¿Quieres ingresar otro videojuego? (s/n): ")

    archivo.close()

def informacion_juegos_tab():
    archivo = open('videojuegos.tsv', 'w', newline='', encoding='utf-8')
    escritor = csv.writer(archivo, delimiter='\t')

    escritor.writerow(['nombre', 'genero', 'desarrollador', 'clasificacion'])

    seguir = 's'
    while seguir == 's':
        nombre = input("Nombre del videojuego: ")
        genero = input("Género: ")
        desarrollador = input("Desarrollador: ")
        clasificacion = input("Clasificación ESRB: ")

        escritor.writerow([nombre, genero, desarrollador, clasificacion])

        seguir = input("¿Quieres ingresar otro videojuego? (s/n): ")

    archivo.close()

def informacion_pokemones():
    archivo = 'pokemones.json'

    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lista_pokemones = json.load(f)
    except FileNotFoundError:
        lista_pokemones = []

    nombre = input("Nombre del Pokémon: ")

    tipo_input = input("Tipo(s) (si son varios, sepáralos por coma): ")
    tipo = [t.strip() for t in tipo_input.split(',')]

    try:
        hp = int(input("HP: "))
        attack = int(input("Ataque: "))
        defense = int(input("Defensa: "))
        sp_attack = int(input("Sp. Ataque: "))
        sp_defense = int(input("Sp. Defensa: "))
        speed = int(input("Velocidad: "))
    except ValueError:
        print("Todos los stats deben ser números enteros")
        return

    nuevo_pokemon = {
        "name": {
            "english": nombre
        },
        "type": tipo,
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }

    lista_pokemones.append(nuevo_pokemon)

    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(lista_pokemones, f, indent=4, ensure_ascii=False)

    print(f"\n{nombre} añadido correctamente")
    sleep(2)

def main():    
    print("Bienvenido al programa de gestión de archivos")
    print("1. Ordenar canciones")
    print("2. Información de videojuegos en CSV")
    print("3. Información de videojuegos en TSV")
    print("4. Información de Pokémon en JSON")
    print("5. Salir")
    opcion = int(input("Selecciona una opción: "))
    while opcion != 5:
        if opcion == 1:
            entrada = input("Nombre del archivo de entrada: ")
            salida = input("Nombre del archivo de salida: ")
            ordenar_canciones(entrada, salida)
        elif opcion == 2:
            informacion_juegos()
        elif opcion == 3:
            informacion_juegos_tab()
        elif opcion == 4:
            informacion_pokemones()
        else:
            print("Opción no válida")
            sleep(2)
        system('cls')
        print("1. Ordenar canciones")
        print("2. Información de videojuegos en CSV")
        print("3. Información de videojuegos en TSV")
        print("4. Información de Pokémon en JSON")
        print("5. Salir")
        opcion = int(input("Selecciona una opción: "))

if __name__ == "__main__":
    main()