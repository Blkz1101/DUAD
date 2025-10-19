'''1. Cree una clase de `Circle` con:
    1. Un atributo de `radius` (radio).
    2. Un método de `get_area` que retorne su área.'''

import math

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * pow(self.radius, 2)

'''2. Cree una clase de `Bus` con:
    1. Un atributo de `max_passengers`.
    2. Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase `Person` vista en la lección). **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
    3. Un método para bajar pasajeros uno por uno (en cualquier orden).'''

class Person():
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Bus():
    def __init__(self, max):
        self.max_passengers = max
        self.current_passengers = 0
        self.passengers = []

    def add(self, passenger):
        if self.current_passengers < self.max_passengers:
            self.passengers.append(passenger)
            self.current_passengers += 1
        else: return "El bus está lleno"

    def drop_off(self):
        self.current_passengers -= 1
        return self.passengers.pop(0)
    
'''Duplique el proyecto Sistema de Control de Estudiantes y modifíquelo para usar objetos para guardar la información de los estudiantes (creando una clase de Student).
Hay que cambiar los estudiantes de diccionarios a objetos.
Hay que convertir la data del csv (que viene por defecto en formato de diccionario) a objetos al importarla.
Hay que convertir los objetos a diccionarios para poder exportarlos a csv.
Hay que modificar el acceso a los keys para accesar a atributos.
student[’Name’] → student.name'''

'''Cree las siguientes clases:
Head
Torso
Arm
Hand
Leg
Feet'''

class Head():
    def __init__(self, hair_color, eye_color, hair_length):
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.eyes_size = hair_length

class Torso():
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Arm():
    def __init__(self, hand):
        self.hand = hand

class Hand():
    def __init__(self):
        pass

class Leg():
    def __init__(self, feet):
        self.feet = feet

class Feet():
    def __init__(self):
        pass

'''Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.'''

class Human():
    def __init__(self, torso):
        self.torso = torso

left_hand = Hand(); right_hand = Hand()
left_feet = Feet(); right_feet = Feet()
left_arm = Arm(left_hand); right_arm = Arm(right_hand)
left_leg = Leg(left_feet); right_leg = Leg(left_leg)
head = Head("Brown", "Green", "Short")
torso = Torso(head, right_arm, left_arm, right_leg, left_leg)
human = Human(torso)

'''Cree una clase Rectangle que:
Tenga atributos width y height
Tenga un método get_area() que retorne el área
Tenga un método get_perimeter() que retorne el perímetro
Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado'''

class Rectangle():
    def __init__(self, width, height):
        if width < 0:
            raise ValueError("Width cannot be a negative number")
        elif height < 0:
            raise ValueError("Height cannot be a negative number")
        else:
            self.width = width; self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return self.width * 2 + self.height * 2
    
'''Cree una clase de Car con:
Atributos: brand, model y speed (inicia en 0).
Métodos:
accelerate(amount) → aumenta la velocidad en la cantidad indicada.
brake(amount) → disminuye la velocidad en la cantidad indicada (sin bajar de 0).
__str__() → retorna un texto con los atributos como "Toyota Corolla - Velocidad: 50 km/h".'''

class Car():
    def __init__(self, brand, model):
        self.brand = brand; self.model = model
        self.speed = 0
    def accelerate(self, amount):
        self.speed += amount
    def brake(self, amount):
        self.speed -= amount
    def __str__(self):
        return f'{self.brand} {self.model} - Velocidad: {self.speed} km/h'