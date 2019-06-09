# You are given an M by N matrix consisting of booleans that represents a board. Each True boolean 
# represents a wall. Each False boolean represents a tile you can walk on.
# Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps
# required to reach the end coordinate from the start. If there is no possible path, then return null.
# You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges
# of the board.
# For example, given the following board:
# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to
# reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on
# the second row.
#
# Algorith: BFS

f = False
t = True

def manhattan_heuristic(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def get_neighbours(matrix, start):
    neighbours = []
    for point in [(start[0] + 1, start[1]), (start[0] - 1, start[1]), (start[0], start[1] + 1), (start[0], start[1] - 1)]:
        x, y = point[0], point[1]
        if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]):
            if matrix[x][y] == f:
                neighbours.append(point)
    return neighbours

def min_steps_bfs(matrix, start, end):
    start_x, start_y = start
    end_x, end_y = end
    if matrix[start_x][start_y] or matrix[end_x][end_y] or start == end:
        return 0
    way = []
    queue = [(start, 0)]
    while len(queue) > 0:
        point, dist = queue.pop(0)
        if point == end:
            return dist
        if point not in way:
            way.append(point)
            for neighbour in get_neighbours(matrix, point):
                queue.append((neighbour, dist + 1))
    return 0

def min_steps_astar(matrix, start, end):
    start_x, start_y = start
    end_x, end_y = end
    if matrix[start_x][start_y] or matrix[end_x][end_y] or start == end:
        return 0
    way = []
    queue = [(start, 0, manhattan_heuristic(start, end))]
    while len(queue) > 0:
        point, dist, heuristic = queue.pop(0)
        if point == end:
            return dist
        if point not in way:
            way.append(point)
            for neighbour in get_neighbours(matrix, point):
                queue.append((neighbour, dist + 1, manhattan_heuristic(point, end)))
                queue.sort(key = lambda x: (x[1] + x[2]))
    return 0

def main():
    matrix = [[f, f, f, f], [t, t, f, t], [f, f, f, f], [f, f, f, f]]
    print("Minimum number of steps (bfs):", min_steps_bfs(matrix, (3, 0), (0, 0)))
    print("Minimum number of steps (a*):", min_steps_astar(matrix, (3, 0), (0, 0)))

if __name__ == "__main__":
    main()