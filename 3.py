class Worker:
    def __init__(
            self,
            name: str,
            surname: str,
            position: str,
            wage: float = 0,
            bonus: float = 0
    ):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self, reverse=False):
        return ' '.join(sorted([self.name, self.surname], reverse=reverse))

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    position_data = [
        {
            'name': 'Вася',
            'surname': 'Пупкин',
            'position': 'Хороший парень',
            'wage':  150000,
            'bonus': 0
        },
        {
            'name': 'Дональд',
            'surname': 'Трамп',
            'position': 'Плохой парень',
            'wage':  90000,
            'bonus': 60000
        },
    ]

    for item in position_data:
        position = Position(**item)

        print('--' * 50)
        print('Полный профайл: ', item)
        print('Имя: ', position.name)
        print('Фамилия: ', position.surname)
        print('Должность: ', position.position)
        print('Оклад: ', position.get_total_income())

