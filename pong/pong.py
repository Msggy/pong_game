from pygame import *
from random import randint

janela = display.set_mode((700, 500))
display.set_caption("catch-up")

# Load and scale the background properly
background = transform.scale(image.load("Background.png"), (700, 500))

game = True
clock = time.Clock()
FPS = 60

#Classes
class GameSprite(sprite.Sprite):
    def __init__(self, speed, player_image,y,x):
        self.speed = speed
        self.image = transform.scale(image.load(player_image),(30,30))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def reset(self):
        janela.blit(self.image,(self.rect.x,self.rect.y))

class Ball(GameSprite):
    directionx = "left"
    directiony = "left"
    def update(self):

        if self.rect.x <= 0:
            self.directionx = "right"

        if self.rect.x >= 700:
            self.directionx = "left"


        if self.rect.y <= 0:
            self.directiony = "right"

        if self.rect.y >= 500:
            self.directiony = "left"

        if self.directionx == "left":
           self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.directiony == "left":
           self.rect.y -= self.speed
        else:
            self.rect.y += self.speed




    
ball = Ball(10,"Ball.png",150,200)
while game:
    janela.blit(background, (0, 0))  # Must include coordinates!
    ball.reset()
    ball.update()
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
