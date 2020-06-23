import pygame

from visual import colors
from objects.sim import Sim
from objects.framerate import Framerate

class Stage:
    def __init__(self):
        pygame.init()
        self.objects = []
        self.objects.append(Framerate(self))

    def set_font(self, font, size):
        self.font = pygame.font.Font(font, size)

    def add_sim(self):
        self.objects.append(Sim(self))

    def set_framerate(self, framerate):
        self.clock = pygame.time.Clock()
        self.framerate = framerate

    def set_window(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))

    def start(self):
        self.running = True
        while self.running:
            self.screen.fill(colors.white)
            self.deltatime = self.clock.tick(self.framerate)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for object in self.objects:
                            object.on_mouse_down(event)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        for object in self.objects:
                            object.on_mouse_up(event)

            for object in self.objects:
                object.loop()

            pygame.display.update()
        pygame.quit()
