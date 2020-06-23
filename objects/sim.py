from random import randint
import pygame

from objects.object import Object
from visual import colors

class Sim(Object):
    def __init__(self, stage):
        self.stage = stage
        self.rectangle = pygame.rect.Rect(
            randint(50, self.stage.width-50),
            randint(50, self.stage.height-50),
            20,
            20
        )
        self.selected = False

    def on_mouse_up(self, event):
        if self.rectangle.collidepoint(event.pos):
            self.selected = not self.selected
        else:
            self.selected = False

    def loop(self):
        if self.selected:
            pygame.draw.rect(self.stage.screen, colors.bright_green, self.rectangle)
        else:
            pygame.draw.rect(self.stage.screen, colors.bright_red, self.rectangle)

    def get_data(self):
        pass

    def add_data(self):
        pass
