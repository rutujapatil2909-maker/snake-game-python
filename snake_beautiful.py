import tkinter as tk
import random

WIDTH = 500
HEIGHT = 500
SIZE = 20

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Snake Game - Mini Project")

        self.frame = tk.Frame(root, bg="#1e1e2f")
        self.frame.pack()

        self.title = tk.Label(self.frame, text="SNAKE GAME",
                              font=("Arial", 24, "bold"),
                              fg="white", bg="#1e1e2f")
        self.title.pack(pady=10)

        self.score_label = tk.Label(self.frame, text="Score: 0",
                                    font=("Arial", 14),
                                    fg="yellow", bg="#1e1e2f")
        self.score_label.pack()

        self.canvas = tk.Canvas(self.frame,
                                width=WIDTH,
                                height=HEIGHT,
                                bg="black",
                                highlightthickness=0)
        self.canvas.pack(pady=10)

        self.button_frame = tk.Frame(self.frame, bg="#1e1e2f")
        self.button_frame.pack()

        self.start_button = tk.Button(self.button_frame,
                                      text="Start Game",
                                      font=("Arial", 12, "bold"),
                                      bg="green",
                                      fg="white",
                                      width=12,
                                      command=self.start_game)
        self.start_button.grid(row=0, column=0, padx=10)

        self.restart_button = tk.Button(self.button_frame,
                                        text="Restart",
                                        font=("Arial", 12, "bold"),
                                        bg="orange",
                                        fg="black",
                                        width=12,
                                        command=self.restart_game)
        self.restart_button.grid(row=0, column=1, padx=10)

        self.root.bind("<Key>", self.change_direction)

        self.running = False

    def start_game(self):
        if not self.running:
            self.running = True
            self.snake = [(100, 100)]
            self.direction = "Right"
            self.food = self.create_food()
            self.score = 0
            self.move()

    def restart_game(self):
        self.canvas.delete("all")
        self.running = False
        self.score_label.config(text="Score: 0")

    def create_food(self):
        x = random.randint(0, (WIDTH//SIZE)-1) * SIZE
        y = random.randint(0, (HEIGHT//SIZE)-1) * SIZE
        return (x, y)

    def change_direction(self, event):
        key = event.keysym
        if key in ["Up", "Down", "Left", "Right"]:
            self.direction = key

    def move(self):
        if not self.running:
            return

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
                                    text="GAME OVER",
                                    fill="red",
                                    font=("Arial", 28, "bold"))
            self.running = False
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.create_food()
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.snake.pop()

        self.draw()
        self.root.after(100, self.move)

    def draw(self):
        self.canvas.delete("all")

        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1],
                                         segment[0]+SIZE, segment[1]+SIZE,
                                         fill="#00ff88", outline="")

        self.canvas.create_oval(self.food[0], self.food[1],
                                self.food[0]+SIZE, self.food[1]+SIZE,
                                fill="red")

root = tk.Tk()
root.configure(bg="#1e1e2f")
game = SnakeGame(root)
root.mainloop()