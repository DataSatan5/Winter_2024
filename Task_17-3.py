class Shape:
    def __init__(self, colour, square):
        self.colour = colour
        self.square = square

    def colour_def(self, colour):
        self.colour = colour

    def square_def(self, square):
        self.square = square

    def colour_get(self):
        print(self.colour)

    def square_get(self):
        print(self.square)


#sample = Shape('Purple', 121)
sample = Shape(input('Введи цвет фигуры: '),
                     int(input('Введи площадь фигуры: ')))

sample.colour_get()
sample.square_get()
sample.colour_def('yellow')
sample.colour_get()
sample.square_def(144)
sample.square_get()