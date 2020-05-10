#Функции json.dump() и json.load()
import json
numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

import json
filename = 'numbers.json'

with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

#Сохранение и чтение данных, сгенерированных пользователем
print('---')

import json
username = input("What's your name? ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + '!')

print('---')

import json
filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
print('Welcome back, ' + username + '!')

print('---')
#Теперь эти две программы необходимо объединить в один файл.

import json
filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + '!')
else:
    print('Welcome back, ' + username + '!')

#Рефакторинг
print('---')
#разбив его на функции, каждая из которых решает свою конкретную задачу.

import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input('What is your name? ')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username

def greet_user():
    username = get_stored_username()
    if username:
        print('Welcome back, ' + username + '!')
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + '!')

greet_user()

#Exercises
print('---')

import json
number = input('What is your best number? ')

filename = 'best_number.json'
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)

import json
filename = 'best_number.json'

with open(filename) as f_obj:
    content = json.load(f_obj)
    print('Let me think, I guess your best number is ' + content + '!')

print('---')

import json
filename = 'best_number.json'

try:
    with open(filename) as f_obj:
        content = json.load(f_obj)
except FileNotFoundError:
    number = input('What is your best number? ')
    filename = 'best_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
else:
    print('Let me think, I guess your best number is ' + content + '!')

print('---')

import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input('What is your name? ')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username

def greet_user():
    username = get_stored_username()
    if username:
        answer = input(username + ', is it you? (yes/no) ')
        if answer == 'yes':
            print('Welcome back, ' + username + '!')
        elif answer == 'no':
            username = get_new_username()
            print("We'll remember you when you come back, " + username + '!')
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + '!')

greet_user()
