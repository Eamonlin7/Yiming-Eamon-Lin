#import the modules (turtle & time)
import turtle
import time 

# create a screen
final = turtle.getscreen()
final.bgcolor("white")
final.title("U.S. Flag Project")

# initialize the object and speed of the turtle
p = turtle.Turtle()
p.speed(1000)
p.penup()

# the function to draw one rectangle: stripes & navy square
def draw_rectangle(x, y, length, height, color):
    p.goto(x,y)       # starting from the point(x,y)
    p.pendown()
    p.color(color)     # color filled
    p.begin_fill()
    p.forward(length)  # length of the rectangle
    p.right(90)
    p.forward(height)  # height of the rectangle
    p.right(90)
    p.forward(length)
    p.right(90)         # make it a rectangle
    p.forward(height)
    p.right(90)
    p.end_fill()
    p.penup()

# create stripes of the flag (total 13 stripes: 7 red + 6 white)
def draw_stripes():
    # starting points of the US flag (half of flag width and of flag height)
    start_x = -250
    start_y = 120
    
    # height and width of the flag
    height_flag = 250
    width_flag = 475
    
    # height and width of the stripes 
    stripe_height = height_flag/13
    stripe_width = width_flag
    
    # draw 7 red stripes
    for stripe in range(7):
        for color in ["red", "white"]:
            draw_rectangle(start_x, start_y, stripe_width, stripe_height, color)
            # Decrease value of y by stripe_height for each stripe continuing
            start_y -= stripe_height
  
#  create the navy color square at the top-left corner of the flag
def draw_navy_square():
    height_flag = 250
    
    square_ht = 7/13 * height_flag
    square_wdt = 0.75 * height_flag
    draw_rectangle(-250, 120, square_wdt, square_ht, 'navy')

# draw 1 star: shape & size & color
def draw_star(x,y,length,color) :
    p.goto(x,y)
    p.setheading(0)
    p.pendown()
    p.color(color)
    p.begin_fill()
    for i in range(5):
        p.forward(length)
        p.right(144)
        
    p.end_fill()
    p.penup()
    
# draw 6 rows of 5 stars
def draw_all_stars_p1():
    #star size
    star_size = 12
    # height and width of the flag
    height_flag = 250
    width_flag = 475
    # height and width of the stripes (total 13 stripes: 7 red + 6 white)
    stripe_height = height_flag/13
    stripe_width = width_flag 
        
    lines = stripe_height + 6
    y = 110
    # create 5 rows of stars
    for row in range(5):
        x = -234
        # create 6 stars in each row
        for star in range (6):
            draw_star(x, y, star_size,'white')
            x += 30                         # seperate each star by 30
        y -= lines                          # seperate each line

# draw 5 rows of 4 stars
def draw_all_stars_p2():
    # height and width of the flag
    height_flag = 250
    width_flag = 475
    # height and width of the stripes (total 13 stripes: 7 red + 6 white)
    stripe_height = height_flag/13
    stripe_width = width_flag 
    
    # the size of each star
    star_size = 12
    
    lines = stripe_height + 6
    y = 100
    # create 4 rows of stars
    for row in range(0,4) :
        x = -217
        # create 5 stars in each row
        for star in range (5):
            draw_star(x, y, star_size, 'white')
            x += 30                    # seperate each star by 30
        y -= lines                      # seperate each line
        

# Call all functions
draw_stripes()
draw_navy_square()

# draw 30 stars (6 rows * 5 stars each)
draw_all_stars_p1()
# draw 20 stars (5 rows * 4 stars each)
draw_all_stars_p2()

# hide the turtle cursor
p.hideturtle()

if __name__ == "__main__":
    final.main()