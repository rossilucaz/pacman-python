import pygame

pygame.init()

screen_size = pygame.display.set_mode((800, 600), 0)

magenta = (255, 0, 255)
black = (0, 0, 0)

class pacman:
    def __init__(self):
        self.center_x = 400
        self.center_y = 300 
        self.size = 100
        self.radius = self.size // 2
        
    def paint(self, screen):
        # Draw Pacman body
        pygame.draw.circle(screen, magenta, (self.center_x, self.center_y), self.radius, 0)
        
        # Draw Pacman mouth
        corner_mouth = (self.center_x, self.center_y)
        upper_lip = (self.center_x + self.radius, self.center_y - self.radius)
        down_lip = (self.center_x + self.radius, self.center_y)
        points = [corner_mouth, upper_lip, down_lip]
        pygame.draw.polygon(screen, black, points, 0)
        
        # Pacman Eyes
        eyes_x = int(self.center_x + self.radius / 3)
        eyes_y = int(self.center_y - self.radius * 0.70)
        eyes_radius = int(self.radius / 10)
        pygame.draw.circle(screen, black, (eyes_x, eyes_y), eyes_radius, 0)
    
if __name__ == "__main__":
    pacman = pacman()
    
    while True:
        # Screen Paint
        pacman.paint(screen_size)
        pygame.display.update()
        
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()