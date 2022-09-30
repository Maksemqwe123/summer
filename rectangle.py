class Rectangle:
    def __init__(self, width: int, length: int):
        self.width = width
        self.length = length

    def square(self):
        print(f'площадь прямоугольника АВСD {self.width * self.length} cm')

    def perimeter(self):
        print(f'периметр прямоугольника ABCD {(self.width + self.length) * 2} cm')


Rectangle_task = Rectangle(10, 5)
Rectangle_task.square()
Rectangle_task.perimeter()
