# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month_number = int(input("Введите цифру от 1 до 12, чтобы узнать сезон: "))
while month_number < 1 or month_number > 12:
    month_number = int(input("Ошибка! Введите цифру от 1 до 12, чтобы узнать сезон: "))
    continue
# реализация через лист
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if month_number in winter:
    print("Это зима!")
elif month_number in spring:
    print("Это весна!")
elif month_number in summer:
    print("Это лето!")
else:
    print("Это осень!")

# используем словарь :

month_number = int(input("Введите цифру от 1 до 12, чтобы узнать сезон: "))
while month_number < 1 or month_number > 12:
    month_number = int(input("Ошибка! Введите цифру от 1 до 12, чтобы узнать сезон: "))
    continue
calendar = {1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"}
if calendar.get(month_number) == "Dec" or "Jan" or "Feb":
    print("Это Зима!")
elif calendar.get(month_number) == "Mar" or "Apr" or "May":
    print("Это Весна!")
elif calendar.get(month_number) == "Jun" or "Jul" or "Aug":
    print("Это Лето!")
else:
    print("Это Осень!")

