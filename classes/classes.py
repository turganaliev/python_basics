#Создание класса
class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')

#Создание экземпляра класса
my_dog = Dog('willie', 6)
print("\nMy dog's name is " + my_dog.name.title() + '.')  #мы обращаемся к значению атрибута name экземпляра my_dog
print("My dog is " + str(my_dog.age) + ' years old.')
#Вызов методов
my_dog.sit()
my_dog.roll_over()

print('---')
#example 1
class Restaurant():

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(self.name.title())
        print(self.type.title())

    def open_restaurant(self):
        print(self.name.title() + ' is now open!')

restaurant = Restaurant('clot mone', 'french')
restaurant_1 = Restaurant('faiza', 'eastern')
restaurant_2 = Restaurant('lukum', 'arabic')
restaurant_3 = Restaurant('barashek', 'asian')
print("Our restaurant's name is " + restaurant.name.title() + '.')
print(restaurant.name.title() + "'s cuisine type is " + restaurant.type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

print('---')

class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name.title() + ' ' + self.last_name.title() +
            ', welcome to the world of programming!')

    def greet_user(self):
        print("Hello, " + self.first_name.title() + '!')

user_1 = User('jack', 'lee')
user_1.describe_user()
user_1.greet_user()

print('---')
#Работа с классами и экземплярами
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
my_new_car = Car('audi', 'a4', 2020)
print(my_new_car.get_descriptive_name())

print('---')
#Назначение атрибуту значения по умолчанию
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print('---')
#Прямое изменение значения атрибута
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23   #<-- changes
my_new_car.read_odometer()

print('---')
#Изменение значения атрибута с использованием метода
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):     #<-- changes
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
my_new_car = Car('audi', 'a4', 2017)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

print('---')
#Изменение значения атрибута с приращением
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
my_used_car = Car('subaru', 'forester', 2010)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

print('---')
class Restaurant():

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name.title())
        print(self.type.title())

    def show_served(self):
        print('This restaurant has served ' + str(self.number_served) + ' people on it!')

    def update_served(self, new_guest):
        if new_guest >= self.number_served:
            self.number_served = new_guest
        else:
            print("You can't roll back served guests!")

    def increment_served(self, served_guest):
        self.number_served += served_guest

restaurant = Restaurant('mishlen', 'french')
restaurant.describe_restaurant()
#restaurant.number_served = 4
restaurant.update_served(4)
restaurant.show_served()

restaurant.increment_served(1)
restaurant.show_served()

print('---')
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name.title()
    def show_login_attempts(self):
        print(self.login_attempts)
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
user_first = User('mia', 'alessia')
print(user_first.describe_user())
user_first.increment_login_attempts()
#user_first.increment_login_attempts()
#user_first.increment_login_attempts()
user_first.show_login_attempts()
user_first.reset_login_attempts()
user_first.show_login_attempts()

print('---')
#Наследование
#Метод __init__() класса-потомка
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it!')
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())

print('---')
#Определение атрибутов и методов класса-потомка
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it!')
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

print('---')
#Экземпляры как атрибуты
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it!')
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print('---')
class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def describe_restaurant(self):
        titled = self.name + '\n' + self.type
        return titled.title()

class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['first', 'second', 'third']
    def show_flavors(self):
        print(self.flavors)
my_cream = IceCreamStand('eskimo', 'holodok')
print(my_cream.describe_restaurant())
my_cream.show_flavors()

print('---')
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name.title()

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['allowed to add messages', 'allowed to delete users',
                            'allowed to ban users', 'etc.']
    def show_privileges(self):
        print(self.privileges)
admin = Admin('adam', 'hendrix')
print(admin.describe_user())
admin.show_privileges()

print('---')
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name.title()

class Privileges():
    def __init__(self, privileges_list=['allowed to add messages', 'allowed to delete users',
                                            'allowed to ban users', 'etc.']):
        self.privileges_list = privileges_list
    def show_privileges(self):
        print(self.privileges_list)

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
admin = Admin('leo', 'fuiry')
print(admin.describe_user())
admin.privileges.show_privileges()

print('---')
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it!')
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')
    def get_range(self):
        if self.battery_size <= 70:
            range = 240
        elif self.battery_size <= 85:
            range = 270
        elif self.battery_size > 85:
            range = 300

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        #if self.battery_size != 70:
        self.battery_size == 85

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

print('---')
#Импортирование классов
#Импортирование одного класса
from car import Car
my_new_car = Car('mercedes', 'gt-63', 2020)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print('---')
#Хранение нескольких классов в модуле
from car import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2010)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print('---')
#Импортирование нескольких классов из модуля
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model roadster', 2020)
print(my_tesla.get_descriptive_name())

print('---')
#Импортирование всего модуля
import car

my_beetle = car.Car('volkswagen', 'beetle', 2018)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadstar', 2020)
print(my_tesla.get_descriptive_name())

#Импортирование всех классов из модуля
from car import *

print('---')
from restaurant import Restaurant
restaurant = Restaurant('faiza', 'eastern')
print(restaurant.describe_restaurant())

print('---')
from restaurant import IceCreamStand
my_cream = IceCreamStand('eskimo', 'sever')
print(my_cream.describe_restaurant())
my_cream.show_flavors()

print('---')
from restaurant import Restaurant, IceCreamStand
restaurant = Restaurant('faiza', 'eastern')
print(restaurant.describe_restaurant())
my_cream = IceCreamStand('eskimo', 'sever')
print(my_cream.describe_restaurant())

print('---')
import restaurant
restaurant = Restaurant('faiza', 'eastern')
print(restaurant.describe_restaurant())
my_cream = IceCreamStand('eskimo', 'sever')
print(my_cream.describe_restaurant())

print('---')
#Стандартная библиотека Python
from collections import OrderedDict
favourite_languages = OrderedDict()
favourite_languages['jen'] = 'python'
favourite_languages['sarah'] = 'c'
favourite_languages['edward'] = 'ruby'
favourite_languages['phil'] = 'python'
for name,language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + '.')
#Это чрезвычайно полезный класс, объединяющий основное преимущество списков
#(сохранение исходного порядка) с главной особенностью словарей (связывание
#двух видов информации).

print('---')
from random import randint
x = randint(1,6)
print(x)

print('---')
class Die():
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        x = randint(1, self.sides)
        return x
z = Die(8)
print(z.roll_die())
