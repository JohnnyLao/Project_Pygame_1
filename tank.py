import pygame


class Tank:

    def __init__(self, screen: object, lives: object, ammo_tank: object) -> object:
        """инициализация танка"""
        self.ammo_tank = ammo_tank
        self.lives = lives
        self.screen = screen
        self.image = pygame.image.load("Pics/tank.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.speed = 0.2
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False

    def output(self):
        """прорисовка танка"""
        self.screen.blit(self.image, self.rect)

    def update_tank(self):
        """обновление позиции танка"""
        if self.mright and self.rect.right < self.screen_rect.right / 2:
            self.x += self.speed
        if self.mleft and self.rect.left > 0:
            self.x -= self.speed
        if self.mup and self.rect.top > 0:
            self.y -= self.speed
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def ammo_restore(self, qty):
        self.ammo_tank += qty

    def tank_kill(self):
        self.x = 100