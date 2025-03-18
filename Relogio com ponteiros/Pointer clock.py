import turtle

# Configuração da tela
screen = turtle.Screen()
screen.bgcolor("black")  # Fundo preto
screen.setup(width=600, height=600)
screen.title("Relógio Analógico Estático")

# Criação do desenho do relógio
relogio = turtle.Turtle()
relogio.hideturtle()
relogio.speed(0)
relogio.pensize(3)

def desenhar_relogio(h, m, s):
    # Desenha o círculo do relógio
    relogio.penup()
    relogio.goto(0, -210)
    relogio.setheading(0)
    relogio.pencolor("gold")  # Cor dourada para o círculo
    relogio.pendown()
    relogio.circle(210)

    # Desenha os números do relógio
    relogio.penup()
    relogio.goto(0, 0)
    relogio.setheading(90)
    relogio.pencolor("gold")  # Cor dourada para os números
    for i in range(12):
        relogio.fd(190)
        relogio.pendown()
        relogio.write(str(i + 1), align="center", font=("Arial", 12, "bold"))
        relogio.penup()
        relogio.goto(0, 0)
        relogio.rt(30)

    # Desenha o ponteiro das horas
    relogio.penup()
    relogio.goto(0, 0)
    relogio.setheading(90)
    relogio.rt(h * 30 + m * 0.5)  # 30 graus por hora + 0.5 graus por minuto
    relogio.pendown()
    relogio.pencolor("gold")  # Cor dourada para o ponteiro das horas
    relogio.pensize(5)  # Espessura do ponteiro
    relogio.fd(80)

    # Desenha o ponteiro dos minutos
    relogio.penup()
    relogio.goto(0, 0)
    relogio.setheading(90)
    relogio.rt(m * 6)  # 6 graus por minuto
    relogio.pendown()
    relogio.pencolor("gold")  # Cor dourada para o ponteiro dos minutos
    relogio.pensize(4)  # Espessura do ponteiro
    relogio.fd(120)

    # Desenha o ponteiro dos segundos
    relogio.penup()
    relogio.goto(0, 0)
    relogio.setheading(90)
    relogio.rt(s * 6)  # 6 graus por segundo
    relogio.pendown()
    relogio.pencolor("red")  # Cor vermelha para o ponteiro dos segundos
    relogio.pensize(2)  # Espessura do ponteiro
    relogio.fd(150)

# Defina a hora que deseja exibir (formato 24 horas)
hora = 14  # 2 PM
minuto = 30
segundo = 45

# Desenha o relógio com a hora definida
desenhar_relogio(hora % 12, minuto, segundo)

# Finaliza
turtle.done()