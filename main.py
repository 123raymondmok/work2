import pygame
from Background import Background
import Enemy
import Player

from random import randrange
clock = pygame.time.Clock()
FPS = 60


#creatspawn_rate=600e game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 432
run=True

points = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Parallax")

background = Background()

 
# set the center of the rectangular object.

enemy_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()
enemy_laser_group = pygame.sprite.Group()
player = Player.Player(SCREEN_WIDTH, SCREEN_HEIGHT,laser_group) 
while run:
  clock.tick(FPS)

  background.scroll += 5
  if Enemy.Enemy.until_spawn > 0:
    Enemy.Enemy.until_spawn -= 1 
  else: 
    Enemy.Enemy.spawn(Enemy.SpaceShip1,enemy_group, screen)
    Enemy.Enemy.until_spawn = Enemy.Enemy.SPAWN_RATE
    
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False

  
  background.draw(screen)
  enemy_group.draw(screen)
  laser_group.draw(screen)
  laser_group.update()
  player.draw(screen)
  player.update()
  enemy_group.update() 
  pygame.display.update()
  
  

  