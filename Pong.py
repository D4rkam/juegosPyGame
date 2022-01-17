import turtle

#================== VENTANA ==================#
ventana = turtle.Screen()
ventana.title("PONG By Thomas")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

#================== MARCADOR ==================#
marcadorA = 0
marcadorB = 0
#================== JUGADOR A ==================#
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350, 0)
jugadorA.shapesize(stretch_wid=5, stretch_len=1)

#================== JUGADOR B ==================#
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350, 0)
jugadorB.shapesize(stretch_wid=5, stretch_len=1)

#================== PELOTA ==================#
pelota = turtle.Turtle()
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.5
pelota.dy = 0.5

#================== LINEA DIVISION ==================#
division = turtle.Turtle()
division.color("white")
division.goto(0, 400)
division.goto(0, -400)

#================== DIBUJO MARCADOR ==================#
lapiz = turtle.Turtle()
lapiz.speed(0)
lapiz.color("white")
lapiz.penup()
lapiz.hideturtle()
lapiz.goto(0, 260)
lapiz.write("Jugador A: 0        Jugador B: 0", align="center", font=("Courier", 20 ,"normal"))

#================== FUNCIONES ==================#
def jugadorA_subir():
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)

def jugadorA_bajar():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)

def jugadorB_subir():
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)

def jugadorB_bajar():
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)

#================== TECLADO ==================#
ventana.listen()
ventana.onkeypress(jugadorA_subir, 'w')
ventana.onkeypress(jugadorA_bajar, 's')
ventana.onkeypress(jugadorB_subir, 'Up')
ventana.onkeypress(jugadorB_bajar, 'Down')

#================== BUCLE ACTUALIZADOR DE LA VENTANA ==================#
while True:
    ventana.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #Bordes Arriba y Abajo
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1
    
    #Bordes Derecha y Izquierda
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorA += 1
        lapiz.clear()
        lapiz.write("Jugador A: {}        Jugador B: {}".format(marcadorA, marcadorB), align="center", font=("Courier", 20 ,"normal"))

    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorB += 1
        lapiz.clear()
        lapiz.write("Jugador A: {}        Jugador B: {}".format(marcadorA, marcadorB), align="center", font=("Courier", 20 ,"normal"))

    #Paleta A
    if pelota.xcor() > 340 and pelota.xcor() < 350 and pelota.ycor() < jugadorB.ycor() + 50 and pelota.ycor() > jugadorB.ycor() -50:
        pelota.dx *= -1
    
    #Paleta B
    if pelota.xcor() < -340 and pelota.xcor() > -350 and pelota.ycor() < jugadorA.ycor() + 50 and pelota.ycor() > jugadorA.ycor() -50:
        pelota.dx *= -1
        