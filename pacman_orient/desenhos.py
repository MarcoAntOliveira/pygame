import pygame #type:ignore
from constantes import PRETO
class Actor:
     def __init__(self) -> None:
          pass



class Screen(pygame.surface.Surface):
     def __init__(self, *args, **kwargs):
          super.__init__(*args, **kwargs)
          self.tamanho = (640, 480)
          self.centro_tela = (320, 240)
          
     def inicializa_tela(self):
          pygame.init()
          pygame.display.set_mode(self.tamanho, 0)     
     def pinta_preto(self, PRETO):
          self.fill(PRETO)
     def update_tela(self):
          pygame.display.update()

     def draw_circle(self, cor, pos, raio, pixels ):
          return pygame.draw.circle(self, cor, pos, raio, pixels)