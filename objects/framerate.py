from visual import colors
from objects.object import Object

class Framerate(Object):
    def __init__(self, stage):
        self.stage = stage

    def loop(self):
        text = self.stage.font.render(f'FPS: {round(self.stage.clock.get_fps())}', True, colors.black)
        textRect = text.get_rect()
        self.stage.screen.blit(text, textRect)
        pass
