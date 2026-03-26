import tkinter as tk
import random

WIDTH = 400
HEIGHT = 400
SIZE = 20

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100)]
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0

        self.root.bind("<Key>", self.change_direction)

        self.move()

    def create_food(self):
        x = random.randint(0, (WIDTH//SIZE)-1) * SIZE
        y = random.randint(0, (HEIGHT//SIZE)-1) * SIZE
        return (x, y)

    def change_direction(self, event):
        key = event.keysym
        if key in ["Up", "Down", "Left", "Right"]:
            self.direction = key

    def move(self):
        x, y = self.snake[0]

        if self.direction == "Up":
            y -= SIZE
        elif self.direction == "Down":
            y += SIZE
        elif self.direction == "Left":
            x -= SIZE
        elif self.direction == "Right":
            x += SIZE

        new_head = (x, y)

        if (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or new_head in self.snake):
            self.canvas.create_text(WIDTH/2, HEIGHT/2, 
                                    text="Game Over", fill="red", font=("Arial", 24))
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.create_food()
            self.score += 1
        else:
            self.snake.pop()

        self.draw()
        self.root.after(100, self.move)

    def draw(self):
        self.canvas.delete("all")

        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1],
                                         segment[0]+SIZE, segment[1]+SIZE,
                                         fill="green")

        self.canvas.create_rectangle(self.food[0], self.food[1],
                                     self.food[0]+SIZE, self.food[1]+SIZE,
                                     fill="red")

        self.canvas.create_text(50, 10, text=f"Score: {self.score}",
                                fill="white", font=("Arial", 12))

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()