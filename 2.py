# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


FILENAME = "task_2.txt"

try:
    with open(FILENAME, 'r', encoding="utf-8") as f:
        lines = [line for line in f.readlines() if line != '\n']
except IOError as e:
    print(e)
    sys.exit(1)

print(f"В это файле столько строк: {len(lines)}")

for line in lines:
    print(f'Строка {line[:50]}... содержит столько слов: {len(line.split())}')



















