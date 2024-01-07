import pygame

pygame.init()

screen_size = pygame.display.set_mode((800, 600), 0)

magenta = (255, 0, 255)
yellow = (255, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
speed = 1

class scenario:
    def __init__(self, size):
        self.size = size
        self.matrix = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]
    def paint_row(self, screen, number_row, row):
        for number_column, column in enumerate(row):
            x = number_column * self.size
            y = number_row * self.size
            half = self.size // 2
            color = black
            if column == 2:
                color = blue
            pygame.draw.rect(screen, color, (x,y, self.size, self.size),0)
            if column == 1:
                pygame.draw.circle(screen, yellow, (x + half, y + half), self.size // 10,0)
                
    def paint(self, screen):
        for number_row, row in enumerate(self.matrix):    
            self.paint_row(screen, number_row, row)
    


class pacman:
    def __init__(self, size):
        self.column = 1
        self.row = 1
        self.center_x = 400
        self.center_y = 300 
        self.size = size
        self.speed_x = 0
        self.speed_y = 0
        self.radius = self.size // 2
        
    def calculate_rules(self):
        self.column = self.column + self.speed_x 
        self.row = self.row + self.speed_y
        self.center_x = int(self.column * self.size + self.radius)
        self.center_y = int(self.row * self.size + self.radius)
        
        if self.center_x + self.radius > 800:
            self.speed_x = -1 
        if self.center_x - self.radius < 0:
            self.speed_x = 1
        if self.center_y + self.radius > 600:
            self.speed_y = -1
        if self.center_y - self.radius < 0:
            self.speed_y = 1
        
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
        
    def processing_events(self, events):
        for i in events:
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_RIGHT:
                    self.speed_x = speed
                elif i.key == pygame.K_LEFT:
                    self.speed_x = -speed
                elif i.key == pygame.K_UP: 
                    self.speed_y = -speed
                elif i.key == pygame.K_DOWN:
                    self.speed_y = speed     
            elif i.type == pygame.KEYUP:
                if i.key == pygame.K_RIGHT:
                        self.speed_x = 0
                elif i.key == pygame.K_LEFT: 
                    self.speed_x = 0
                elif i.key == pygame.K_UP: 
                    self.speed_y = 0
                elif i.key == pygame.K_DOWN:
                    self.speed_y = 0
                      
    def processing_events_mouse(self, events):
        delay = 100
        for i in events:
            if i.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = i.pos 
                self.column = (mouse_x - self.center_x) / delay
                self.row = (mouse_y - self.center_y) / delay
                              
    
if __name__ == "__main__":
    size = 600 // 30
    pacman = pacman(size)
    scenario = scenario(size)
    
    while True:
        
        # Calculete Rules
        pacman.calculate_rules()
        
        # Screen Paint
        screen_size.fill(black)
        scenario.paint(screen_size)
        pacman.paint(screen_size)
        pygame.display.update()
        pygame.time.delay(100)
        
        # Catch event
        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT:
                exit()
            pacman.processing_events(events)
                