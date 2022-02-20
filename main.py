"""This the python learning course in which I'm going to develop
a game called Snake Game. So let's get started """

import turtle

# Define program constants
WIDTH = 600
HEIGHT = 600

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Dot Catcher")
screen.bgcolor("white")

# Create a turtle to do your bidding
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

# Your turtle awaits your command
my_turtle.forward(100)  # Sample command

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()