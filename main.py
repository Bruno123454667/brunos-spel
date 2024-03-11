import turtle
import time
import random

#reset game frame
def reset():
    reset.sleep

# frame
gameframe = 1
def gameframe ():
    frame = turtle.Turtle()
    frame.penup()
    frame.goto(-310,310)
    frame.pendown()

#frame = turtle.Turtle()
    frame.forward(620)
    frame.left(-90)
    frame.forward(620)
    frame.left(-90)
    frame.forward(620)
    frame.left(-90)
    frame.forward(620)

gameframe2 = 0

def gameframe2():
    frame = turtle.Turtle()
    frame.penup()
    frame.goto(-260, 260)
    frame.pendown()

    # frame = turtle.Turtle()
    frame.forward(310)
    frame.left(-45)
    frame.forward(310)
    frame.left(-45)
    frame.forward(310)
    frame.left(-45)
    frame.forward(310)

# Screen settings (color, height and width)

wn = turtle.Screen()
wn.title("snake game")
wn.bgcolor("grey")
wn.setup(width = 600, height = 600)
wn.tracer(0)
wn.tracer(0) #turns of the screen updates

# snake head

#animation speed
head = turtle.Turtle()
head.speed(0)

#color and shape of the head
head.shape("circle")
head.color("green")

#delay
delay = 0.2

# score
score = 0
high_score = 0



# start in the center
head.penup()
head.goto(0,0)

head.direction = ("stop")

# food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,40)


# score board
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 high score: 0", align= "center", font = ("courier", 24,  "normal"))


#=====================
# test att försöka göra spel planen mindre
#=====================
#gameframe2()
#wn.update()
#time.sleep(10)
#turtle.reset()
#wn.update()
#gameframe()
#wn.update()
#time.sleep(10)
#gameframe3()...
#=====================
#test att göra spel planen mindre
#=====================
#while True:
    #wn.update()

    #if delay == 0.2:
        #gameframe()
    #elif delay < 0.19:
        #gameframe2()
#=====================

# prevents the snake from going opposite way from where facing
# up
def go_up():
    if head.direction != "down":
        head.direction = "up"

# down
def go_down():
    if head.direction != "up":
        head.direction = "down"

# right
def go_right():
    if head.direction != "left":
        head.direction = "right"

# left
def go_left():
    if head.direction != "right":
        head.direction = "left"



# keybinds (w,a,s,d)
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")

# keybinds (pilar)
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_left,"Left")




# the snakes segments
segments = []

# function up
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

# function down
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

# function right
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# function left
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)



#main game loop
while True:
    wn.update() #uppdate the screen when loop

# Check for a collision with border

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"



        #hide segments

        for segment in segments:
            segment.goto(1000, 1000) # moves the segment out of the screen (not delating them)


        #Clear segment list
        segments = []

        # reset score
        score = 0

        # reset speed
        delay = 0.2

        #update score
        pen.clear()
        pen.write("Score: {} high score: {}".format(score, high_score), align="center", font=("courier", 24, "normal"))

#check for coalition with food
    if head.distance(food) < 20:
        #move food
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        food.goto(x,y)

        #add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("lime green")
        new_segment.penup()
        segments.append(new_segment)

        #increase the speed

        if delay > 0.03:
            delay -= 0.004


        # increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} high score: {}".format(score, high_score), align="center", font = ("courier", 24,  "normal"))



# move end segments in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)


# move segment zero to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()
# check for head collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"


            for segment in segments:
                segment.goto(1000, 1000)  # moves the segment out of the screen (not delating them)

            # Clear segment list
            segments = []

            # reset score
            score = 0
            # update score
            pen.clear()
            pen.write("Score: {} high score: {}".format(score, high_score), align="center", font=("courier", 24, "normal"))

    time.sleep(delay)


wn.mainloop()