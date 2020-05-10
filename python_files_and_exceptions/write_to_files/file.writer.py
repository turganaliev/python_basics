#Запись в пустой файл
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write('I love programming.')

#Многострочная запись
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write('I love programming.')
    file_object.write('\nI love creating games.')

#Присоединение данных к файлу
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write('\nI also love finding meaning in large datasets.')
    file_object.write('\nI like creating apps that can run in a browser.')

#Exercises
filename = 'your_name.txt'
name = input('Enter your name:')
with open(filename, 'w') as file_object:
     file_object.write(name.title())

print('---')
while True:
    name = input('Enter your name:')
    message = 'Hello, ' + name.title() + '!\n'
    if name == 'q':
        break
    filename = 'your_names_book.txt'
    with open(filename, 'a') as file_object:
        file_object.write(message)

print('---')
print('Why do you love programming?')
while True:
    answer = input('Enter your answer:')
    if answer == 'q':
        break
    filename = 'your_answer.txt'
    with open(filename, 'a') as file_object:
        file_object.write('\n' + answer)
