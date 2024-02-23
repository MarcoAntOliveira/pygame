import pygame #type:ignore
from constantes import AMARELO, TAMANHO_TELA, PRETO
from desenhos import draw_circle

pygame.init()
tela = pygame.display.set_mode(TAMANHO_TELA, 0)
x = 10
vel_x =0.1
while True:
    #calcula  regras
    x += vel_x
    if x > 640:
      vel_x = -0.1
    elif x < 0:
        vel_x = 0.1

     
    #pinta
    tela.fill(PRETO)
    draw_circle(tela, AMARELO, (int(x), 240), 30, 0)
    pygame.display.update()

    #eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()