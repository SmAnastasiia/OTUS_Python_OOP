from src.Figure import Figure

class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        if type(side_a) == int and side_a <= 0 or type(side_b) == int and side_b <= 0:
            raise ValueError("Can't create Rectangle")
        if not isinstance(side_a, (int, float)):
            raise ValueError("Side must be a number")
        if not isinstance(side_b, (int, float)):
            raise ValueError("Side must be a number")
        self.side_a = side_a
        self.side_b = side_b
        self.name = f"Rectangle {side_a} and {side_b}"

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)
