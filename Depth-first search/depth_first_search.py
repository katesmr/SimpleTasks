from Way import Way
from Maze import Maze


def depth_first_search(maze, start, end):

    def _go_back_till_crossway():
        while len(crossway_path) != 0 and not crossway_path[-1].is_crossay():
            crossway_path.pop()
            maze.put(correct_path.pop(), EMPTY)

    if start == end:
        maze.put(start, Maze.IDS["PATH"])
        return

    if maze.at(start) is Maze.IDS["WALL"] or maze.at(end) is Maze.IDS["WALL"]:
        print("One of position inside WALL")
        return

    crossway_path = []
    correct_path = []
    width = maze.width
    height = maze.height
    current_position = start
    EMPTY = Maze.IDS["EMPTY"]

    maze.put(current_position, Maze.IDS["PATH"])

    while True:
        crossway = Way()
        r = current_position.clone().go_right()
        if r.x < width and maze.at(r) is EMPTY:  # go right
            crossway.add_coord(r)
        b = current_position.clone().go_down()
        if b.y < height and maze.at(b) is EMPTY:  # go down
            crossway.add_coord(b)
        l = current_position.clone().go_left()
        if l.x >= 0 and maze.at(l) is EMPTY:  # go left
            crossway.add_coord(l)
        t = current_position.clone().go_up()
        if t.y >= 0 and maze.at(t) is EMPTY:  # go up
            crossway.add_coord(t)

        if crossway.is_deadlock():
            _go_back_till_crossway()
            if len(correct_path):
                maze.put(correct_path.pop(), EMPTY)
            if len(crossway_path) == 0:  # can not find exit
                print("Can not find exit")
                break
        else:
            crossway_path.append(crossway)

        if crossway_path[-1].is_valid():
            current_position = crossway_path[-1].get_last_coord()
            correct_path.append(current_position)
            maze.put(current_position, maze.IDS["PATH"])
        else:
            _go_back_till_crossway()
            if len(crossway_path) == 0:  # can not find exit
                print("Can not find exit")
                break

        if current_position == end:
            print("Finish")
            break  # finish
