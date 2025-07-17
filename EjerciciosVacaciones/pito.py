import turtle

# Configuración inicial
pantalla = turtle.Screen()
pantalla.bgcolor("white")
t = turtle.Turtle()
t.speed(3)

radio = 50
altura_torre = 300

def dibujar_circulo(x, y):
    t.penup()
    t.goto(x, y - radio)
    t.pendown()
    t.circle(radio)

def dibujar_torre(x, y, ancho, alto):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(2):
        t.forward(ancho)
        t.left(90)
        t.forward(alto)
        t.left(90)

# Dibujar bolitas (dos círculos)
dibujar_circulo(-radio, 0)      # izquierda
dibujar_circulo(radio, 0)       # derecha

# Dibujar torre (rectángulo con base del mismo tamaño que los círculos)
torre_ancho = 2 * radio
torre_x = -radio
torre_y = 0
dibujar_torre(torre_x, torre_y, torre_ancho, altura_torre)

t.hideturtle()
pantalla.mainloop()
