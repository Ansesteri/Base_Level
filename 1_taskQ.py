import sys
import pygame
from settings import Settings

class Window:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.settings.bg_color = (0, 0, 255)
        if self.settings.fullscreen == True:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        elif self.settings.fullscreen == False:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Blue Window")
    
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
    def _check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    main = Window()
    main.run_game()