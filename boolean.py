#Простой пример
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print('---')
#Проверка неравенства
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':      #Восклицательный знак представляет отрицание
    print('Hold the anchovies!')

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

print('---')
#Использование and и or для проверки нескольких условий
age_0 = 2
age_1 = 4
if age_0 >= 3 and age_1 >= 3:
    print('True')
else:
    print('False')

if age_0 >= 1 and age_1 >= 1:
    print('True')
else:
    print('False')

if age_0 >= 5 or age_1 >= 5:
    print('True')
else:
    print('False')

if age_0 >= 3 or age_1 >= 3:
    print('True')
else:
    print('False')

print('---')
#Проверка вхождения и отсутствия значения в списке
requested_toppings = ['mushrooms', 'onions', 'pineapple']   #вхождения
if 'mushrooms' in requested_toppings:
    print('True')
else:
    print('False')

if 'pepperoni' in requested_toppings:
    print('True')
else:
    print('False')

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ', you can post a response if you wish.')
print('---')
#Блок команды if может содержать сколько угодно строк.
age = 19
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')

print('---')
#Цепочки if-elif-else
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print('Your admission cost is $' + str(price) + '.')

print('---')
#Серии блоков elif
age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print('Your admission cost is $' + str(price) + '.')

print('---')
#Отсутствие блока else
age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print('Your admission cost is $' + str(price) + '.')

#Блок else «универсален»: он обрабатывает все условия, не подходящие ни под одну
#конкретную проверку if или elif, причем в эту категорию иногда могут попасть
#недействительные или даже вредоносные данные. Если у вас имеется завершающее
#конкретное условие, лучше используйте завершающий блок elif и опустите блок
#else. В этом случае вы можете быть уверены в том, что ваш код будет выполняться
#только в правильных условиях.

print('---')
#Проверка нескольких условий
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')
print('\nFinished making your pizza!')       #Такое решение уместно, когда истинными могут быть сразу несколько
                                             #условий и вы хотите отреагировать на все истинные условия.

print('---')
#Проверка специальных значений
requested_toppings = ['mushrooms', 'green pepper', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green pepper':
        print('Sorry, we are out of green pepper right now.')
    else:
        print('Adding ' + requested_topping + '.')
print('\nFinished making your pizza!')

print('---')
#Проверка наличия элементов в списке
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')
        print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')       #Когда имя списка используется в условии if, Python возвращает True,
                                                        #если список содержит хотя бы один элемент; если список пуст, возвращается значение False.

print('---')
#Множественные списки
available_toppings = [
'mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese'
]
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print('Sorry, we do not have ' + requested_topping + '.')
print('\nFinished making your pizza!')

print('---')
#example for ^ : Проверка имен пользователей
current_users = ['jack', 'brown', 'billie', 'steward']
new_users = ['adam', 'JACK', 'Brown', 'biLLie', 'steward', 'Anna']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('Sorry, please choose another name!')
    else:
        print('Your name choosen!')
