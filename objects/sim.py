from random import randint
import pygame

from objects.object import Object
from visual import colors

class Sim(Object):
    def __init__(self, stage):
        self.stage = stage
        self.pos = (0, 0)
        self.rectangle = pygame.rect.Rect(
            self.pos[0],
            self.pos[1],
            20,
            20
        )
        self.selected = False

    def on_mouse_down(self, event):
        if self.rectangle.collidepoint(event.pos):
            self.stage.dragging = False

    def on_mouse_up(self, event):
        if self.rectangle.collidepoint(event.pos) and not self.stage.dragging:
            self.selected = not self.selected
        else:
            self.selected = False

    def loop(self):
        self.pos = self.stage.rel_pos(0, 0)
        self.rectangle = pygame.rect.Rect(
            self.pos[0],
            self.pos[1],
            20,
            20
        )
        if self.selected:
            pygame.draw.rect(self.stage.screen, colors.bright_green, self.rectangle)
        else:
            pygame.draw.rect(self.stage.screen, colors.bright_red, self.rectangle)

    def get_data(self):
        self.speed = 1
        self.rotation = 0
        pass

    def set_data(self):
        pass
