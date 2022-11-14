import pygame
from random import randint
from settings import *
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #create player rect
        self.image = pygame.image.load('graphics/player/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (120,120))
        self.rect = self.image.get_rect()
        self.rect.center = (WIN_WIDTH //2,WIN_HEIGHT//2+150)
        self.proj_img = pygame.image.load('graphics/projectile/projectile1.png')
    

    def update(self):
        #display.blit(self.img, self.rect)
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0] - self.image.get_width()//2
        #print(len(self.projectiles))



class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.image = surface
        self.rect = self.image.get_rect()
        #self.rect.midbottom= pos

        #self.x, self.y = pos.x, pos.y
        self.rect.midbottom = (pos.x + SHOOTER_OFFSET, pos.y)

    def update(self):
        #self.pos.y -= self.speed * dt
        self.rect.y -= PROJ_SPEED * 60
        #self.rect.y = round(self.y)
        #print(self.rect.y)
        #display.blit(self.image, self.rect)

        if self.rect.y <= -100:
            self.kill()

class asteroid(pygame.sprite.Sprite):
    def __init__(self, img):
        self.image = img
        self.rect = img.get_rect()
        self.speed = 0.2

        self.rect.x = randint(0, WIN_WIDTH)
        self.rect.y = 100
        
    def update(self):
        pass

class Button:
    def __init__(self, x, y, img, price, text=''):
        self.x, self.y = x, y
        self.original_img = pygame.image.load(img).convert_alpha()
        self.img = self.original_img
        self.price = price
        self.text = text

    def draw(self, display):
        #pygame.draw.rect(display,(self.x,self.y,8,8),0)
        display.blit(self.img, (self.x, self.y))
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            display.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
