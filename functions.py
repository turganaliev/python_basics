#простая функция greet_user()
def greet_user():
    print('Hello!')
greet_user()

print('---')
#Передача информации функции
def greet_user(username):                       #Переменная username — параметр
    print('Hello, ' + username.title() + '!')
greet_user('marella')                           #Значение 'marella' — аргумент


#--- Передача аргументов
#Определение функции может иметь несколько параметров, и может оказаться, что
#при вызове функции должны передаваться несколько аргументов. Существуют
#несколько способов передачи аргументов функциям.

print('---')
#Позиционные аргументы
def describe_pet(animal_type, pet_name):
    print('I have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
describe_pet('hamster', 'harry') #Позиционные аргументы перечисляются в порядке, точно соответствующем порядку записи параметров.
describe_pet('dog', 'grisha')  #Функция может вызываться в программе столько раз, сколько потребуется.

print('---')
#Именованные аргументы
def describe_pet(animal_type, pet_name):
    print('I have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
describe_pet(animal_type = 'hamster', pet_name = 'harry')
describe_pet(pet_name = 'harry', animal_type = 'hamster')  #Порядок следования именованных аргументов в данном случае не важен, потому
                                                                             #что Python знает, где должно храниться каждое значение.

print('---')
#Значения по умолчанию
def describe_pet(pet_name, animal_type = 'dog'):   #теперь функция будет вызвана без указания animal_type, Python знает,
        print('I have a ' + animal_type + '.')         #что для этого параметра следует использовать значение 'dog
        print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
describe_pet(pet_name = 'willie')
describe_pet('willie')
describe_pet('willie', 'hamster')  #<-- Эквивалентные вызовы функций
#Если вы используете значения по умолчанию, все параметры со значением по умолчанию должны
#следовать после параметров, у которых значений по умолчанию нет. Это необходимо для того,
#чтобы Python правильно интерпретировал позиционные аргументы.

print('---')
#Возвращаемое значение
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()     #Команда return передает значение из функции в строку, в которой эта функция была вызвана.
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, last_name):
    print(first_name.title() + ' ' + last_name.title())
get_formatted_name('jimi', 'hendrix')

print('---')
#Необязательные аргументы
def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')      #Обновленная версия этой функции подойдет как для людей, у которых задается
print(musician)                                                #только имя и фамилия, так и для людей со вторым именем.
get_formatted_name('bruce', 'lee')

print('---')
#Возвращение словаря
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age = ''):
        person = {'first': first_name, 'last': last_name}
        if age:
            person['age'] = age
        return person
musician = build_person('jimi', 'hendrix', age = 27)
print(musician)

print('---')
#Использование функции в цикле while
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print('\nPlease enter your name:')
    print("(enter 'q' at any time to quit)")

    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print('\nHello, ' + formatted_name + '!')             #Функции могут использоваться со всеми структурами Python, уже известными вам.

print('---')
#Передача списка
def greet_users(names):
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

print('---')
#Изменение списка в функции
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print('---')
#Запрет изменения списка в функции
#Если удаление элементов из списка unprinted_designs в print_models.py нежелательно,
#функцию print_models() можно вызвать так:
print_models(unprinted_designs[:], completed_models)

print('---')
#Передача произвольного набора аргументов
def make_pizza(*toppings):          #Звездочка в имени параметра *toppings приказывает Python
    print("\nMaking a pizza with the following toppings:")   #создать пустой кортеж с именем toppings и упаковать в него все полученные значения.
    for topping in toppings:
        print('- ' + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

print('---')
#Позиционные аргументы с произвольными наборами аргументов
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print('- ' + topping)
make_pizza(12, 'pepperoni')
make_pizza(21, 'mushrooms', 'green peppers', 'extra cheese')

print('---')
#Использование произвольного набора именованных аргументов
def build_profile(first, last, **user_info):   #Две звездочки перед параметром **user_info заставляют Python создать пустой словарь с име-
    profile = {}                                                  #нем user_info и упаковать в него все полученные пары «имя—значение».
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location = 'princeton',
                             field = 'physics')
print(user_profile)

print('---')
#*args (кортеж)
def func(*args):
    return args

print(func(1, 2, 3, 'abc'))
print(func(1))
print(func())

#*kwargs (кортеж)
def func(**kwargs):
    return kwargs

print(func(a=1, b=2, c=3))
print(func(a = 'Python'))
print(func())

print('---')
#инструкция lambda
func = lambda x, y: x + y
print(func(1, 2))
print(func('a', 'b'))
print((lambda x, y: x + y)(1, 2))
print((lambda x, y: x + y)('a', 'b'))

func = lambda *args: args
print(func(1, 2, 3, 4))

print('---')
#function locals()
def some_func():
    print(locals())
some_func()

def some_func(name):
    print(locals())
some_func('Python')

def get_information():
    name = 'John'
    age = 18
    print(locals())
get_information()

print('---')
#function map()
items = [1, 2, 3, 4, 5]                          #itmes = [1,2,3,4,5]
squared = list(map(lambda x: x**2, items))       #squared = []
print(squared)                                   #for i in items:
                                                 #  squared.append(i**2)
                                                 #print(squared)

print('---')
#function filter()
num_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, num_list))
print(less_than_zero)

print('---')
#function reduce()
from functools import reduce
product = reduce((lambda x, y: x * y), range(1, 5))
print(product)
