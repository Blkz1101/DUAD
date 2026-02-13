'''Ejercicios

1. Cree una clase de `BankAccount` que:
    1. Tenga un atributo de `balance`.
    2. Tenga un método para ingresar dinero.
    3. Tengo un método para retirar dinero.
    
    Cree otra clase que herede de esta llamada `SavingsAccount` que:
    
    1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
    2. Arroje un error si al intentar retirar dinero, el retiro haría que el `balance` quede 
    debajo del `min_balance`. Es decir que sí se pueden hacer retiros **siempre y cuando** el 
    `balance` quede arriba del `min_balance`.'''

class BankAccount():
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("The amount must be positive")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")

class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        self.min_balance = min_balance
    
    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        elif self.balance - amount < self.min_balance:
            raise ValueError("You can't withdraw this amount: The balance would be below the minimum balance")
        else: 
            self.balance -= amount

'''2. Cree una clase abstracta de `Shape` que:
    1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
    2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
    3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.'''

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass

    @abstractmethod
    def calculate_area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self):
        self.radius = 0; self.diameter = 0

    def calculate_perimeter(self) -> float:
        if self.diameter <= 0:
            if self.radius > 0:
                return (self.radius * 2 * pi)
            else:
                raise ValueError("The radius and diameter are not stated or below 0")
        return (self.diameter * pi)

    def calculate_area(self) -> float:
        if self.radius <= 0:
            if self.diameter > 0:
                return (pi * (self.diameter / 2) ** 2)
            else:
                raise ValueError("The radius and diameter are not stated or below 0")
        return (pi * self.radius ** 2)
    
class Square(Shape):
    def __init__(self):
        self.side_length = 0

    def calculate_perimeter(self) -> float:
        if self.side_length > 0:
            return (self.side_length * 4)
        else:
            raise ValueError("The side length is not stated or below 0")
    
    def calculate_area(self) -> float:
        if self.side_length > 0:
            return (self.side_length ** 2)
        else:
            raise ValueError("The side length is not stated or below 0")
    
class Rectangle(Shape):
    def __init__(self):
        self.height = 0; self.width = 0

    def calculate_perimeter(self) -> float:
        if self.height > 0:
            if self.width > 0:
                return (self.height * 2 + self.width * 2)
            else:
                raise ValueError("The width length is not stated or below 0")
        else:
            raise ValueError("The height length is not stated or below 0")
    
    def calculate_area(self) -> float:
        if self.height > 0:
            if self.width > 0:
                return (self.height * self.width)
            else:
                raise ValueError("The width length is not stated or below 0")
        else:
            raise ValueError("The height length is not stated or below 0")
        
'''3. Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.'''

class HasPosition():
    def __init__(self):
        self.xpos = 0; self.ypos = 0

class CanMove():
    def move(self, direction, amount):
        if direction == "right":
            self.xpos += amount
        elif direction == "left":
            self.xpos -= amount

class CanJump():
    def jump(self, amount):
        self.ypos -= amount
        #Esto tomando en cuenta que las coordenadas (0,0) son arriba a la izquierda de la pantalla

class CanFall():
    def fall(self, amount):
        self.ypos += amount

class Human(HasPosition, CanMove, CanJump, CanFall):
    pass

class Elephant(HasPosition, CanMove, CanFall):
    pass

'''Ejercicios Extra

1. Cree una clase `Employee` con los siguientes requisitos:
    - Atributos privados: `_name`, `_salary`
    - Use `@property` y `@<atributo>.setter` para:
        - Mostrar el nombre y el salario
        - Validar que el salario nunca sea negativo
    - Cree un método `promote` que aumente el salario un porcentaje definido'''

class Employee:
    def __init__(self, name: str, salary: float):
        self._name = name
        self._salary = salary

    @property
    def name(self) -> str:
        return self._name

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    def promote(self, percent: float):
        if percent < 0:
            raise ValueError("Percent must be positive")
        self.salary += self.salary * (percent / 100)


'''2. Cree una clase abstracta `User` con los siguientes métodos abstractos:
    - `get_role()`
    - `has_permission(permission)`
- Luego cree dos clases que hereden de ella:
    - `AdminUser`
    - `RegularUser`
- Cada una debe implementar los métodos'''

class User(ABC):
    @abstractmethod
    def get_role(self) -> str:
        pass

    @abstractmethod
    def has_permission(self, permission: str) -> bool:
        pass

class AdminUser(User):
    def get_role(self) -> str:
        return "Admin"

    def has_permission(self, permission: str) -> bool:
        return True  
    
class RegularUser(User):
    def __init__(self, permissions: list[str]):
        self.permissions = permissions

    def get_role(self) -> str:
        return "Regular"

    def has_permission(self, permission: str) -> bool:
        return permission in self.permissions

'''3. Cree una clase base `Vehicle` con los atributos:
    - `_brand`
    - `_year`
- Agregue un método `get_info()` que devuelva una descripción del vehículo.
- Luego cree dos clases hijas:
    - `Car`
    - `Motorcycle`
- Cada una debe agregar su propio atributo (por ejemplo, `doors` o `type`) y sobrescribir
el método `get_info()` para incluir esta información adicional.'''

class Vehicle:
    def __init__(self, brand: str, year: int):
        self._brand = brand
        self._year = year

    def get_info(self) -> str:
        return f"Brand: {self._brand}, Year: {self._year}"


class Car(Vehicle):
    def __init__(self, brand: str, year: int, doors: int):
        super().__init__(brand, year)
        self.doors = doors

    def get_info(self) -> str:
        base = super().get_info()
        return f"{base}, Doors: {self.doors}"


class Motorcycle(Vehicle):
    def __init__(self, brand: str, year: int, moto_type: str):
        super().__init__(brand, year)
        self.moto_type = moto_type

    def get_info(self) -> str:
        base = super().get_info()
        return f"{base}, Type: {self.moto_type}"