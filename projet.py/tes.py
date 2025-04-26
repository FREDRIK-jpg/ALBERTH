import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle to draw
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(5)

# Function to draw the head (circle)
def draw_head():
    pen.penup()
    pen.goto(0, -100)  # Move the turtle to the starting position
    pen.pendown()
    pen.begin_fill()
    pen.color("peachpuff")
    pen.circle(100)
    pen.end_fill()

# Function to draw the eyes
def draw_eyes():
    # Left eye
    pen.penup()
    pen.goto(-35, 50)
    pen.pendown()
    pen.begin_fill()
    pen.color("white")
    pen.circle(15)
    pen.end_fill()

    # Right eye
    pen.penup()
    pen.goto(35, 50)
    pen.pendown()
    pen.begin_fill()
    pen.color("white")
    pen.circle(15)
    pen.end_fill()

    # Pupils
    # Left pupil
    pen.penup()
    pen.goto(-35, 55)
    pen.pendown()
    pen.begin_fill()
    pen.color("black")
    pen.circle(5)
    pen.end_fill()

    # Right pupil
    pen.penup()
    pen.goto(35, 55)
    pen.pendown()
    pen.begin_fill()
    pen.color("black")
    pen.circle(5)
    pen.end_fill()

# Function to draw the mouth
def draw_mouth():
    pen.penup()
    pen.goto(-40, 20)
    pen.pendown()
    pen.setheading(-60)
    pen.circle(50, 120)

# Function to draw the hair (representing Naruto's spiky hair)
def draw_hair():
    pen.penup()
    pen.goto(-70, 100)
    pen.pendown()
    pen.setheading(30)
    pen.forward(50)
    
    pen.penup()
    pen.goto(-60, 110)
    pen.pendown()
    pen.setheading(20)
    pen.forward(50)
    
    pen.penup()
    pen.goto(60, 100)
    pen.pendown()
    pen.setheading(150)
    pen.forward(50)
    
    pen.penup()
    pen.goto(50, 110)
    pen.pendown()
    pen.setheading(160)
    pen.forward(50)

# Function to draw Naruto's headband
def draw_headband():
    # Draw the headband
    pen.penup()
    pen.goto(-80, 120)
    pen.pendown()
    pen.setheading(0)
    pen.begin_fill()
    pen.color("gray")
    pen.forward(160)
    pen.right(90)
    pen.forward(30)
    pen.right(90)
    pen.forward(160)
    pen.right(90)
    pen.forward(30)
    pen.end_fill()

    # Draw the symbol (the leaf)
    pen.penup()
    pen.goto(0, 120)
    pen.pendown()
    pen.color("black")
    pen.circle(10, 360)
    pen.penup()

# Draw the complete face
draw_head()
draw_eyes()
draw_mouth()
draw_hair()
draw_headband()

# Hide the turtle and finish
pen.hideturtle()

# Finish
screen.mainloop()