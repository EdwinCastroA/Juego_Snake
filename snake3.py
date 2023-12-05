import turtle
import time
import random

# Configuración de la ventana
turtle.title("Juego de la Serpiente")
turtle.bgcolor("lime green")
turtle.setup(width=600, height=600)
turtle.tracer(0)

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.shape("square")
cabeza.color("white")
cabeza.speed(0)
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "Stop"

# Comida
comida = turtle.Turtle()
comida.shape("circle")
comida.color("red")
comida.speed(0)
comida.penup()
comida.goto(0, 100)

#comida2
comida2 = turtle.Turtle()
comida2.shape("square")
comida2.color("blue")
comida2.speed(0)
comida2.penup()
comida2.goto(-150, -130)








# Cuerpo de la serpiente
segmentos = []

# Puntuación
puntuacion = 0

# Funciones de movimiento
def arriba():
    cabeza.direction = "Up"

def abajo():
    cabeza.direction = "Down"

def izquierda():
    cabeza.direction = "Left"

def derecha():
    cabeza.direction = "Right"

# Función de movimiento
def mover():
    if cabeza.direction == "Up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "Down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "Left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "Right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# Teclado
turtle.listen()
turtle.onkey(arriba, "w")
turtle.onkey(abajo, "s")
turtle.onkey(izquierda, "a")
turtle.onkey(derecha, "d")

# Función principal del juego
while True:
    turtle.update()

    # Colisiones con la pared
    if cabeza.xcor() > 290 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "Stop"

        # Ocultar segmentos
        for segmento in segmentos:
            segmento.goto(1000, 1000)

    

        # Limpiar la lista de segmentos
        segmentos.clear()

        # Reiniciar la puntuación
        puntuacion = 0

    # Colisiones con la comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        comida.goto(x, y)

        # Agregar segmento
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("gray")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        # Incrementar la puntuación
        puntuacion += 1


    elif cabeza.distance(comida2) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        comida2.goto(x, y)

    # Agregar dos segmentos
        for _ in range(2):
            nuevo_segmento = turtle.Turtle()
            nuevo_segmento.speed(0)
            nuevo_segmento.shape("square")
            nuevo_segmento.color("gray")
            nuevo_segmento.penup()
            segmentos.append(nuevo_segmento)

        # Incrementar la puntuación
        puntuacion += 2




    # Mover el cuerpo de la serpiente
    total_segmentos = len(segmentos)
    for index in range(total_segmentos - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    # Mover el primer segmento a la posición de la cabeza
    if total_segmentos > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    # Llamada a la función de movimiento
    mover()

    # Colisiones con el cuerpo
    for segmento in segmentos:
        if cabeza.distance(segmento) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "Stop"

            # Ocultar segmentos
            for segmento in segmentos:
                segmento.goto(1000, 1000)

            # Limpiar la lista de segmentos
            segmentos.clear()

            # Reiniciar la puntuación
            puntuacion = 0

            


    # Mostrar la puntuación en la ventana
    turtle.clear()
    turtle.color("white")
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, 260)
    turtle.write("Puntuación: {}".format(puntuacion), align="center", font=("Courier", 24, "normal"))

    time.sleep(0.1)


    

    