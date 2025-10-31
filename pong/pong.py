from pygame import *
from random import randint

janela = display.set_mode((700, 500))
display.set_caption("catch-up")
janela.fill((255, 145, 227))

game = True
clock = time.Clock()
FPS = 60

while game:
    janela.fill((255, 145, 227))

    for e in event.get():
            if e.type == QUIT:
                game = False

    display.update()
    clock.tick(FPS)