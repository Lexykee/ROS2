from turtle import Screen, Turtle

WIDTH, HEIGHT = 800, 800

screen = Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

turtle = Turtle()
turtle.hideturtle()
turtle.penup()

# Define the gradient colors
start_color = (255, 0, 0)  # Red
end_color = (0, 0, 255)    # Blue

# Calculate the color increment for each step
color_steps = 100
color_increment = [(end_color[i] - start_color[i]) / color_steps for i in range(3)]

# Set the initial color
current_color = start_color

def draw_line(length):
    turtle.pendown()
    turtle.forward(length)

def fractal_dragon(level, distance, is_forward=True):
    if level == 0:
        draw_line(distance)
    else:
        if is_forward:
            turtle.right(45)
            fractal_dragon(level - 1, distance, True)
            turtle.left(90)
            fractal_dragon(level - 1, distance, False)
            turtle.right(45)
        else:
            turtle.left(45)
            fractal_dragon(level - 1, distance, True)
            turtle.right(90)
            fractal_dragon(level - 1, distance, False)
            turtle.left(45)

def draw_fractal_dragon():
    turtle.penup()
    turtle.goto(WIDTH/2 - 200, HEIGHT/2 - 200)  # Starting position
    turtle.pendown()

    global current_color  # Declare the variable as global

    for i in range(color_steps):
        # Convert RGB color values to strings
        color_str = "#%02x%02x%02x" % current_color
        turtle.pencolor(color_str)
        fractal_dragon(15, 5, True)  # Adjust the level and distance as desired
        current_color = tuple(current_color[i] + color_increment[i] for i in range(3))

draw_fractal_dragon()

screen.exitonclick()

