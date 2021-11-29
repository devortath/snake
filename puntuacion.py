from turtle import Turtle

ALINEACION = "center"
FUENTE = ("Courier", 16, "normal")


class Puntuacion(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.actualizar_puntuacion()
        self.hideturtle()

    def actualizar_puntuacion(self):
        self.write(f"Puntuación: {self.score}", align=ALINEACION, font=FUENTE)

    def incrementar_puntuacion(self):
        self.score += 1
        self.clear()
        self.actualizar_puntuacion()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALINEACION, font=FUENTE)
