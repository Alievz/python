#Программа просит пользователя ввести любое положительное целое число, после чего показывает,
# какая цифра в числе является самой большой.


a = int(input("Введите любое целое положительное число: ")) #запрашиваем число и присваиваем его объекту a
m = a % 10 #отделим остаток от числа a и присвоим его объекту m
a = a // 10 #новое число a без остатка
while a > 0: #повторяющийся цикл, пока наше число a больше 0
    if a % 10 > m: #сравниваем остаток нового числа a с первоначальным остатком объекта m
        m = a % 10 #присваиваем новый наибольший остаток объекту m
    a = a // 10 #продолжаем деление на 10 и избавляемся от старого остатка. Как только a станет меньше 0,
                # остаток будет являться наибольшей цифрой в числе.
print(f"Самая большая цифра в числе это {m}") #выводим самую большую цифру в числе a.


