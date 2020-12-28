# Для списка реализовать обмен значений соседних элементов
# Считаем длину списка и задаем объект с позицией 0 в списке
# Создаем два цикла в зависимости от того, какая длина списка (четная или нечетная)
# Меняем элементы местами
# Цикл действителен для каждой следующей пары
# Выводим список на экран

bio = ["Зелимхан", "Алиев", 25, 5.77, "студент GeekBrains"] # произвольный список, можно дописать, что угодно
list_items = len(bio)
position_number = 0
if list_items % 2 == 0:
    while position_number < list_items:
        bio[position_number], bio[position_number + 1] = bio[position_number + 1], bio[position_number]
        position_number += 2
        continue
else:
    while position_number + 1 < list_items:
        bio[position_number], bio[position_number + 1] = bio[position_number + 1], bio[position_number]
        position_number += 2
        continue
print(bio)

