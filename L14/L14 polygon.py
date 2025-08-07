import turtle #importing library

paper = turtle.Screen() # make the paper on the screen
paper.bgcolor("lightblue") # set the 'paper' background color
paper.setup(500,500) # width = 500, height = 500
paper.title("Polygon")

pen = turtle.Turtle() #make the pen

num_sides = 6 # number of hexagon's  side
side_length = 100 #for the hexagon size

angle = 360 / num_sides

for i in range(num_sides):
    pen.forward(side_length) #move the pen
    pen.right(angle) # turn the pen

turtle.done()