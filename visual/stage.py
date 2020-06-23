import pygame

from visual import colors


class Stage:
    def __init__(self):
        pygame.init()
        self.objects = []

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

            for object in self.objects:
                object.loop()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
