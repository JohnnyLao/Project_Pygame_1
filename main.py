import pygame, controls
from tank import Tank
from enemy import Enemy
from pygame.sprite import Group
from text import Text


def run():
    pygame.init()
    screen = pygame.display.set_mode((1800, 800))
    pygame.display.set_caption("Олег Пидор")
    bg_color = (0, 0, 0)
    tank = Tank(screen, 3, 999)
    bullets, enemy_bullets = Group(), Group()
    enemy = Enemy(screen, 3, 999)
    text = Text(screen, "ОЛЕГ VS ЕГОРКА")
    while True:
        controls.events(screen, tank, bullets, enemy, enemy_bullets, text)
        controls.update(bg_color, screen, tank, bullets, enemy, enemy_bullets, text)
        controls.update_bullets(bullets)
        controls.update_enemy_bullets(enemy_bullets)


if __name__ == '__main__':
    run()


