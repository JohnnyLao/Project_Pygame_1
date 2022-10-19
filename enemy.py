import pygame


class Enemy:
    """класс противника"""

    def __init__(self, screen, lives, ammo_enemy):
        """инициализация противника и начальной позиции"""
        self.lives = lives
        self.ammo_enemy = ammo_enemy
        self.screen = screen
        self.image = pygame.image.load("Pics/tank2.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.midright = self.screen_rect.midright
        self.speed = 0.2
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False

    def output(self):
        """вывод на экран"""
        self.screen.blit(self.image, self.rect)

    def update_tank_enemy(self):
        """обновление позиции врага"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        #Right
        if self.mleft and self.rect.left > self.screen_rect.right / 2:
            self.x -= self.speed
        if self.mup and self.rect.top > 0:
            self.y -= self.speed
        #Right
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed
        #Left
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def ammo_restore(self, qty):
        self.ammo_enemy += qty

    def enemy_kill(self):
        self.x = 1700




