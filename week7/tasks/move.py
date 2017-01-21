import turtle
import time

FRAME_PERIOD = 1.0

window = turtle.Screen()
window.bgcolor('black')
window.tracer(0)
window.listen()
window.onkey(window.bye, 'q')

player = turtle.Turtle()
player.penup()
player.setposition(-200, 0)
player.speed(0)
player.color('white')


def move(offset):
    start_time = time.clock()

    player.forward(offset)

    window.update()
    time.sleep(FRAME_PERIOD)


def travel(speed, distance):
    """
    Целта е да продвижите играча надясно на разсояние `distance` със
    скорост `speed`.
    Придвижването става като извиквате функцията `move` със аргумент
    расзтоянието на което искате да се промести играча.
    Едно придвижване отнема 1 секунда.

    Напр.:
        Ако искате да придвижите играча на разстояние 300 пиксела за 3 секунди,
        трябва да извикате `move` 3 пъти с аргумент 100.
    """
    pass
    # Добавете вашия код тук


# v = 10 пиксела/сек, t = 300 пиксела
travel(10, 300)

window.bye()
