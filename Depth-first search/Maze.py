import random


class Maze:
    IDS = {
        "WALL": '#',
        "EMPTY": ' ',
        "PATH": '.',
    }

    def __init__(self, width, height, maze=None):
        self._width = width
        self._height = height
        if maze is None:
            self._cells = self.__create()
        else:
            self._cells = maze

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def generate(self):
        self._cells = self.__create()

    def draw(self):
        print('#' * (len(self._cells[0])*2 + 1))
        [print('#' + ' '.join(row) + '#') for row in self._cells]
        print('#' * (len(self._cells[0])*2 + 1))

    def at(self, pos):
        return self._cells[pos.y][pos.x]

    def put(self, pos, el):
        self._cells[pos.y][pos.x] = el

    def __create(self):
        return [[Maze.IDS[random.choice(("WALL", "EMPTY"))] for _ in range(self.height)] for _ in range(self.width)]
