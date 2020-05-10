bicycles = ['trek', 'connandale', 'bandbx', 'ural']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

print('---')
#изменение элементов в списке
automobiles = ['bmw', 'mercedes-benz', 'nissan']
print(automobiles)
automobiles[0] = 'bugatti'
print(automobiles)

print('---')
#присоединение элементов в конец списка
automobiles = ['bmw', 'mercedes-benz', 'nissan']
automobiles.append('bugatti')
print(automobiles)
automobiles = []
automobiles.append('bmw')
automobiles.append('nissan')
automobiles.append('mercedes')
print(automobiles)

print('---')
#вставка элементов в список
letters = ['a', 'b', 'c']
letters.insert(0, 'd')
print(letters)

print('---')
#удаление элемента с использованием команды del
family = ['asan', 'uson', 'akylai']
del family[1]    #значение, удаленное из списка после использования команды del, становится недоступным.
print(family)

print('---')
#удаление элемента с использованием метода pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)         #метод pop() удаляет последний элемент из списка, но позволяет работать с ним после удаления.
print(popped_motorcycle)

print('---')
#извлечение элементов из произвольной позиции списка
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)           #вызов pop() может использоваться для удаления элемента в произвольной позиции списка.
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

print('---')
#удаление элементов по значению
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)     # Иногда позиция удаляемого элемента неизвестна. Если вы знаете только значение элемента, используйте метод remove().
motorcycles.remove('ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')

print('---')
#постоянная сортировка списка методом sort()
cars = ['bmw', 'toyota', 'subaru', 'audi']
cars.sort()
print(cars)      #в алфавитном порядке
cars = ['bmw', 'toyota', 'subaru', 'audi']
cars.sort(reverse=True)
print(cars)      #в обратном алфавитном порядке

print('---')
#временная сортировка списка функцией sorted()
cars = ['bmw', 'toyota', 'subaru', 'audi']
print(sorted(cars))
print(cars)

print('---')
#вывод списка в обратном порядке
cars = ['bmw', 'toyota', 'subaru', 'audi']
print(cars)
cars.reverse()
print(cars)

print('---')
#определение длины списка
cars = ['bmw', 'toyota', 'subaru', 'audi']
print(len(cars))

print('---')
#перебор всего списка
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(magician.title() + ",that was a great trick!\n")
print("Thank you everyone.That was a great magic show!")

print('---')
#функция range()
for value in range(1,5):
    print(value)

print('---')
#использование range() для создания числового списка
numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,2))  #В этом примере функция range() начинает со значения 2, а затем увеличивает его на 2.
print(even_numbers)
squares = []
for value in range(1,11):       #список квадратов всех целых чисел от 1 до 10
    square = value**2
    squares.append(square)
print(squares)

print('---')
#простая статистика с числовыми списками
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

print('---')
#генераторы списков
squares = [value**2 for value in range(1,11)]      #всего в одной строке.
print(squares)
even_numbers = [value for value in range(2,11,2)]
print(even_numbers)

million = list(range(1,1000001))
print(sum(million))
print(max(million))
print(min(million))

odd_numbers = list(range(1,11,2))
print(odd_numbers)

cubed_numbers = [value**3 for value in range(3,13)]
print(cubed_numbers)

print('---')
#Создание среза
players = ['first', 'second', 'third', 'fourth', 'fifth']
print(players[0:3])    #останавливается на элементе, предшествующем второму индексу.
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[:-3])

print('---')
#Копирование списка
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake']
print('My favourite foods are: ')
for x in my_foods:
    print('-> ' + x)

print('---')
#Кортежи
dimensions = (200, 50)
print(dimensions[0])    #Кортеж выглядит как список, не считая того, что вместо квадратных скобок используются круглые скобки.
print(dimensions[1])    #неизменяемый список называется 'кортежем'.

for dimension in dimensions:
    print(dimension)          #Перебор всех значений в кортеже
