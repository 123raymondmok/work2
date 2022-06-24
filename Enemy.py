
from random import randrange
import pygame
import os


width, height = 100,100
#Loading Enemy Ship Images
SpaceShip1 = pygame.image.load(os.path.join("images/ship (1).png"))
SpaceShip2 = pygame.image.load(os.path.join("images/ship (2).png"))
SpaceShip3 = pygame.image.load(os.path.join("images/ship (3).png"))
SpaceShip4 = pygame.image.load(os.path.join("images/ship (4).png"))
SpaceShip6 = pygame.image.load(os.path.join("images/ship (6).png"))
SpaceShip7 = pygame.image.load(os.path.join("images/ship (7).png"))
SpaceShip8 = pygame.image.load(os.path.join("images/ship (8).png"))
SpaceShip9 = pygame.image.load(os.path.join("images/ship (9).png"))
SpaceShip10 = pygame.image.load(os.path.join("images/ship (10).png"))
SpaceShip11 = pygame.image.load(os.path.join("images/ship (11).png"))
SpaceShip12 = pygame.image.load(os.path.join("images/ship (12).png"))
SpaceShip13 = pygame.image.load(os.path.join("images/ship (13).png"))
SpaceShip14 = pygame.image.load(os.path.join("images/ship (14).png"))
SpaceShip15 = pygame.image.load(os.path.join("images/ship (15).png"))
SpaceShip16 = pygame.image.load(os.path.join("images/ship (16).png"))

#Code for Enemy Ships
class Enemy(pygame.sprite.Sprite):
  SPAWN_RATE = 20
  until_spawn = SPAWN_RATE
  def spawn(image, group, screen):
    enemy = Enemy(image)
    
    enemy.set_position(screen.get_width(), randrange(screen.get_height()))
    group.add(enemy)
  def __init__(self, image):
    pygame.sprite.Sprite.__init__(self)
    self.speed = 10
    self.image = image
    self.size = self.image.get_size()
    self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.25), int(self.size[1]*0.25)))
    self.image = pygame.transform.rotate(self.image, 90)
    self.rect = self.image.get_rect()
  def draw(self, screen):
    screen.blit(self.image)
  def update(self):
    self.rect.x -= self.speed
  
  def set_position(self, X, Y):
    self.rect.center = (X, Y)
    
   
def battle(player, enemy):
    print ("An enemy {0.name} appears...".format(enemy))
    # Combat loop
    while player.health > 0 and enemy.health > 0:
        player.attack(enemy)
        print("The health of the {0.name} is now {0.health}.".format(enemy))
        if enemy.health <= 0:
            break
        enemy.attack(player)
        print("Your health is now {0.health}.".format(player))
    # Display outcome
    if player.health > 0:
        print("You killed the {0.name}.".format(enemy))
    elif enemy.health > 0:
        print("The {0.name} killed you.".format(enemy))
























