# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def summation():
    try:
        with open('task_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()
            print("Сумма чисел:", sum(map(int, my_numb)))
    except IOError:
        print('Ошибка внутри файла!')
    except ValueError:
        print('Ошибка ввода-вывода!')
summation()

