
import pygame

pygame.init()

tela = pygame.display.set_mode((640, 480), 0)
mageta = (0, 255, 0)

while True:
    # Calcula as Regras
    
    # Pinta
    pygame.draw.circle(tela, mageta,(320, 240), 50, 0)
    pygame.display.update()
    
    
    # Eventos
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()