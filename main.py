from random import randrange

import pygame as pg
from Constants import *

from GameClasses import Player, Zombie, Bullet


def main():
    # Инициализация PyGame и создание игрового окна
    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Zombie Attack")
    clock = pg.time.Clock()

    all_sprites = pg.sprite.Group()
    zombies = pg.sprite.Group()
    bullets = pg.sprite.Group()
    player = Player()
    all_sprites.add(player)
    for _ in range(randrange(3, 9)):
        zombie = Zombie()
        all_sprites.add(zombie)
        zombies.add(zombie)

    # Основной игровой цикл
    running = True
    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    bullet = player.player_shooter()
                    all_sprites.add(bullet)
                    bullets.add(bullet)

        # Обновляем группу со спрайтами спрайты
        all_sprites.update()

        # проверяем на столкновения Игрока и зомби
        collisions = pg.sprite.spritecollide(player, zombies, False)
        if collisions:
            running = False

        # проверяем на столкновения сняряда и зомби
        collisions = pg.sprite.groupcollide(zombies, bullets, True, True)
        for _ in collisions:
            zombie = Zombie()
            all_sprites.add(zombie)
            zombies.add(zombie)

        # Отрисовка объектов на экране
        screen.fill(BLACK)
        all_sprites.draw(screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    pg.quit()


if __name__ == '__main__':
    main()
