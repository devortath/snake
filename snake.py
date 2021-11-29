from turtle import Turtle

POSICIONES_INICIALES = [(0, 0), (-20, 0), (-40, 0)]
DISTANCIA_MOVIMIENTO = 20
ARRIBA = 90
ABAJO = 270
IZQUIERDA = 180
DERECHA = 0


class Snake:
    def __init__(self):
        self.segmentos = []
        self.crear_serpiente()
        self.cabeza = self.segmentos[0]

    def anadir_segmento(self, posicion):
        """Creacion de los segmentos"""
        segmento = Turtle()
        segmento.shape("square")
        segmento.color("white")
        segmento.penup()
        segmento.goto(posicion)
        self.segmentos.append(segmento)

    def crear_serpiente(self):
        for posicion in POSICIONES_INICIALES:
            self.anadir_segmento(posicion)

    def mover_serpiente(self):
        """Movemos los segmentos de la serpiente, del último al primero, cambiando su posicion con el predecesor y movemos la cabeza hacia delante."""
        for i in range(len(self.segmentos) - 1, 0, -1):
            nueva_x = self.segmentos[i - 1].xcor()
            nueva_y = self.segmentos[i - 1].ycor()
            self.segmentos[i].goto(nueva_x, nueva_y)
        # adelantamos el primero
        self.cabeza.forward(DISTANCIA_MOVIMIENTO)

    def extender(self):
        """Añade un nuevo segmento a la serpiente"""
        self.anadir_segmento(self.segmentos[-1].position())

    def up(self):
        if self.cabeza.heading() != ABAJO:
            self.cabeza.setheading(ARRIBA)

    def down(self):
        if self.cabeza.heading() != ARRIBA:
            self.cabeza.setheading(ABAJO)

    def left(self):
        if self.cabeza.heading() != DERECHA:
            self.cabeza.setheading(IZQUIERDA)

    def right(self):
        if self.cabeza.heading() != IZQUIERDA:
            self.cabeza.setheading(DERECHA)
