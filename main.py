from turtle import Screen
from snake import Snake
from food import Food
from puntuacion import Puntuacion
import time

pantalla = Screen()
pantalla.setup(600, 600)
pantalla.bgcolor("black")
pantalla.title("Snake")
# Desactivar animación de pantalla para que se vea la animación fluida
pantalla.tracer(0)

snake = Snake()
food = Food()
puntuacion = Puntuacion()

jugando = True
pantalla.listen()
pantalla.onkey(snake.up, "Up")
pantalla.onkey(snake.down, "Down")
pantalla.onkey(snake.right, "Right")
pantalla.onkey(snake.left, "Left")

while jugando:
    pantalla.update()
    time.sleep(0.1)
    snake.mover_serpiente()

    # Detectando colision con la comida
    if snake.cabeza.distance(food) < 15:
        food.refresh()
        puntuacion.incrementar_puntuacion()
        snake.extender()

    # Detectar colision con la pared
    if (
        snake.cabeza.xcor() > 290
        or snake.cabeza.xcor() < -290
        or snake.cabeza.ycor() > 290
        or snake.cabeza.ycor() < -290
    ):
        jugando = False
        puntuacion.game_over()

    # Detectar colision con la serpiente
    for segmento in snake.segmentos[1:]:
        if snake.cabeza.distance(segmento) < 5:
            jugando = False
            puntuacion.game_over()


pantalla.exitonclick()
