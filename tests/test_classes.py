from src.Rectangle import Rectangle
from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle

import pytest


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(4, 6, 24, 20),
                          (5, 10, 50, 30)])
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(-4, -6, 24, -20),
                          (0, 0, 0, 0),
                          ('a', 3, None, None,)])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter

@pytest.mark.parametrize(("side", "area", "perimeter"),
                         [(4, 8, 16),
                          (5, 10, 20)])
def test_square(side, area, perimeter):
    r = Square(side)
    assert r.name == f"Square {side}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter

@pytest.mark.parametrize(("side", "area", "perimeter"),
                         [(-4, -8, 16),
                          (0, 0, 0),
                          ('a', None, None)])
def test_square_negative(side, area, perimeter):
    r = Square(side)
    assert r.name == f"Square {side}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                             [(4, 4, 4, 6.93, 12), #проверка равностороннего треугольника
                              (3, 4, 5, 6, 12), #проверка тупоугольного треугольника
                              (66, 67, 68, 1942.93, 201), #проверка остроугольного треугольника
                              (3, 3, 5, 4.15, 11), #проверка равнобедренного треугольника
                              (3, 4, 5, 6, 12)]) #проверка прямоугольного треугольника

def test_triangle(side_a, side_b, side_c, area, perimeter):
    r = Triangle(side_a, side_b, side_c)
    assert r.name == f"Triangle {side_a} and {side_b} and {side_c}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                           [(-4, -4, -4, -6.93, -12),
                            (0, 0, 0, 0, 0),
                            (2, 3, 10, 0, 0)])
def test_triangle_negative(side_a, side_b, side_c, area, perimeter):
    r = Triangle(side_a, side_b, side_c)
    assert r.name == f"Triangle {side_a} and {side_b} and {side_c}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter

@pytest.mark.parametrize(("radius", "area", "perimeter"),
                             [(6, 113.1, 37.7)])
def test_circle(radius, area, perimeter):
    r = Circle(radius)
    assert r.name == f"Circle {radius}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter

@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(-6, -113.1, -37.7),
                         ('a', None, None)])
def test_circle_negative(radius, area, perimeter):
    r = Circle(radius)
    assert r.name == f"Circle {radius}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter

def test_add_area():
    r = Rectangle(2, 5)
    s = Square(5)
    assert r.add_area(s) == 20


def test_add_area_negative():
    r = Rectangle(2, 5)
    c = Circle(10)
    assert c.add_area(r) == 15
