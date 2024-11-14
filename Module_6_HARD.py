import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = self.__validate_color(color)
        self.__sides = self.__validate_sides(*sides) or [1] * self.sides_count
        self.filled = False


    @staticmethod
    def __is_valid_color(r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    def __validate_color(self, color):
        if len(color) == 3 and self.__is_valid_color(*color):
            return list(color)
        return [0, 0, 0]

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    @staticmethod
    def __is_valid_sides(sides_count, *sides):
        return (
            len(sides) == sides_count
            and all(isinstance(side, int) and side > 0 for side in sides)
        )

    def __validate_sides(self, *sides):
        if self.__is_valid_sides(self.sides_count, *sides):
            return list(sides)
        return None

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        validated_sides = self.__validate_sides(*new_sides)
        if validated_sides:
            self.__sides = validated_sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius**2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = len(self) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = sides * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        edge = self.get_sides()[0]
        return edge**3



circle1 = Circle((200, 200, 100), 10)

cube1 = Cube((222, 35, 130), 6)


circle1.set_color(55, 66, 77)

print(circle1.get_color())  # [55, 66, 77]

cube1.set_color(300, 70, 15)

print(cube1.get_color())  # [222, 35, 130]


cube1.set_sides(5, 3, 12, 4, 5)

print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

circle1.set_sides(15)

print(circle1.get_sides())


print(len(circle1))


print(cube1.get_volume())