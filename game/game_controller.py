import pygame
import sys

import utils
import config

class GameController(object):
    def __init__(self, caption):
        pygame.init() #pylint: disable=E1101

        self.screen = pygame.display.get_surface()
        self.caption = caption
        self.done = False
        self.clock = pygame.time.Clock()
        self.fps = 60.0
        self.fps_visible = True
        self.now = 0.0
        self.keys = pygame.key.get_pressed()
        self.titleText = utils.Text(config.FONT, 50, "Space Invaders", config.colors.WHITE, 164, 155)

    def update(self):
        self.now = pygame.time.get_ticks()
        self.check_input()

    def draw(self, interpolate):
        self.titleText.draw(self.screen)
        pygame.display.update()

    def main(self):
        lag = 0.0
        while not self.done:
            lag += self.clock.tick(self.fps)
            while lag >= config.TIME_PER_UPDATE:
                self.update()
                lag -= config.TIME_PER_UPDATE
            self.draw(lag/config.TIME_PER_UPDATE)

    def check_input(self):
        self.keys = pygame.key.get_pressed()
        for e in pygame.event.get():
            if e.type == pygame.QUIT: #pylint: disable=E1101
              sys.exit()
