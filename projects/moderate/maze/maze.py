import time
import math
from random import shuffle, randrange
import turtle
import functools


PLAYGROUND_WIDTH= 400
PLAYGROUND_HEIGHT= 400
STRIDE = 10


def draw_border():
    pen = turtle.Turtle()
    pen.color('yellow')
    pen.penup()
    pen.setposition(-PLAYGROUND_WIDTH // 2 - 3, PLAYGROUND_HEIGHT // 2 + 3)
    pen.pendown()
    pen.pensize(3)
    for side in [PLAYGROUND_WIDTH, PLAYGROUND_HEIGHT,
                 PLAYGROUND_WIDTH, PLAYGROUND_HEIGHT]:
        pen.forward(side + STRIDE + 3)
        pen.right(90)
    pen.hideturtle()


def draw_square(pen, x, y, side, color):
    pen.pencolor(color)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(4):
        pen.forward(side)
        pen.right(90)
    pen.end_fill()


def draw_maze(maze):
    pen = turtle.Turtle()
    pen.penup()
    pen.goto(-PLAYGROUND_WIDTH // 2, PLAYGROUND_HEIGHT // 2)
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            color = 'black' if maze[row][col] == '1' else 'white'
            draw_square(
                pen,
                col * STRIDE - PLAYGROUND_WIDTH // 2,
                -row * STRIDE + PLAYGROUND_HEIGHT // 2,
                STRIDE,
                color
            )
    pen.hideturtle()


def make_maze(w = 16, h = 8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [['10'] * w + ['1'] for _ in range(h)] + [[]]
    hor = [['11'] * w + ['1'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = '10'
            if yy == y: ver[y][max(x, xx)] = '00'
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    maze = []
    for (a, b) in zip(hor, ver):
        maze.append(''.join(a))
        maze.append(''.join(b))
    return maze


def create_player():
    player = turtle.Turtle()
    player.color('blue')
    player.penup()
    player.speed(0)
    player.goto(-PLAYGROUND_WIDTH // 2 + STRIDE + STRIDE // 2,
                PLAYGROUND_HEIGHT // 2 - STRIDE - STRIDE // 2)
    player.direction = 'right'
    player.x = 1
    player.y = 1
    return player


maze = make_maze((PLAYGROUND_WIDTH // STRIDE) // 2, (PLAYGROUND_HEIGHT // STRIDE) // 2)

def is_free(x, y):
    result = 0 < x < len(maze) and 0 < y < len(maze[0]) and maze[y][x] == '0'
    return result


# Set up screen
window = turtle.Screen()
window.bgcolor('black')
window.tracer(0)

draw_border()
draw_maze(maze)
player = create_player()
window.update()


def player_left_is_free():
    # code here
    pass


def player_up_is_free():
    # code here
    pass


def player_right_is_free():
    # code here
    pass


def player_down_is_free():
    # code here
    pass


def go_forward():
    """
    Преместете напред на разстояние `STRIDE`, ако е възможно.
    Обновете `player.x` или `player.y`
    """
    pass


def go_backward():
    """
    Преместете назад на разстояние `STRIDE`, ако е възможно.
    Обновете `player.x` или `player.y`
    """
    pass


def turn_rigth():
    """
    Завийте надясн ако е възможно.
    Обновете `player.direction`
    """
    pass


def turn_left():
    """
    Завийте наляво ако е възможно.
    Обновете `player.direction`
    """
    pass


def quit_game():
    window.bye()


def update_after(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        window.update()
        return result
    return wrapper


# Set keyboard bindings
window.listen()
window.onkey(update_after(turn_left), 'Left')
window.onkey(update_after(turn_rigth), 'Right')
window.onkey(update_after(go_forward), 'Up')
window.onkey(update_after(go_backward), 'Down')
window.onkey(quit_game, 'q')

window.mainloop()
