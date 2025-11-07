from pygame import *
from random import randint

janela = display.set_mode((700, 500))
display.set_caption("Pong")

# Load and scale the background properly
background = transform.scale(image.load("Background.png"), (700, 500))

game = True
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, pimage, x, y, speed):
        super.__init__()
        self.image = transform.scale(image.load(pimage), (80, 80))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        janela.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            self.rect.y -= 10
        if keys_pressed[K_DOWN]:
            self.rect.y += 10
    
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -= 10
        if keys_pressed[K_s]:
            self.rect.y += 10
    
#sprites


while game:
    janela.blit(background, (0, 0))  # Must include coordinates!

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
