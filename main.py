import pygame, sys
from settings import *
from sprite import *


'''
Idea 3: *
reach for the sky will be maybe trying to launch player into another layer of 
space to reach their goals, and will end up becoming an endless scroller
-it being something like an old arcade space shooter is even more cliche

story element: trying to "shoot for the moon" (maybe actually trying to shoot the moon like gru)
will end up overshooting and now you have to shoot up asteroids and planets and stuff
probably includes a bunch of upgrades that can be collected from materials (contained in asteroids and stuff)
but each upgrade will take TIME and makes the ship VULNERABLE

should you use ur powers for good and do space exploration or hunt down earth?


make counter variable that when reaches a point it will activate some function?

make asteroids work by making timer, timer summons asteroids random y distance from top of 
screen, then amount of asteroids will be some percentage/float that is rounded
make asteroids into sprite group

add:
-setup constant projectile shooting
-add button classes that get darken after being clicked.
-health bar
-shields and other protections
-add star overlay which is the one that moves downward (while being copied again at the top) and spaceship stays still
-make different astroid groups (each group gives a chance of different loot)
-inventory for space rocks and their loot

-loot can be used for different upgrades
-asteroid belt stages are difficult nd have MASSIVE amounts of rock
'''


class Game:
    def __init__(self):

        #create game
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('Game')
        #create background
        self.bg_img = pygame.image.load('graphics/bg/space0.png').convert()
        self.bg_img = pygame.transform.rotozoom(self.bg_img,90, 1)
        self.bg_rect = self.bg_img.get_rect()
        self.bg_stars = pygame.image.load('graphics/bg/stars.png').convert_alpha()
        self.bg_stars = pygame.transform.rotozoom(self.bg_stars,90, 1)
        self.star_rect1 = self.bg_stars.get_rect()
        self.star_rect2 = self.bg_stars.get_rect()
        self.star_rect2.bottom = 0
        self.star_vel = 4

        #game vars
        self.all_sprites = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.buttons = []

        #timers
        self.NEW_SHOOT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.NEW_SHOOT, 2000)

        self.ASTEROID_TIMER = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ASTEROID_TIMER, 4000)

        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        #self.player = Player()

        self.buttons.append(Button(600, 200, 'graphics/Button/button1.png', 60))
        self.buttons.append(Button(600, 280, 'graphics/Button/button1.png', 60))
        self.buttons.append(Button(600, 360, 'graphics/Button/button1.png', 60))
    
    def create_stars(self):
        if self.star_rect1.top >= WIN_HEIGHT:
            self.star_rect1.bottom = 0
        if self.star_rect2.top >= WIN_HEIGHT:
            self.star_rect2.bottom = 0
        
        self.star_rect1.bottom += self.star_vel
        self.star_rect2.bottom += self.star_vel

        self.display.blit(self.bg_stars, self.star_rect1)
        self.display.blit(self.bg_stars, self.star_rect2)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == self.NEW_SHOOT:
                    #print('shoot')
                    #self.player.shoot()
                    self.projectiles.add(Projectile(self.player.sprite.rect, self.player.sprite.proj_img))

            #display background
            self.display.blit(self.bg_img, self.bg_rect)
            self.create_stars()            
            
            #self.player.update(self.display)
            self.player.update()
            self.projectiles.update()
            self.projectiles.draw(self.display)
            self.player.draw(self.display)

            for button in self.buttons:
                button.draw(self.display)

            

            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()