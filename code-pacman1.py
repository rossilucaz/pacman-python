
import pygame

user_color = []
for i in range(3):
    color_user = int(input(f" Enter color{i+1}: "))
    if color_user == 0:
        color_user_default = [255, 0, 255]
        user_color.append(color_user)
    else:
        user_color.append(color_user_default)

magenta = (user_color[0], user_color[1], user_color[2])
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
    # Calculate Rules
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
    
    
    # Events
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()