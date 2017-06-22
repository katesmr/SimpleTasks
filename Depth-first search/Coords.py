class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def clone(self):
        return Coords(self.x, self.y)

    def go_right(self):
        self.x += 1
        return self

    def go_left(self):
        self.x -= 1
        return self

    def go_up(self):
        self.y -= 1
        return self

    def go_down(self):
        self.y += 1
        return self
