'''Ejercicios
1. Cree un decorador que haga print de los parámetros y retorno de la función que decore.'''

def decor(func):
    def wrapper(*args, **kwargs):
        print(f"Parameters: {args}, {kwargs}")
        f = func(*args)
        print(f"Result: {f}")
        return f
    return wrapper

@decor
def func(n, m):
    return n + m

func(3, 4)

'''2. Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore 
son números, y arroje una excepción de no ser así.'''

def validate_numbers(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("All arguments have to be numbers")
        return func(*args)
    return wrapper

@validate_numbers
def func(*args):
    print(args)

#func(2, 16, 128, '1024')
func(2, 16, 128, 1024)

'''3. Cree una clase de `User` que:
    - Tenga un atributo de `date_of_birth`.
    - Tenga un property de `age`.
    
    Luego cree un decorador para funciones que acepten un `User` como parámetro que se 
encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.'''

from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year
    
def adult_required(func):
    def wrapper(user):
        if user.age < 18:
            raise Exception("User is not an adult")
        return func(user)
    return wrapper

@adult_required
def enter_club(user):
    print("Welcome to the club")

u1 = User(date(2000, 5, 1))
u2 = User(date(2010, 5, 1))

enter_club(u1)
#enter_club(u2)

'''Ejercicios adicionales
1. Cree una función que imprima “Hola, [nombre]” dos veces:
- Cree un decorador `@repeat_twice` que haga que la función 
decorada se ejecute dos veces seguidas, con los mismos argumentos'''

def repeat_twice(func):
    def wrapper(*args):
        func(*args)
        func(*args)
    return wrapper

@repeat_twice
def func(name):
    print(f"Hola, {name}")
    print(f"Hola, {name}")

func("Blkz")
        
'''1. Cree un decorador `@requires_login` que:
- Verifique si la variable global `user_logged_in` es `True`
- Si no lo es, debe lanzar una excepción `"Usuario no autenticado"`
- Si lo es, la función decorada se ejecuta normalmente'''

user_logged_in = True
#user_logged_in = False
def requires_login(func):
    def wrapper(*args):
        if not user_logged_in:
            raise Exception("Usuario no autenticado")
        return func(*args)
    return wrapper

@requires_login
def func(*args):
    print(args)

func(2, 16, 128, 1024)
        
'''2. Cree una función que se llame `multiply`, la cual obtiene dos valores y los multiplica entre si
- A esta función  se le debe combinar dos decoradores:
    - `@log_call`: imprime el nombre de la función, los argumentos, fecha actual y el retorno
    - `@validate_numbers`: revisa que todos los argumentos sean numéricos'''

def validate_numbers(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("All arguments have to be numbers")
        return func(*args)
    return wrapper

date = "08/03/2026"
def log_call(func):
    def wrapper(*args):
        print(f"Function name: {func.__name__}")
        print(f"Arguments: {args}")
        print(f"Date: {date}")
        f = func(*args)
        print(f"Function result: {f}")
        return f
    return wrapper

@validate_numbers
@log_call
def multiply(x, y):
    return x * y

multiply(3, 8)
#multiply(3, '8')