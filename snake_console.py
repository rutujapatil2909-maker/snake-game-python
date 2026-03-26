import random
import os
import time

WIDTH = 20
HEIGHT = 10

snake = [(5, 5)]
direction = "RIGHT"

food = (random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw():
    clear()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in snake:
                print("O", end="")
            elif (x, y) == food:
                print("*", end="")
            elif x == 0 or x == WIDTH-1 or y == 0 or y == HEIGHT-1:
                print("#", end="")
            else:
                print(" ", end="")
        print()

def move():
    global food
    head_x, head_y = snake[0]

    if direction == "UP":
        new_head = (head_x, head_y - 1)
    elif direction == "DOWN":
        new_head = (head_x, head_y + 1)
    elif direction == "LEFT":
        new_head = (head_x - 1, head_y)
    else:
        new_head = (head_x + 1, head_y)

    if new_head in snake or \
       new_head[0] == 0 or new_head[0] == WIDTH-1 or \
       new_head[1] == 0 or new_head[1] == HEIGHT-1:
        return False

    snake.insert(0, new_head)

    if new_head == food:
        food = (random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2))
    else:
        snake.pop()

    return True

# Game loop
while True:
    draw()
    print("Score:", len(snake) - 1)
    print("Use W A S D to move")

    move_input = input("Move: ").upper()

    if move_input == "W":
        direction = "UP"
    elif move_input == "S":
        direction = "DOWN"
    elif move_input == "A":
        direction = "LEFT"
    elif move_input == "D":
        direction = "RIGHT"
    else:
        continue

    if not move():
        print("💀 Game Over!")
        print("Final Score:", len(snake) - 1)
        break