# Depth-first search

Is an algorithm for searching tree or graph data structures, based on data (begin coord and finish coord).

# Usage
```
from Coords import Coords
from Maze import Maze
from depth_first_search import depth_first_search

maze = Maze(10, 10, [
    [' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' '],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    [' ', ' ', '#', '#', '#', '#', '#', '#', ' ', ' '],
    [' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' '],
    [' ', '#', '#', ' ', '#', '#', ' ', ' ', ' ', ' '],
    [' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#'],
    [' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' '],
    ['#', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' '],
    [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' '],
    [' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' '],
])
begin = Coords(5, 6)
end = Coords(9, 0)
depth_first_search(maze, begin, end)

maze.draw()
```
