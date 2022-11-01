import pygame, sys
from bullets import Bullet, Bullet_enemy
from text import Text
from main import run

def events(screen, tank, bullets, enemy, enemy_bullets, text):
    """управление игроков"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                tank.mright = True
            elif event.key == pygame.K_a:
                tank.mleft = True
            elif event.key == pygame.K_w:
                tank.mup = True
            elif event.key == pygame.K_s:
                tank.mdown = True
            if event.key == pygame.K_RIGHT:
                enemy.mright = True
            elif event.key == pygame.K_LEFT:
                enemy.mleft = True
            elif event.key == pygame.K_UP:
                enemy.mup = True
            elif event.key == pygame.K_DOWN:
                enemy.mdown = True
            elif event.key == pygame.K_SPACE:
                if tank.ammo > 0:
                    print(f'AMMO = {tank.ammo - 1}')
                    new_bullet = Bullet(screen, tank)
                    bullets.add(new_bullet)
                    tank.ammo -= 1
                else:
                    print(f'TANK NO AMMO!!!')
            elif event.key == pygame.K_BACKSPACE:
                if enemy.ammo > 0:
                    print(f'AMMO = {enemy.ammo - 1}')
                    new_bullet = Bullet_enemy(screen, enemy)
                    enemy_bullets.add(new_bullet)
                    enemy.ammo -= 1
                else:
                    print(f'ENEMY NO AMMO!!!')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                tank.mright = False
            elif event.key == pygame.K_a:
                tank.mleft = False
            elif event.key == pygame.K_w:
                tank.mup = False
            elif event.key == pygame.K_s:
                tank.mdown = False
            elif event.key == pygame.K_RIGHT:
                enemy.mright = False
            elif event.key == pygame.K_LEFT:
                enemy.mleft = False
            elif event.key == pygame.K_UP:
                enemy.mup = False
            elif event.key == pygame.K_DOWN:
                enemy.mdown = False


def update(bg_color, screen, tank, bullets, enemy, enemy_bullets, text):
    """обновление экрана"""
    screen.fill(bg_color)
    text.text_show()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for enemy_bullet in enemy_bullets.sprites():
        enemy_bullet.draw_enemy_bullet()
    tank.output()
    enemy.output()
    tank.update_tank()
    enemy.update_tank()
    pygame.display.flip()
    if pygame.sprite.spritecollide(enemy, bullets, True): #
        """Попадание по Врагу, сброс спавна, + 5 патронов"""
        print("ENEMY HIT!")
        enemy.enemy_kill()
        tank.ammo_restore(5)
        bullets.empty()
        enemy_bullets.empty()
        print(f'TANK AMMO = {tank.ammo} --> +5 ammo restored')
        pygame.time.delay(1000)

    if pygame.sprite.spritecollide(tank, enemy_bullets, True):
        """Попадание по Игроку, сброс спавна, + 5 патронов"""
        print("TANK HIT!")
        tank.kill()
        enemy.ammo_restore(5)
        bullets.empty()
        enemy_bullets.empty()
        print(f'ENEMY AMMO = {enemy.ammo} --> +5 ammo restored')
        pygame.time.delay(1000)

    if pygame.sprite.groupcollide(bullets, enemy_bullets, True, True):
        """Попадание по Снаряду"""
        print("BANG")


def update_bullets(bullets):
    """обновление позиции пуль игрока"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.right >= 1800:
            bullets.remove(bullet)


def update_enemy_bullets(enemy_bullets):
    """обновление позиции пуль врага"""
    enemy_bullets.update()
    for bullet in enemy_bullets.copy():
        if bullet.rect.right <= 0:
            enemy_bullets.remove(bullet)

