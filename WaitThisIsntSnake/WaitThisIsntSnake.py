try:
    import requests
    print("API Functionality Enabled!")
except:
    print("API Not Available.")
    print("To enable API functionality:")
    print(">Open Command Prompt")
    print('>Type "pip install requests" and wait')
    print(">If successful, close this program and run it again.")
    print(">Otherwise, I don't know how to help you.")
    pass
import turtle
import time
import random
import functools as func
import json
import sys

print("\nUse LEFT and RIGHT arrow keys to turn.")
print("If you go out of bounds, you will loop around the screen.")
print("\nEating food will give you a boost.")
print("Using a boost will boost you forward a short distance.")
print("While boosting, you are invulnerable and can pass through walls.")
print("You can use a boost with the UP arrow key.")
print("\nIMPORTANT: To end the game properly, press ESC.")
print("Otherwise, your high score won't be written to the leaderboard.")
print("Additionally, the Python file may have to be in its own folder in order to write the highscore file.")

#Score ReadWrite
score=0
try:
    with open("highscore.json", "r") as file:
        print("\n   Leaderboard!\n+"+"-"*16+"+")
        scoredict=json.load(file)
        leaderboard=reversed(sorted([(i[1],i[0]) for i in scoredict.items()]))
        for i in leaderboard:
            print("|{0:<10}: {1:>4}|".format("{:.10}".format(i[1]),"{:.4}".format(str(i[0]))))
        print("+"+"-"*16+"+")
except:
    print("Attempting to create highscore.json.")
    scoredict=dict(zip([chr(x)*3 for x in range(ord("A"),ord("K"))],[0 for x in range(10)]))
    leaderboard=reversed(sorted([(i[1],i[0]) for i in scoredict.items()]))
    with open("highscore.json", "w") as file:
        json.dump(scoredict,file)
    print("\n   Leaderboard!\n+"+"-"*16+"+")
    for i in leaderboard:
        print("|{0:<10}: {1:>4}|".format("{:.10}".format(i[1]),"{:.4}".format(str(i[0]))))
    print("+"+"-"*16+"+")
timer=10

#Turtle Setup

wn=turtle.Screen()
wn.title("SnakeFacts")
wn.setup(width=600, height=600)

head=turtle.Turtle()
head.st()
head.shapesize(0.5)
head.pensize(10)
head.speed(0)
head.shape("square")
head.color("black")
head.pendown()
head.goto(0,0)
head.boosting=False
head.leaving=False
head.hs=0

food=turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("square")
food.penup()
food.goto(0,100)
canvas=wn.getcanvas()
foodid = canvas.find_overlapping(food.xcor(),-food.ycor(),food.xcor(),-food.ycor())[0]

def scorefact(num,high="s"):
    try:
        response=requests.get("http://numbersapi.com/{}?json".format(num)).json()
        text=response["text"].replace(str(num),"Your high score" if high=="hs" else "Your score")
    except:
        text=("Your session high score is "+str(num)) if high=="hs" else ("Your score is "+str(num))
    return linehalf(text)
def linehalf(string):
    lst=string.split()
    lst=["\n"+lst[x] if x%6==0 and x!=0 else lst[x] for x in range(len(lst))]
    return " ".join(lst).replace("e old","e on").replace("s of a","s in a")

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("blue")
pen.penup()
pen.ht()

boostpen=turtle.Turtle()
boostpen.speed(0)
boostpen.shape("square")
boostpen.color("blue")
boostpen.penup()
boostpen.ht()

#Main starts here. Yes it's recursive, and yes, there was probably a better way of doing this.

def main(hs):
    #ReSetup
    timer=10
    foodtimer=50
    score=0
    head.hs=hs
    boosts=0
    wn.listen()
    def left():
        head.lt(45)
        head.fd(5)
    def right():
        head.rt(45)
        head.fd(5)
    def boost():
        head.boosting=True
    def leave():
        head.leaving=True
    wn.onkeypress(left,"Left")
    wn.onkeypress(right,"Right")
    wn.onkeypress(boost,"Up")
    wn.onkeypress(leave,"Escape")
    pen.clear()
    pen.goto(0,200)
    pen.write(scorefact(score)+" ("+str(score)+")",align="center",font=("consolas", 12, "bold"))
    pen.goto(0,0)
    pen.write(scorefact(head.hs,"hs")+" ("+str(head.hs)+")",align="center",font=("consolas", 12, "bold"))
    boostpen.clear()
    boostpen.goto(0,-200)
    boostpen.write("You have "+str(boosts)+(" boost!" if boosts==1 else " boosts!"),align="center",font=("consolas", 12, "bold"))

    #Enter Gameloop

    while True:
        head.fd(5)
        if head.boosting and boosts>=1:
            head.boosting=False
            boosts-=1
            head.penup()
            timer=10
            boostpen.clear()
            boostpen.goto(0,-200)
            boostpen.write("You have "+str(boosts)+(" boost!" if boosts==1 else " boosts!"),align="center",font=("consolas", 12, "bold"))
        if not timer<=0: timer-=1
        else: head.pendown()

        #Collision ughhhh
        canvas=wn.getcanvas()
        overlapping = canvas.find_overlapping(head.xcor(),-head.ycor(),head.xcor(),-head.ycor())
        if head.isdown():
            head.penup()
            head.pendown()
        if len(overlapping)>=4 and not foodid in overlapping:
            if len(overlapping)>=5:
                break
        if foodid in overlapping:
            food.goto(random.randint(0,600)-300,random.randint(0,600)-300)
            score+=1
            boosts+=1
            if head.hs<score: head.hs=score
            pen.clear()
            pen.goto(0,200)
            pen.write(scorefact(score)+" ("+str(score)+")",align="center",font=("consolas", 12, "bold"))
            pen.goto(0,0)
            pen.write(scorefact(head.hs,"hs")+" ("+str(head.hs)+")",align="center",font=("consolas", 12, "bold"))
            boostpen.clear()
            boostpen.goto(0,-200)
            boostpen.write("You have "+str(boosts)+" boosts!",align="center",font=("consolas", 12, "bold"))
        if foodtimer==0:
            foodtimer=25
            food.fd(25)
            exec(random.choice(["food.lt(90)","food.rt(90)"]))
            if abs(food.xcor())>=300: food.goto(food.xcor()*(-0.8),food.ycor())
            if abs(food.ycor())>=300: food.goto(food.xcor(),food.ycor()*(-0.8))
        if abs(head.xcor())>=300:
            head.penup()
            head.goto(head.xcor()*(-0.99),head.ycor())
            head.pendown()
        if abs(head.ycor())>=300:
            head.penup()
            head.goto(head.xcor(),head.ycor()*(-0.99))
            head.pendown()
        foodtimer-=1
        if head.leaving:
            with open("highscore.json", "r") as file:
                scoredict=json.load(file)
                minname=list(scoredict.keys())[list(scoredict.values()).index(min(scoredict.values()))]
            if head.hs>scoredict[minname]:
                print("\nYou have made it to the leaderboard!\n")
                name=input("Enter your name: ")
                if name in scoredict: del scoredict[name]
                else: del scoredict[minname]
                scoredict[name]=head.hs
                with open("highscore.json", "w") as file:
                    json.dump(scoredict,file)
            wn.bye()
            sys.exit()
    head.clear()
    main(head.hs)
main(head.hs)
