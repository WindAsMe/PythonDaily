def judge(i):
    if not isinstance(i, tuple):
        raise TypeError


class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def size(self):
        return self._length, self._width

    @size.setter
    def length(self, value):
        self._length = value

    @size.setter
    def width(self, value):
        self._width = value


if __name__ == '__main__':
    r = Rectangle(1, 2)
    r.length = 4
    r.width = 11
    print(r.size)
