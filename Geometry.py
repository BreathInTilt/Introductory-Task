from math import sqrt, isclose, pi
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius < 0:
            raise ValueError("Radius cannot be negative")
        return pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        # Проверяем, что стороны положительны
        if self.side_a <= 0 or self.side_b <= 0 or self.side_c <= 0:
            raise ValueError("Sides must be positive")

        # Проверяем, что треугольник может существовать
        if (self.side_a + self.side_b <= self.side_c) or \
                (self.side_a + self.side_c <= self.side_b) or \
                (self.side_b + self.side_c <= self.side_a):
            raise ValueError("Triangle with given sides cannot exist")

        s = (self.side_a + self.side_b + self.side_c) / 2
        return sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def is_right_angled(self):
        sides = sorted([self.side_a, self.side_b, self.side_c])
        return isclose(sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2)


def compute_area(shape):
    return shape.area()


# Пример использования:
circle = Circle(5)
triangle = Triangle(3, 4, 5)
print(f"Circle Area: {compute_area(circle)}")
print(f"Triangle Area: {compute_area(triangle)}")
print(f"Triangle is right-angled: {triangle.is_right_angled()}")
