# gpu.py

import pygame

class GPU:
    def __init__(self):
       
        pygame.init()
        self.screen = pygame.display.set_mode((160, 144))  

    def render(self, memory):
        
        
        self.screen.fill((0, 0, 0))  

        
        pygame.display.flip()
