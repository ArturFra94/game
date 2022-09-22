#https://www.youtube.com/watch?v=XGf2GcyHPhc

import turtle

wn = turtle.Screen() #tworzenie okna
wn.title("Pong by Artur")
wn.bgcolor("black")
wn.setup(width=800, height=600) #ustawienia okna
wn.tracer() #zapobieganie aktualizacji okna, większa wydajność


#paddle A
paddle_a = turtle.Turtle() #male turtle to nazwa obiektu, Turtle oznacza nazwe klasy
paddle_a.speed(0) #prękośc wyświetlania animacji na ekranie
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(380,0)


#paddle B
paddle_b = turtle.Turtle() #male turtle to nazwa obiektu, Turtle oznacza nazwe klasy
paddle_b.speed(0) #prękośc wyświetlania animacji na ekranie
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(-380,0)

#Ball

ball = turtle.Turtle() #male turtle to nazwa obiektu, Turtle oznacza nazwe klasy
ball.speed(0) #prękośc wyświetlania animacji na ekranie
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2


#functions

def paddle_a_up():
    y = paddle_a.ycor() #ycor zwraca koordynaty aktualnego miejsca paddle_a
    y += 20
    paddle_a.sety(y) #przypisanie zmiennej y do paddle_a
def paddle_a_down():
    y = paddle_a.ycor() #ycor zwraca koordynaty aktualnego miejsca paddle_a
    y += -20
    paddle_a.sety(y) #przypisanie zmiennej y do paddle_a
def paddle_b_up():
    y = paddle_b.ycor() #ycor zwraca koordynaty aktualnego miejsca paddle_a
    y += 20
    paddle_b.sety(y) #przypisanie zmiennej y do paddle_a
def paddle_b_down():
    y = paddle_b.ycor() #ycor zwraca koordynaty aktualnego miejsca paddle_a
    y += -20
    paddle_b.sety(y) #przypisanie zmiennej y do paddle_a


# keyboard binding
wn.listen() # zczytanie z klawiatury
wn.onkeypress(paddle_a_up, "8") #gdy nacisnę y, wywołaj funkcje paddle_a_up
wn.onkeypress(paddle_a_down, "5") #gdy nacisnę y, wywołaj funkcje paddle_a_up
wn.onkeypress(paddle_b_up, "w") #gdy nacisnę y, wywołaj funkcje paddle_a_up
wn.onkeypress(paddle_b_down, "s") #gdy nacisnę y, wywołaj funkcje paddle_a_up

# Main game llop

while True:
    wn.update() #aktualizowanie okna non stop
    #turtle.exitonclick()
    #move the ball
    ball.setx(ball.xcor()  + ball.dx)
    ball.sety(ball.ycor()  + ball.dy)

    #border checking
    if ball.ycor() > 290: #jeśli koordynaty piłki będą w górnej krawędzi
        ball.sety(290) #ustal koordynaty piłki
        ball.dy *= -1 #odwróć kierunek ruchu
    if ball.xcor() > 390: #jeśli koordynaty piłki będą w górnej krawędzi
        ball.setx(390) #ustal koordynaty piłki
        ball.dx *= -1 #odwróć kierunek ruchu
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if (paddle_a.ycor() == ball.ycor() and
            paddle_a.xcor() == ball.xcor()):
        ball.dy *= -1
    if (paddle_b.ycor() == ball.ycor() and
            paddle_b.xcor() == ball.xcor()):
        ball.dy *= -1