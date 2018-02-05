import turtle
from turtle import *
import time
import random
import math
from ball import Ball

turtle.register_shape("life_loss.gif")
turtle.register_shape("death.gif")
#BgChanger=turtle.clone()
#BgChanger.shape("life_loss.gif")
#BgChanger.ht()
#Hearts=3
# turtle.register_shape("test.gif")
# heart=turtle.clone()
# heart.pu()
# heart.shape("test.gif")

score=turtle.clone()
score.ht()
score.pu()
turtle.register_shape("test.gif")
score.shape("test.gif")
d=50
a=50
health_pos1=(int(680/2) -d-a*2,600/2 -d)
health_pos2=(int(680/2) -d-a,600/2 -d)
health_pos3=(int(680/2) -d,600/2 -d)
health_positions=[(health_pos1),(health_pos2),(health_pos3)]

def heart_stamps():
    for position in health_positions:
        score.goto(position)
        score.stamp()

# score=turtle.clone()
# score.pu()
# score.ht()
# score.pencolor("white")


#def my_score(event):
    # X = (event.x - round(SCREEN_WIDTH))
    # Y = (round(SCREEN_HEIGHT) - event.y)
    # score.goto(X,Y)
    # score.write(BallsEaten)






# d=50
# a=50
# health1=(int(680/2) -d,600/2 -d)
# health2=(int(680/2) -d-a,600/2 -d)
# health3=(int(680/2) -d-a*2,600/2 -d)

# heart_pos=[(health1),(health2),(health3)]
# heart_stamp_list=[]

#for position in heart_pos:
    # heart.goto(position)
    # new_heart=heart.stamp()
    # heart_stamp_list.append(new_heart)

#def lose_heart():
    # current_health=int(len(heart_stamp_list))
    # if check_myball_eaten==True and current_health >1:
    #     old_stamp=heart_stamp_list.pop(-1)
    #     heart.clearstamp(old_stamp)
    #     turtle.clearscreen()
        # Generate_Balls()
        # MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)
        # move_all_balls()
        # check_all_balls_collision()
        # MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)
        # turtle.getscreen().update()

    # else:
    #     turtle.clear()
    #     turtle.write("GameOver", font=("Arial",40))
    #     global RUNNING
    #     RUNNING = False

colormode(255)

turtle.hideturtle()


RUNNING = True

SLEEP = 0.016

SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

turtle.bgpic("sbg.gif")


# color=()
MY_BALL = Ball(0, 0, 0, 0, 30, "black")
# counter=Turtle()
# counter.ht()
# counter.pu()
# counter.goto(0,0)
# counter.write(str(score))

MAXIMUM_NUMBER_OF_BALLS = 5

MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 40

MINIMUM_BALL_DX = 1
MAXIMUM_BALL_DX = 3

MINIMUM_BALL_DY = 1
MAXIMUM_BALL_DY = 3
turtle.tracer(0.5)

BALLS = []


def Generate_Balls():
    while len(BALLS) < MAXIMUM_NUMBER_OF_BALLS:
        r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
        while True:
            global x 
            x= random.randint(round(-SCREEN_WIDTH)+MAXIMUM_BALL_RADIUS,
                               round(SCREEN_WIDTH) - MAXIMUM_BALL_RADIUS)
            global y
            y = random.randint(round(-SCREEN_HEIGHT)+MAXIMUM_BALL_RADIUS,
                               round(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS)
            DistanceFromMyBall = math.sqrt(
                math.pow(x-MY_BALL.x, 2) + math.pow(y-MY_BALL.y, 2))
            if DistanceFromMyBall > MY_BALL.r+r:
                break
        dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
        while(dx == 0):
            dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)

        dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
        while(dy == 0):
            dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)

        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        color = (R, G, B)
        #while color == "white":
        #    color = (R, G, B)
        ball = Ball(x, y, dx, dy, r, color)
        BALLS.append(ball)


def move_all_balls():
    for ball in BALLS:
        ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)


def collide(ball_a, ball_b):
    if ball_a == ball_b:
        return False

    x1 = ball_a.xcor()
    y1 = ball_a.ycor()

    x2 = ball_b.xcor()
    y2 = ball_b.ycor()

    Distance = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))

    if Distance == 0:
        return False
    if Distance < ball_a.r+ball_b.r:
        return True

    else:
        return False


def check_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS:
            if collide(ball_a, ball_b) == True:

                ra = ball_a.r
                rb = ball_b.r
                if ra > rb:
                    ball_a.r += 1  
                    ball_a.shapesize(ball_a.r/10)
                    BALLS.remove(ball_b)
                    remove_ball(ball_b)
                    break
                else:
                    ball_b.r += 1  
                    ball_b.shapesize(ball_b.r/10)
                    BALLS.remove(ball_a)
                    remove_ball(ball_a)
                    break

def remove_ball(ball):
	ball.x=SCREEN_WIDTH
	ball.y=SCREEN_HEIGHT
	ball.shapesize(0.000000000000000000000000000000000000000001)
	ball.shape("classic")
	ball.goto(ball.x,ball.y)
def check_myball_eaten():
    for enemy in BALLS:
        if collide(MY_BALL, enemy) == True:
            if enemy.r > MY_BALL.r:
                return True
                
            MY_BALL.r += enemy.r/30
            #BallsEaten+=1
            
            MY_BALL.shapesize(MY_BALL.r/10)
            
            turtle.clear()
            enemy.clearstamps()
            BALLS.remove(enemy)
            remove_ball(enemy)
    return False


def movearound(event):
    X = (event.x - round(SCREEN_WIDTH))
    Y = (round(SCREEN_HEIGHT) - event.y)
    MY_BALL.goto(X,Y)
    #counter.goto(X,Y)


turtle.getcanvas().bind("<Motion>", movearound )#,my_score)
#turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()




while RUNNING == True:
    heart_stamps()
    #score.goto(MY_BALL.x,MY_BALL.y)
    #score.write(BallsEaten)
    # move_all_balls()
    # check_all_balls_collision()
    Generate_Balls()
    MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    # Surprise from your fellow TA. Good luck with your project. Just a reminder to not keep your laptop open like this!
    # :)
    # SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
    # SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
    move_all_balls()
    check_all_balls_collision()
    MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    if check_myball_eaten() == True and len(health_positions)>=1:
        #lose_heart()
        health_positions.pop(0)
        score.clearstamps()
        heart_stamps()
        #exit()
        #turtle.clearscreen()
        turtle.bgpic("life_loss.gif")
        turtle.getscreen().update()
        time.sleep(1)

        turtle.bgpic("sbg.gif")
        heart_stamps()
        MY_BALL.goto(x,y)
        time.sleep(0.5)
        if len(health_positions)==0:
            turtle.clearscreen()
            turtle.clear()
            turtle.ht()
            turtle.bgpic("death.gif")
            #time.sleep(0.5)
            break        


    turtle.getscreen().update()            
    time.sleep(SLEEP)



turtle.mainloop()
