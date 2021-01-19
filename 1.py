# Создать программно файл в текстовом формате, записать
# в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_f = open('task_1.txt', 'w', encoding="utf-8")
line = input('Введите текст: ')
while line:
    new_line = line + "\n"
    my_f.writelines(new_line)
    line = input('Введите текст: ')
    if not line:
        break

my_f.close()
my_f = open('task_1.txt', 'r', encoding="utf-8")
content = my_f.readlines()
print(content)
my_f.close()

