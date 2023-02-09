from random import randrange

from GameFunction import load_images, text_draw

import pygame as pg
from Constants import *

from GameClasses import Player, Zombie


def main():
    # Инициализация PyGame и создание игрового окна
    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Zombie Attack")
    clock = pg.time.Clock()
    # Загрузка игровой графики
    background_rect = load_images()[0].get_rect()

    all_sprites = pg.sprite.Group()
    zombies = pg.sprite.Group()
    bullets = pg.sprite.Group()
    player = Player()
    all_sprites.add(player)
    for _ in range(randrange(3, 9)):
        zombie = Zombie()
        all_sprites.add(zombie)
        zombies.add(zombie)

    # Cчетчик очков
    score = 0

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
            # running = False
            print('*')

        # проверяем на столкновения сняряда и зомби
        collisions = pg.sprite.groupcollide(zombies, bullets, True, True)
        for _ in collisions:
            score += 1
            zombie = Zombie()
            all_sprites.add(zombie)
            zombies.add(zombie)
            print(score)

        # Отрисовка объектов на экране
        screen.fill(BLACK)
        screen.blit(load_images()[0], background_rect)
        all_sprites.draw(screen)
        text_draw(screen, str(score), 18, SCREEN_WIDTH // 2, 10)
        # *after* drawing everything, flip the display
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()


if __name__ == '__main__':
    main()
