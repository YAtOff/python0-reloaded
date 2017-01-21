import turtle
import time
from random import randint


PLAYGROUND_SIDE = 200
FRAME_PERIOD = 0.05


def drow_border():
    mypen = turtle.Turtle()
    mypen.color('white')
    mypen.penup()
    mypen.setposition(-PLAYGROUND_SIDE, -PLAYGROUND_SIDE)
    mypen.pendown()
    mypen.pensize(3)
    for side in range(4):
        mypen.forward(2 * PLAYGROUND_SIDE)
        mypen.left(90)
        mypen.hideturtle()


enemies = []


def place_enemies():
    square_side = PLAYGROUND_SIDE // 5
    squares_per_side = (2 * PLAYGROUND_SIDE // square_side)
    density = 0.6
    enemy_position_range = (-squares_per_side // 2 + 1, squares_per_side // 2 - 2)
    for _ in range(int((squares_per_side ** 2) * density)):
        while True:
            x = randint(*enemy_position_range)
            y = randint(*enemy_position_range)
            for e in enemies:
                if e.xcor() == x * square_side or e.ycor() == y * square_side:
                    continue
            enemy = turtle.Turtle()
            enemy.penup()
            enemy.setposition(
                x * square_side + (square_side // 2) + randint(-square_side // 2, square_side // 2),
                y * square_side + (square_side // 2) + randint(-square_side // 2, square_side // 2)
            )
            enemy.speed(0)
            enemy.color('red')
            enemy.shape('circle')
            enemies.append(enemy)
            break


def can_move(x, y):
    region = (PLAYGROUND_SIDE // 5) // 3
    def in_range(i, j):
        return (j - region) <= i and i <= (j + region)

    for e in enemies:
        if in_range(x, e.xcor()) and in_range(y, e.ycor()):
            return False
    return True


def play(move_player):
    window = turtle.Screen()
    window.bgcolor('black')
    window.tracer(0)

    player = turtle.Turtle()
    player.penup()
    player.setposition(-PLAYGROUND_SIDE, 0)
    player.speed(0)
    player.color('white')

    play_game = True

    def quit_game():
        play_game = False

    window.listen()
    window.onkey(quit_game, 'q')

    drow_border()
    place_enemies()

    while play_game:
        start_time = time.clock()

        old_x, old_y = player.xcor(), player.ycor()

        move_player(player)

        x, y = player.xcor(), player.ycor()
        if 1 < abs(old_x - x) or 1 < abs(old_y - y):
            play_game = False
        elif not can_move(x, y):
            play_game = False
        elif player.xcor() == PLAYGROUND_SIDE:
            play_game = False

        window.update()
        elapsed = time.clock() - start_time
        if elapsed < FRAME_PERIOD:
            time.sleep(FRAME_PERIOD - elapsed)

    window.bye()
