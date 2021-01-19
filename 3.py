#  Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их
#  окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#  Выполнить подсчет средней величины дохода сотрудников.


with open("task_3.txt", 'r', encoding="utf-8") as f:
    salary = []
    low_income = []
    my_list = f.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           low_income.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20.000 {low_income}, средний оклад всех сотрудников {sum(map(int, salary)) / len(salary)}')

