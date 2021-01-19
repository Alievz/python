# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


translation = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []
result = []
with open("task_4.txt", 'r') as file_object:
    try:
        for line in file_object:
            tokens = line.split(" - ")
            print(tokens)
            if tokens[0] in translation:
                word = translation[tokens[0]]
                result.append(word +' - '+ tokens[1])
        print(result)
    except IOError:
        print("Произошла ошибка ввода-вывода!")

with open("task_4_output.txt", "w", encoding="utf-8") as file_object_2:
    try:
        file_object_2.writelines(result)
    except IOError:
        print("Произошла ошибка ввода-вывода!")
