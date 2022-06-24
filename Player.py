import pygame
from Weapon import PlayerWeapon
class Player(pygame.sprite.Sprite):
  def __init__(self, width, height,laser_group):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('images/playership.png')
    self.rect = self.image.get_rect()
    
    self.rect.midleft = (0, height/2)
    self.movex = 0
    self.movey = 0
    self.speed = 10
    self.width = width
    self.height = height
    self.laser_group=laser_group
   
  def draw(self, surface):
    surface.blit(self.image, self.rect)

  def update(self):
    if pygame.key.get_pressed()[pygame.K_SPACE]:
      laser=PlayerWeapon(*self.rect.center)
      self.laser_group.add(laser)
      #event.wait()
    if pygame.key.get_pressed()[pygame.K_LEFT]:
      if self.rect.left > 0:
        self.rect.x -= self.speed
                         
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
      if self.rect.right < self.width - self.rect.width * 0.5:
        self.rect.x += self.speed

    if pygame.key.get_pressed()[pygame.K_UP]:
      if self.rect.center[1] > self.rect.height * 0.5:
        self.rect.y -= self.speed

    if pygame.key.get_pressed()[pygame.K_DOWN]:
      if self.rect.center[1] < self.height - self.rect.height * 1.5:
        self.rect.y += self.speed
    
    
     
