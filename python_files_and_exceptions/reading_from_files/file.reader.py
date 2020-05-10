#Чтение всего файла
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

print('---')
#Чтение по строкам
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print('---')
#Создание списка строк по содержимому файла
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

print('---')
#Работа с содержимым файла
filename = 'pi_30_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

print('---')
#Большие файлы: миллион цифр
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52] + '...')
print(len(pi_string))

print('---')
#Проверка дня рождения
filename = 'pi_thousand_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
birthday = input('Enter your birthday, in the form mmddyy: ')
if birthday in pi_string:
    print('Your birthday appears in the first thousand digits of pi!')
else:
    print('Your birthday does not appear in the first thousand digits of pi.')

print('---')
with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents)

print('---')
contents = 'learning_python.txt'
with open(contents) as file_object:
    for line in file_object:
        print(line.rstrip())

print('---')
contents = 'learning_python.txt'
with open(contents) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

print('---')
contents = 'learning_python.txt'
with open(contents) as file_object:
    lines = file_object.readlines()
message = ''
for line in lines:
    message += line.rstrip()
    message.replace('Python', 'C')
print(message)
