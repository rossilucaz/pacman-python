
import pygame

magenta = (255, 0, 255)
black = (0, 0, 0)
speed = 1
radius = 30

pygame.init()

screen = pygame.display.set_mode((640, 480), 0)

x = 10 
y = 10
speed_x = speed
speed_y = speed
   
while True:
    # Calcula as Regras
    x = x + speed_x
    y = y + speed_y
    
    if x + radius > 640:
        speed_x = -speed
    if x - radius < 0:
        speed_x = speed
        
    if y + radius > 480:
        speed_y = -speed
    if y + radius < 0:
        speed_y = speed
    
        
        
        
    # Pinta
    screen.fill(black)
    
    pygame.draw.circle(screen, magenta,(int(x), int(y)), radius, 0)
    pygame.display.update()
    
    
    # Eventos
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()