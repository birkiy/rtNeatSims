import pygame
import time


class Stage:
    def __init__(self):
        pygame.init()
        self.init_time = time.time()
        self.prev_time = self.init_time


    def set_window(self, width, height):
        self.width = width
        self.height = height
        screen = pygame.display.set_mode((width, height))

    def loop(self):
        current_time = time.time()
        delta_time = current_time - self.prev_time
        self.fps = 1 // delta_time


        self.prev_time = current_time
        pass

    def close(self):
        self.running = False
        pygame.quit()
