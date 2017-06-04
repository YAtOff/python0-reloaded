import turtle

MAX_ERRORS = 5

hangman_builder = turtle.Turtle()
hangman_builder.penup()
hangman_builder.goto(-100, -200)
hangman_builder.pendown()

def build_hangman(step):
    if step == 1:
        pass
    elif step == 2:
        pass
    elif step == 3:
        pass
    elif step == 4:
        pass
    elif step == 5:
        pass
    # Добавете до MAX_ERRORS стъпки
    else:
        print('You lost')


if __name__ == '__main__':
    for step in range(1, MAX_ERRORS + 1):
        build_hangman(step)

