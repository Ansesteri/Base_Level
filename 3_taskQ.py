import sys

import pygame

from settings import Settings
from ship_second import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        if self.settings.fullscreen == True:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        elif self.settings.fullscreen == False:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)  
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if self.settings.movement_keys == "1":
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_UP:
                self.ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                self.ship.moving_down = True
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        elif self.settings.movement_keys == "2":
            if event.key == pygame.K_d:
                self.ship.moving_right = True
            elif event.key == pygame.K_a:
                self.ship.moving_left = True
            elif event.key == pygame.K_w:
                self.ship.moving_up = True
            elif event.key == pygame.K_s:
                self.ship.moving_down = True
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
    
    def _check_keyup_events(self, event):
        if self.settings.movement_keys == "1":
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False
            elif event.key == pygame.K_UP:
                self.ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                self.ship.moving_down = False
        elif self.settings.movement_keys == "2":
            if event.key == pygame.K_d:
                self.ship.moving_right = False
            elif event.key == pygame.K_a:
                self.ship.moving_left = False
            elif event.key == pygame.K_w:
                self.ship.moving_up = False
            elif event.key == pygame.K_s:
                self.ship.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
