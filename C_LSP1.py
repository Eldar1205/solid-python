from typing import final


class Rectangle:
    def __init__(self) -> None:
        self._height = 0
        self._width = 0

    def get_height(self) -> int:
        return self._height

    def set_height(self, height: int) -> None:
        self._height = height

    def get_width(self) -> int:
        return self._width

    def set_width(self, width: int) -> None:
        self._width = width

    @final
    def calc_area(self) -> int:
        return self._height * self._width

class Square(Rectangle):
    def set_height(self, height: int) -> None:
        super().set_height(height)
        super().set_width(height)

    def set_width(self, width: int) -> None:
        super().set_height(width)
        super().set_width(width)

class RectangleTests:
    def test_rectangle(self) -> None:
        self.__inner_test_rectangle(Rectangle())
    
    def test_square(self) -> None:
        self.__inner_test_rectangle(Square())

    def __inner_test_rectangle(self, rectangle: Rectangle) -> None:
        rectangle.set_height(3)
        rectangle.set_width(6)
        area = rectangle.calc_area()

        assert area == 18 # Fails for Square