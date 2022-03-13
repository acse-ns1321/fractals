import turtle


# Lindenmayer system to draw the fractal
def koch_fract(turtle, divis, size):
   if(divis == 0):
      turtle.forward(size)
   else:
      for angle in [60, -120, 60, 0]:
         koch_fract(turtle, divis - 1, size / 3)               
         turtle.left(angle)

# set some variables for the parameters to enter into the function
divis = 30 # any number of divisions, the larger the number, the more detailed the diagram
size = 2000 # any length

# set up the turtle and screen
wn = turtle.Screen()
wn.setup(width=1000, height=500)
turtle.speed(10)
turtle.pendown()

# loop to use our Koch curve function to create the Koch Snowflake
for i in range(0, 3):
   koch_fract(turtle, divis, size)
   turtle.left(-120)


