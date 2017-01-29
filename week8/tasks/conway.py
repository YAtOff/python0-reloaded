def alive_cell_neighbours(x, y, board):
    """
    Намира броя живи съседни клетки на дадената.
    Напр. за да вземете състоянието на клетката отгоре,
    използвайте board[x - 1, y]

    (x - 1, y - 1) | (x - 1, y) | (x - 1, y + 1)
    --------------------------------------------
    (x, y - 1)     | (x, y)     | (x, y + 1)
    --------------------------------------------
    (x + 1, y - 1) | (x + 1, y) | (x + 1, y + 1)
    """
    count = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            count += board[x + i][y + j]
    return count - board[x][y]


def next_cell_state(x, y, board):
    """
    Намира състоянието на клетката (0 или 1) през следващото поколение
    Текущото състояние на клетката е board[x][y]
    Изплзвайте функцията alive_cell_neighbours за да изчислите броя
    живи съседни клетки, и чрез тази стойност да определите дали клетката
    ще е жива или мъртва.
    """
    alive_neigbours = alive_cell_neighbours(x, y, board)
    current = board[x][y]
    if current == 0:
        if alive_neigbours == 3:
            return 1
        else:
            return 0
    else:
        if 2 <= alive_neigbours <= 3:
            return current
        else:
            return 0


if __name__ == '__main__':
    board = [
        [0,0,0,0,0,0,0],
        [0,0,1,1,0,0,0],
        [0,0,1,1,0,0,0],
        [0,0,0,0,1,1,0],
        [0,0,0,0,1,1,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]

    print(alive_cell_neighbours(1, 1, board))  # 2
    print(next_cell_state(1, 1, board))  # 0
    print(alive_cell_neighbours(1, 2, board))  # 3
    print(next_cell_state(1, 2, board))  # 1
    print(alive_cell_neighbours(2, 3, board))  # 4
    print(next_cell_state(2, 3, board))  # 0
