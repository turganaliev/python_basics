#Обработка исключения ZeroDivisionError
try:
    print(5/0)
except ZeroDivisionError:
    print("\nYou can't divide by zero!")

print('---')
#Использование исключений для предотвращения аварийного завершения программы
#Блок else
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input('\nFirst number:')
    if first_number == 'q':
        break
    second_number = input('Second number:')
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

print('---')
#Обработка исключения FileNotFoundError
filename = 'alice_1.txt'
try:
     with open(filename) as f_obj:
         f_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + ' does not exist.'
    print(msg)

print('---')
#Анализ текста
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + ' does not exist.'
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print('The file ' + filename + ' has about ' + str(num_words) + ' words.')

print('---')
#Работа с несколькими файлами
def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = 'Sorry, the file ' + filename + ' does not exist.'
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' has about ' + str(num_words) + ' words.')

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

print('---')
#Ошибки без уведомления пользователя
def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass    # <-- Единственное отличие
    else:
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' has about ' + str(num_words) + ' words.')

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

print('---')
#Exercises
while True:
    first_number = input('Enter number:')
    if first_number == 'q':
        break
    second_number = input('Enter number:')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You can't add letters!")
    else:
        print(answer)

print('---')
first_number = input('Enter number:')
second_number = input('Enter number:')
try:
    answer = int(first_number) + int(second_number)
except  ValueError:
    print('Please enter an integer!')
else:
    print(answer)

print('---')
def read_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
        #print('The file ' + filename + ' does not exist.')
    else:
        print(contents.strip())
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    read_words(filename)

print('---')
filename = 'data_science.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    pass
else:
    the_n = contents.lower().count('the')
    print(the_n)
