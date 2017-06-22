class Way:
    def __init__(self, *args):
        self._list = list(args)
        self._pointer = len(self._list) - 1

    def is_crossay(self):
        return len(self._list) > 1 and self.is_valid()

    def get_last_coord(self):
        pos = self._list[self._pointer]
        self._pointer -= 1
        return pos

    def is_deadlock(self):
        return len(self._list) == 0

    def add_coord(self, pos):
        self._pointer += 1
        self._list.append(pos)

    def is_valid(self):
        return self._pointer != -1
