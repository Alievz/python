class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def process(self):
        mass = int(input("Введите массу асфальта в кг на 1 см: "))
        thickness = int(input("Введите толщину полотна в см: "))
        total = self._length * self._width * mass * thickness / 1000
        return total

start = Road(25, 30)
print(f"Чтобы покрыть всю дорогу нужно {start.process()} тонн асфальта")





