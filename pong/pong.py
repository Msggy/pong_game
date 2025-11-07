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
        if keys_pressed[K_UP] and self.rect.y >= 20:
            self.rect.y -= 10
        if keys_pressed[K_DOWN] and self.rect.y <= 400:
            self.rect.y += 10
    
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 20:
            self.rect.y -= 10
        if keys_pressed[K_s] and self.rect.y <= 400:
            self.rect.y += 10
    
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




#sprites
player_r = Player("Bars.png", 600, 200, 10)
player_l = Player("Bars.png", 20, 200, 10)
ball = Ball("Ball.png", 150, 200, 5)
while game:
    janela.blit(background, (0, 0))  # Must include coordinates!
    ball.reset()
    ball.update()
    player_r.update_r()
    player_r.reset()
    player_l.update_l()
    player_l.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
