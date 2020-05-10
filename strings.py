#регистры
name = "ada lovelace"
print(name.title())     #method "title"...Метод представляет собой действие, которое Python выполняет с данными.
print(name.upper())
print(name.lower())

print("---")
#Конкатенация
first_name = "ada"
second_name = "lovelace"
full_name = first_name + " " + second_name
print(full_name)
print("Hello, " + full_name.title() + "!")
message = "Hello, " + full_name.title() + "!"
print(message)

print("---")
#пропуски
print("Python")         #табуляции
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")       #разрывы строк
print("Languages:\n\tPython\n\tC\n\tJavaScript")

print("---")
#удаление пропусков
favourite_language = " python "
print(favourite_language)
print(favourite_language.rstrip())                  #справа
favourite_language = favourite_language.rstrip()
print(favourite_language)
print(favourite_language.lstrip())                  #слева
print(favourite_language.strip())                   #с обеих сторон



print('Albert Einstein once said, "A person who never made a mistake never tried\nanything new."')
famous_person = "Albert Einstein"
message = famous_person + ' once said, "A person who never made a mistake never\ntried anything new."'
print(message)
