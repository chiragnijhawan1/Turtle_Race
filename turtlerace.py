import turtle as t 
import random
Screen=t.Screen()
Screen.setup(1000,1000)
Screen.bgcolor("light green")
t.speed(0)
startx = -300

for i in range(13):
    t.penup()
    t.goto(i*50 + startx, 300)
    t.pendown()
    t.write(i+1)
    t.setheading(-90)
    for i in range (21):
        t.forward(20)
        t.penup()
        t.forward(10)
        t.pendown()

t.write("Finish Line")

def createPlayers(name,color,xcord,ycord):
    tNew = t.Turtle()
    tNew.shape("turtle")
    tNew.color(color)
    tNew.penup()
    tNew.goto(xcord, ycord)
    tNew.pendown()
    tNew.write(name)
    return tNew

def declareWinner(winner):
    winner.penup()
    winner.goto(0, 350)
    winner.pendown()
    winner.write("I won the race!!!", font=("Jokerman", 40, "bold", "italic"), align="center")
    while True:
        winner.right(5)
    
p1=createPlayers("player 1", "blue", -320, 275)
p2=createPlayers("player 2", "pink", -320, 200)
p3=createPlayers("player 3", "yellow", -320, 125)
p4=createPlayers("player 4", "black", -320, 50)
p5=createPlayers("player 5", "red", -320, -25)
p6=createPlayers("player 6", "orange", -320, -100)
p7=createPlayers("player 7", "magenta", -320, -175)
p8=createPlayers("player 8", "grey", -320, -250)
p9=createPlayers("Player 9", "gold", -320, -325)

finish_line= 300
while True:
    p1.fd(random.randint(1,5)) 
    if p1.pos()[0]>=finish_line:
        declareWinner(p1)
        break
    p2.fd(random.randint(1,5)) 
    if p2.pos()[0]>=finish_line:
        declareWinner(p2)
        break
    p3.fd(random.randint(1,5)) 
    if p3.pos()[0]>=finish_line:
        declareWinner(p3)
        break
    p4.fd(random.randint(1,5)) 
    if p4.pos()[0]>=finish_line:
        declareWinner(p4)
        break
    p5.fd(random.randint(1,5)) 
    if p5.pos()[0]>=finish_line:
        declareWinner(p5)
        break
    p6.fd(random.randint(1,5)) 
    if p6.pos()[0]>=finish_line:
        declareWinner(p6)
        break
    p7.fd(random.randint(1,5)) 
    if p7.pos()[0]>=finish_line:
        declareWinner(p7)
        break
    p8.fd(random.randint(1,5)) 
    if p8.pos()[0]>=finish_line:
        declareWinner(p8)
        break
    p9.fd(random.randint(1,5)) 
    if p9.pos()[0]>=finish_line:
        declareWinner(p9)
        break
t.done()

