import pygame


class Bonus:

    def __init__(self, screen):
        """инициализация танка"""
        self.ammo = ammo
        self.lives = lives
        self.screen = screen
        self.image = pygame.image.load("Pics/tank.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.center = float(self.rect.centerx)
        self.rect.left = self.screen_rect.left
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

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