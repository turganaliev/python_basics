current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1    #Оператор += является сокращенной формой записи для
                                        #current_number = current_number + 1

print('---')
#Пользователь решает прервать работу программы
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = " "
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

print('---')        #Если программа должна выполняться только при истинности
#Флаг                       нескольких условий,определите одну переменную - флаг
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

print('---')
#break
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + '!')

print('---')
#continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

print('---')
#Предотвращение зацикливания
x = 1
while x <= 5:
    x += 1
    print(x)      #если случайно пропустить строку x += 1,цикл будет выполняться бесконечно.

print('---')
#Использование цикла while со списками и словарями
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)

print('\nThe following users have been confirmed: ')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
#Использование циклов while со списками и словарями позволяет собирать,
#хранить и упорядочивать большие объемы данных для последующего анализа
#и обработки.

print('---')
#Удаление всех вхождений конкретного значения из списка
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

print('---')
#Заполнение словаря данными, введенными пользователем
responses = {}
polling_active = True

while polling_active:
    name = input('\nWhat is your name? ')
    response = input('What mountain would you like to climb someday? ')
    responses[name] = response
    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        polling_active = False
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(name + ', would you like to climb ' + response + '.')     #При каждом проходе цикла while ваша программа может
                                                                           #запрашивать любое необходимое количество данных.

#split
pizza = [
    'first_item', 'second_item', 'third_item',
    'fourth_item', 'fifth_item', 'sixth_item',
    'seventh_item', 'and last_item'
]
enumerations = []

for item in pizza:
    new_item = item.split('_')[0]
    if new_item.startswith('s'):
        continue
    elif new_item.startswith('a'):
        break
    enumerations.append(new_item.title())

print(enumerations)

#enumerate() function
for index, item in enumerate(pizza):
    print(f'This is index {index}, and item ---{item}')
    new_item = item.split('_')[0]
    enumerations.append(new_item.title())
print(enumerations)

#dir function and dander method __next__()
str_ = 'hello'
print(dir(str_))
i = str_.__iter__()
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
