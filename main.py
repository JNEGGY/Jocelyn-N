import turtle

screen=turtle.Screen()
screen.screensize(200,200)
screen.bgcolor("White")

t=turtle.Turtle()
t2=turtle.Turtle()
t2.hideturtle()
t2.penup()
t.fillcolor("Pink")
t.begin_fill()
t.pencolor("Black")
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.left(45)
t.end_fill()
t.penup()
t.goto(0,200)
t.pendown()
t.write("Jocelyn N slides", font=("arial", 30, "bold"), align = "center")

turtle.addshape("intropic.gif")
t2.goto(-100,0)
t2.shape("intropic.gif")
a = t2.stamp()
t2.goto(-100,0)

turtle.addshape("intropic2.gif")
t2.goto(150,0)
t2.shape("intropic2.gif")
a = t2.stamp()
t2.goto(100,0)

enter=input("Press Enter to continue:")
t.clear()
t2.clearstamps()

screen.bgcolor("Blue")
t.clear()
t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(0)
t.penup()
t=turtle.Turtle()
t.fillcolor("LightBlue")
t.begin_fill()
t.pencolor("white")
t.circle(40)
t.left(45)
t.end_fill()
t.penup()
t.goto(0,200)
t.pendown()
t.write("Favorite Food", font=("arial", 30, "bold"), align = "center")
t.penup()
t.goto(0,-200)
t.pendown()
t.write("Tacos, Pizza, Mazzarella Sticks", font=("arial", 30, "bold"), align = "center")

turtle.addshape("tacobell.gif")
t2.goto(150,0)
t2.shape("tacobell.gif")
a = t2.stamp()
t2.goto(-100,0)

turtle.addshape("pizza.gif")
t2.goto(150,0)
t2.shape("pizza.gif")
a = t2.stamp()
t2.goto(100,0)

enter=input("Press Enter to continue:")
t.clear()
t2.clearstamps()

screen.bgcolor("Red")

t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(0)
t.penup()

t=turtle.Turtle()
t.fillcolor("Pink")
t.begin_fill()
t.pencolor("white")
t.forward(25)
t.left(90)
t.forward(50)
t.left(90)
t.forward(25)
t.left(90)
t.forward(50)
t.left(90)
t.left(45)
t.end_fill()
t.penup()
t.goto(0,200)
t.pendown()
t.write("Hobbies", font=("arial", 30, "bold"), align = "center")
t.penup()
t.goto(0,-200)
t.pendown()
t.write("Sleeping,Eating,Hanging out with friends, Playing Fortnite", font=("arial", 15, "bold"), align = "center")

turtle.addshape("fortnite.gif")
t2.goto(-100,0)
t2.shape("fortnite.gif")
a = t2.stamp()
t2.goto(-100,0)

turtle.addshape("sleeping.gif")
t2.goto(150,0)
t2.shape("sleeping.gif")
a = t2.stamp()
t2.goto(100,0)


enter=input("Press Enter to continue:")
t.clear()
t2.clearstamps()

screen.bgcolor("Orange")

t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(0)
t.penup()

t=turtle.Turtle()
t.pencolor("Black")
t.fillcolor("White")
t.begin_fill()
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.end_fill()
t.penup()
t.goto(0,200)
t.pendown()
t.write("Favorite Movie", font=("arial", 30, "bold"), align = "center")
t.penup()
t.goto(0,-200)
t.pendown()
t.write("10 Things I Hate About You", font=("arial", 30, "bold"), align = "center")

turtle.addshape("movie.gif")
t2.goto(-100,0)
t2.shape("movie.gif")
a = t2.stamp()
t2.goto(-100,0)

turtle.addshape("movie2.gif")
t2.goto(150,0)
t2.shape("movie2.gif")
a = t2.stamp()
t2.goto(100,0)


enter=input("Press Enter to continue:")
t.clear()
t2.clearstamps()

screen.bgcolor("Green")

t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(0)
t.penup()

t=turtle.Turtle()
t.fillcolor("LightGreen")
t.begin_fill()
t.pencolor("white")
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.penup()
t.goto(0,200)
t.left(45)
t.end_fill()
t.pendown()
t.write("Favorite Sport", font=("arial", 30, "bold"), align = "center")
t.penup()
t.goto(0,-200)
t.pendown()
t.write("Badminton", font=("arial", 30, "bold"), align = "center")

turtle.addshape("Badmittion.gif")
t2.goto(-100,0)
t2.shape("Badmittion.gif")
a = t2.stamp()
t2.goto(-100,0)

turtle.addshape("badmittion2.gif")
t2.goto(150,0)
t2.shape("badmittion2.gif")
a = t2.stamp()
t2.goto(100,0)


enter=input("Press Enter to continue:")
t.clear()
t2.clearstamps()

