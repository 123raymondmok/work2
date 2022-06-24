import pygame
class Background:
  def __init__(self):
    self.scroll = 0
    self.images = []
    for i in range(8):
      image = pygame.image.load(f"images/bkgd_{i}.png").convert_alpha()
      self.images.append(image)
    self.width = self.images[0].get_width()
  
  def draw(self, screen):
    width = screen.get_width()
    for x in range(5):
      speed = 1
      for i in self.images:
        offset = (self.scroll * speed) % width
        extra = width - offset + self.width
        if extra > 0:
          screen.blit(i, ( self.width + (x * self.width) - offset, 0))
          
        screen.blit(i, ((x * self.width) - offset, 0))
        speed += 0.2
