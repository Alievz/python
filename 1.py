'''
Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
'''


def div(*args):

    try:
        arg1 = int(input("Введите целое делимое число "))
        arg2 = int(input("Введите целый делитель "))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка, число должно быть целым'
    except ZeroDivisionError:
        return "Ошибка! Делить на 0 нельзя!"

    return res

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Ошибка! Делить на 0 нельзя!")
    '''


print(f'result  {div()}')

