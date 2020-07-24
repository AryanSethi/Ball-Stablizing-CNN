import turtle as t
from math import sin,cos,pi

running=True
wn= t.Screen()
wn.title("Balance")
wn.bgcolor("black")
wn.setup(width=800,height=800)
wn.tracer(0)

plank= t.Turtle()
plank.speed(0)
plank.shape("square")
plank.color("blue")
plank.shapesize(stretch_len=20, stretch_wid=0.1)
plank.penup()
plank.goto(0,-200)

ball= t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.shapesize(stretch_len=0.5, stretch_wid=0.5)
ball.penup()
ball.goto(0,-185)
ball.dx= 0
ball.dy=0


theta=0
u=0
g=0.001
k= pi/180

def ball_position():
    global theta,vel,g,u
    x = ball.xcor()
    y = ball.ycor()
    g_new=g*sin(theta*k)
    v= u + g_new
    ball.dx= -v*cos(theta*k)
    ball.dy= -v*sin(theta*k)
    ball.setx(x+ball.dx)
    ball.sety(y+ball.dy)
    u=v


def plank_right():
    global theta
    plank.right(3)
    theta = theta-3
    print(theta)


def plank_left():
    global theta
    plank.left(3)
    theta=theta+3
    print(theta)


def quit_game():
    global running
    running =False


wn.listen()
wn.onkeypress(plank_left,"Left")
wn.onkeypress(plank_right,"Right")
wn.onkeypress(quit_game,"q")


while running:
    wn.update()
    ball_position()

