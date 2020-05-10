#Простой словарь
alien_0 = {'color': 'green', 'points': 5}    #«ключ—значение».
print(alien_0['color'])  #Значением может быть число, строка,список и даже другой словарь.
print(alien_0['points'])

print('---')
#Добавление новых пар «ключ—значение»
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print('---')
#Создание пустого словаря
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print('---')
#Изменение значений в словаре
alien_0['color'] = 'yellow'
print(alien_0)

print('---')
#более интересный пример:
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}   #change 'medium' to 'fast' or 'slow',and it will change whole operation.
print('Original x-position: ' + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x-position: ' + str(alien_0['x_position']))

print('---')
#Удаление пар «ключ—значение»
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)          #Учтите, что удаление пары «ключ—значение» отменить уже не удастся.

print('---')
#Перебор всех пар «ключ—значение»
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key,value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

print('---')
#Перебор всех ключей в словаре
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in favorite_languages.keys():
    print(name.title())

print('---')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(' Hi ' + name.title() +
            ', I see your favourite language is ' +
            favorite_languages[name].title() + '!')

print('---')
#Упорядоченный перебор ключей словаря
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for taking the poll.')

print('---')
#Перебор всех значений в словаре
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print('The following languages have been mentioned: ')
for language in set(favorite_languages.values()):
    print('\t' + language.title())
#Чтобы получить список выбранных языков без повторений, можно
#воспользоваться множеством (set).Множество в целом похоже на список,
#но все его элементы должны быть уникальными:

print('---')
Rivers = {'nile':'egypt', 'semirechye':'asia', 'amazonka':'brazil'}
for key,value in Rivers.items():
    print('The ' + key.title() + ' runs through ' + value.title())
    print(key.title())
    print(value.title())

print('---')
voters = {
        'adam': 'python', 'brown': 'c#', 'cabello': 'ruby',
        'dmitriy': 'java', 'eilish': 'javascript'
        }
voted = ['adam', 'dmitriy', 'eilish']
for voter, language in voters.items():
    if voter in voted:
        print(voter.title() + ', thank you for voting' + ' and choosing ' + language.title() + '!')
    else:
        print(voter.title() + ', do you want to vote?')

#Вложение
print('---')
#Список словарей
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

print('---')
aliens = []
for alien_number in range(10):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    print(alien)

print('---')
aliens = []
for alien_number in range(0,10):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[0:5]:
    print(alien)

print('---')
#Список в словаре
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print('\n' + name.title() + "'s favourite_languages are: ")
    for language in languages:
        print('\t' + language.title())

print('---')
#Словарь в словаре
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print('Username: ' + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print('\tFullname: ' + full_name.title())
    print('\tLocation: ' + location.title())
