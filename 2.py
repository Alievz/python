# Задание два




class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Нельзя делить на ноль!!!!")


div = DivisionByNull(5, 8)
print(DivisionByNull.divide_by_null(5, 0))
print(DivisionByNull.divide_by_null(5, 0.1))
print(div.divide_by_null(8, 0))