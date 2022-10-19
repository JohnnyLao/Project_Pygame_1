import pygame
import random


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, tank):
        """создание снаряда в танке"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 12, 2)
        self.color = (133, 195, 74)
        self.speed = 0.5
        self.rect.centery = tank.rect.centery - 4
        self.rect.right = tank.rect.right
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """перемещение снаряда"""
        self.x += self.speed
        self.y += random.randint(1, 4) - random.randint(1, 4)
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_bullet(self):
        """отображение на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)


class Bullet_enemy(pygame.sprite.Sprite):

    def __init__(self, screen, enemy):
        """создание снаряда у врага"""
        super(Bullet_enemy, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 12, 2)
        self.color = (136, 8, 8)
        self.speed = 0.5
        self.rect.centery = enemy.rect.centery - 4
        self.rect.left = enemy.rect.left
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """перемещение снаряда"""
        self.x -= self.speed
        self.y -= random.randint(1, 4) - random.randint(1, 4)
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_enemy_bullet(self):
        """отображение на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        # print(len(enemy_bullets))

            # pygame.time.wait(1000)


