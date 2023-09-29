print("Start Task #1")

"""1.	Дан код. Исправить его в соответствии с принципом DRY."""

import sqlite3


class DatabaseManager:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.database_name)

    def execute_sql_query(self, query):
        if self.connection is None:
            self.connect()

        try:
            with self.connection:
                cur = self.connection.cursor()
                cur.execute(query)
                results = cur.fetchall()
                for line in results:
                    print(line)
        except sqlite3.Error as e:
            print("Ошибка при выполнении SQL запроса:", e)


QUERY_1 = 'SELECT name FROM users'
QUERY_2 = 'SELECT name FROM customers'

database_manager = DatabaseManager('database1.db')
database_manager.execute_sql_query(QUERY_1)
database_manager = DatabaseManager('database2.db')
database_manager.execute_sql_query(QUERY_2)

print("End Task #1\n")

print("Start Task #2")
"""2.	Дан код. Исправить его в соответствии с принципом KISS."""


def calculate_complex_formula(a, b, c, d, e, f, g, h):
    if a > 0:
        result = b * c
    else:
        result = -d / e

    if g < h:
        result += f * (g + h)
    else:
        result -= (d - f) / g
    return result


print(calculate_complex_formula(1, 2, 3, 4, 5, 6, 7, 8))

print("End Task #2\n")

print("Start Task #3")

"""3.	Дан код. Исправить его в соответствии с принципом POLA."""


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18


MESSAGE_ADULT = "Добро пожаловать на сайт для взрослых."
MESSAGE_CHILD = "Добро пожаловать на детский сайт."


def greet_user(user):
    if user.is_adult():
        greeting = MESSAGE_ADULT
    else:
        greeting = MESSAGE_CHILD

    print(f"Привет, {user.name}! {greeting}")


user1 = User("Алекс", 25)
greet_user(user1)

user2 = User("Лиза", 12)
greet_user(user2)

print("End Task #3\n")

print("Start Task #4")

"""4.	Дан код. Исправить его в соответствии с принципом Single Responsibility."""

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class DatabaseManager:
    def save_to_database(self):
        pass


class EmailSender:
    def send_email(self, message):
        pass


class ActivityLogger:
    def log_activity(self, activity):
        pass


print("End Task #4\n")

print("Start Task #5")

"""5.	Дан код. Исправить его в соответствии с принципом Open/Closed. """


class Shape:
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2


rectangle = Rectangle(5, 4)
circle = Circle(3)

print(rectangle.calculate_area())  # прямоугольника
print(circle.calculate_area())  # круга

print("End Task #5\n")

print("Start Task #6")

"""6.	Дан код. Исправить его в соответствии с принципом Liskov Substitution. """


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class AreaCalculator:
    def calculate_area(self, shape):
        #подсмотрено
        return shape.area()



rectangle = Rectangle("Прямоугольник", 4, 6)
circle = Circle("Круг", 3)

calculator = AreaCalculator()
area1 = calculator.calculate_area(rectangle)
area2 = calculator.calculate_area(circle)

print(f"{rectangle.name} имеет площадь {area1}")
print(f"{circle.name} имеет площадь {area2}")

print("End Task #6\n")

print("Start Task #7")

"""7.	Дан код. Исправить его в соответствии с принципом Interface Segregation. """


class Eating:
    def eat(self):
        pass


class Working:
    def work(self):
        pass


class Managing:
    def manage(self):
        pass


class Worker(Working, Eating):
    def work(self):
        pass

    def eat(self):
        pass


class Manager(Managing):
    def manage(self):
        pass


class SuperWorker(Working, Eating, Managing):
    def work(self):
        pass

    def eat(self):
        pass

    def manage(self):
        pass


print("End Task #7\n")

print("Start Task #8")

"""8.	Дан код. Исправить его в соответствии с принципом Dependency Inversion."""

from abc import ABC, abstractmethod

class Switching(ABC):
    @abstractmethod
    def turn_on(self):
        pass


class LightBulb(Switching):
    def turn_on(self):
        print("Лампочка включена")


class Switch:
    def __init__(self, device):
        self.device = device

    def operate(self):
        self.device.turn_on()


bulb = LightBulb()
switch = Switch(bulb)
switch.operate()

print("End Task #8\n")