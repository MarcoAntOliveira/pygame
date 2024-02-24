import pygame #type:ignore
from constantes import AMARELO, TAMANHO_TELA, PRETO
from desenhos import Screen

#pygame.init()
#tela = pygame.display.set_mode(TAMANHO_TELA, 0)
tela = Screen()
tela.inicializa_tela
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
    tela.pinta_preto
    tela.draw_circle(AMARELO, (int(x), 240), 30, 0)
    tela.update_tela

    #eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()