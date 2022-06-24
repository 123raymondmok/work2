import pygame

class PlayerWeapon (pygame.sprite.Sprite):
  
  def __init__(self, x,y,play_sound=True):
    #self.sound=pygame.sounds.load('sounds/Laser_sound1.ogg')
    #if play_sound:
      #self.sound.play()
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("images/Laser_bullet.png")
    self.vx=10                                                                                          
    
    self.rect=self.image.get_rect()
    
    self.size = self.image.get_size()
    self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.25), int(self.size[1]*0.25)))
    self.rect.center=(x+self.size[0]*0.5,y+self.size[1]*0.5)
  def draw(self,surface):
    surface.blit(self.image, (self.rect.x,self.rect.y))
    
  def update(self):
    self.rect.x += self.vx
    
    
