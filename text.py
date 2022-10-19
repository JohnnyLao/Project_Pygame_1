import pygame


class Text:
    def __init__(self, screen, text):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text = text
        self.text_color = (100, 100, 100)
        self.font = pygame.font.SysFont(None, 120)
        self.image_score()

    def image_score(self):
        self.text_img = self.font.render(str(self.text), True, self.text_color, (0, 0, 0))
        self.text_rect = self.text_img.get_rect()
        self.text_rect.center = self.screen_rect.center

    def text_show(self):
        self.screen.blit(self.text_img, self.text_rect)



