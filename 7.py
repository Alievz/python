# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

def fact(n):
    count = 1
    while count <= n:
        yield count
        count += 1
i = 1
list = []
for el in fact(10):
    if i > 10:
        break
    else:
        list.append(el)
        i += 1
print(list)

