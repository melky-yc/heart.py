import turtle
import math
import random
import time

# Configurações gerais
screen = turtle.Screen()  # Criação da tela
screen.setup(width=800, height=600)  # Define o tamanho da janela
screen.bgcolor("black")  # Define a cor de fundo
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Função para calcular as coordenadas do coração
def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y

# Função para obter pontos uniformemente distribuídos no contorno do coração
def ponto_uniforme():
    n = random.uniform(0, 2 * math.pi)  # Ângulo aleatório entre 0 e 2π
    x, y = corazon(n)
    return x * 20, y * 20  # Ajuste de escala

# Configurações das linhas
num_linhas = 500  # Quantidade de linhas
linhas = []  # Lista para armazenar as coordenadas das linhas

# Desenho do coração
for _ in range(num_linhas):
    t.color("red")
    t.pensize(random.randint(1, 3))
    
    # Gera dois pontos no contorno do coração
    x1, y1 = ponto_uniforme()
    x2, y2 = ponto_uniforme()
    
    # Verifica se os pontos estão no topo do coração
    if y1 > 0 and y2 > 0:
        # Se ambos os pontos estão no topo, não desenhe a linha
        continue
    
    # Salva as linhas para desaparecer depois
    linhas.append(((x1, y1), (x2, y2)))
    
    # Desenha a linha
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

# Pausa para visualização do coração completo
time.sleep(2)

# Finaliza o desenho
turtle.done()