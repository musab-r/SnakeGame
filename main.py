"""This the python learning course in which I'm going to develop
a game called Snake Game. So let's get started """

# Import the Turtle Graphics module
import turtle
from Procedural import offsets, get_distance, get_random_food_pos, colors, shapes


class SnakeGame:
    def __init__(self, width=800, height=600, delay=100, food_size=10):
        # Define program constants
        self.WIDTH = width
        self.HEIGHT = height
        self.DELAY = delay  # Milliseconds
        self.FOOD_SIZE = food_size
        self.food = None
        self.snake_direction = None
        self.score = 0
        self.snake = None
        self.food_pos = None
        self.screen = None
        self.stamper = None
        self.high_score= 0

    def set_snake_direction(self, direction):

        if direction == "up":
            if self.snake_direction != "down":  # No self-collision simply by pressing wrong key.
                self.snake_direction = "up"
        elif direction == "down":
            if self.snake_direction != "up":
                self.snake_direction = "down"
        elif direction == "left":
            if self.snake_direction != "right":
                self.snake_direction = "left"
        elif direction == "right":
            if self.snake_direction != "left":
                self.snake_direction = "right"

    def bind_direction_keys(self):
        self.screen.onkey(lambda: self.set_snake_direction("up"), "Up")
        self.screen.onkey(lambda: self.set_snake_direction("down"), "Down")
        self.screen.onkey(lambda: self.set_snake_direction("left"), "Left")
        self.screen.onkey(lambda: self.set_snake_direction("right"), "Right")

    def game_loop(self):
        self.stamper.clearstamps()  # Remove existing stamps made by stamper.

        new_head = self.snake[-1].copy()
        new_head[0] += offsets[self.snake_direction][0]
        new_head[1] += offsets[self.snake_direction][1]

        # Check collisions
        if new_head in self.snake or new_head[0] < - self.WIDTH / 2 or new_head[0] > self.WIDTH / 2 \
                or new_head[1] < - self.HEIGHT / 2 or new_head[1] > self.HEIGHT / 2:
            self.reset()
        else:
            # Add new head to snake body.
            self.snake.append(new_head)

            # Check food collision
            if not self.food_collision():
                self.snake.pop(0)  # Keep the snake the same length unless fed.

            # Draw snake for the first time.
            for segment in self.snake:
                self.stamper.goto(segment[0], segment[1])
                self.stamper.stamp()

            # Refresh screen
            self.screen.title(f"Snake Game. --- Score: {self.score} --- High Score: {self.high_score} ---")
            self.screen.update()

            # Rinse and repeat
            turtle.ontimer(self.game_loop, self.DELAY)

    def food_collision(self):
        if get_distance(self.snake[-1], self.food_pos) < 20:
            self.score += 1  # score = score + 1
            self.food_pos = get_random_food_pos(self.WIDTH, self.HEIGHT, self.FOOD_SIZE)
            self.food.goto(self.food_pos)
            return True
        if self.high_score < self.score:
            self.high_score = self.score
        return False

    def reset(self):
        self.score = 0
        self.snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
        self.snake_direction = "up"
        self.food_pos = get_random_food_pos(self.WIDTH, self.HEIGHT, self.FOOD_SIZE)
        self.food.goto(self.food_pos)
        self.game_loop()

    def food_install(self):
        # Food
        self.food = turtle.Turtle()
        self.food.shape(shapes)
        self.food.color(colors)
        self.food.fillcolor(colors)
        self.food.shapesize(self.FOOD_SIZE / 20)
        self.food.penup()

    def create_screen(self):
        # Create a window where we will do our drawing.
        self.screen = turtle.Screen()
        self.screen.setup(self.WIDTH, self.HEIGHT)  # Set the dimensions of the Turtle Graphics window.
        self.screen.title("Snake Game")
        self.screen.bgcolor("white")
        self.screen.tracer(0)  # Turn off automatic animation.

        # Event handlers
        self.screen.listen()
        self.bind_direction_keys()

    def create_stamper(self):
        # Create a turtle to do your bidding
        self.stamper = turtle.Turtle()
        self.stamper.shape("circle")
        self.stamper.color("green")
        self.stamper.penup()
        self.stamper.goto(0, 0)
        self.stamper.direction = "Stop"


sg = SnakeGame()
sg.create_screen()
sg.create_stamper()
sg.food_install()

sg.reset()

turtle.done()
del sg
