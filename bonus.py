import pygame


class Bonus:

    def __init__(self, screen):
        """инициализация танка"""
        self.screen = screen
        self.image = pygame.image.load("")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.center = float(self.rect.centerx)
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.mup = False
        self.mdown = False

    def output(self):
        """прорисовка танка"""
        self.screen.blit(self.image, self.rect)

    def update_tank(self):
        """обновление позиции танка"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 0.2
        #Right
        if self.mleft and self.rect.left > 0:
            self.center -= 0.2
        #Left
        self.rect.centerx = self.center

    def ammo_restore(self, qty):
        self.ammo += qty