from pygame import *
from random import randint

janela = display.set_mode((700, 500))
display.set_caption("catch-up")

# Load and scale the background properly
background = transform.scale(image.load("Background.png"), (700, 500))

game = True
clock = time.Clock()
FPS = 60

while game:
    janela.blit(background, (0, 0))  # Must include coordinates!

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
