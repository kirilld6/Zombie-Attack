import sys
from random import randrange, choice, random
from GameFunction import load_images, text_draw, load_game_sound, load_background_music, health_draw, lives_draw, \
    start_screen_game, game_over_screen
from Constants import *
from GameClasses import Player, Zombie, Killing, Power


def main():
    # функция создания зомби,
    def create_zombie():
        zombie = Zombie()
        all_sprites.add(zombie)
        zombies.add(zombie)

    # Инициализация PyGame и создание игрового окна
    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Zombie Attack")


    # Загрузка изображений фонов
    background = pg.image.load(path.join(IMG_DIR, 'BG.png')).convert()
    background_rect = background.get_rect()

    bg_start_game = pg.image.load(path.join(IMG_DIR, 'Start.jpg')).convert()
    bg_start_game = pg.transform.scale(bg_start_game, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_start_game_rect = bg_start_game.get_rect()

    # «аварийное завершение»


    # Загрузка фонового изображения основной игры

    # Фоновая музыка
    load_background_music()
    # Основной игровой цикл
    start_game = True
    game_over = False
    running = True
    while running:
        if start_game:
            start_screen_game(screen, bg_start_game, bg_start_game_rect)
            start_game = False

            # Группы спрайтов
            all_sprites = pg.sprite.Group()
            zombies = pg.sprite.Group()
            bullets = pg.sprite.Group()
            power_up = pg.sprite.Group()

            # Создаем экземпляр класса игрока
            player = Player()
            all_sprites.add(player)

            # Создаем зомби
            for _ in range(randrange(3, 9)):
                create_zombie()
            score = 0

        # Частота обновления цикла
        CLOCK.tick(FPS)
        # Обработка событий
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if player.power_gun == 1:
                        bullet = player.player_shooter()[0]
                        fire = player.player_shooter()[1]
                        all_sprites.add(bullet)
                        all_sprites.add(fire)
                        bullets.add(bullet)
                        load_game_sound()[0].play()
                    if player.power_gun >= 2:
                        bullet_1 = player.player_shooter()[0]
                        bullet_2 = player.player_shooter()[1]
                        fire_1 = player.player_shooter()[2]
                        fire_2 = player.player_shooter()[3]
                        all_sprites.add(bullet_1)
                        all_sprites.add(bullet_2)
                        all_sprites.add(fire_1)
                        all_sprites.add(fire_2)
                        bullets.add(bullet_1)
                        bullets.add(bullet_2)
                        load_game_sound()[3].play()

        if game_over:
            game_over_screen(screen, background, background_rect, score)
            game_over = False

            # Группы спрайтов
            all_sprites = pg.sprite.Group()
            zombies = pg.sprite.Group()
            bullets = pg.sprite.Group()
            power_up = pg.sprite.Group()

            # Создаем экземпляр класса игрока
            player = Player()
            all_sprites.add(player)

            # Создаем зомби
            for _ in range(randrange(3, 9)):
                create_zombie()
            score = 0

        # Обновляем группу со спрайтами
        all_sprites.update()

        # проверяем на столкновения сняряда и зомби
        collisions = pg.sprite.groupcollide(zombies, bullets, True, True)
        for collision in collisions:
            score += randrange(1, 4)
            choice(load_game_sound()[1]).play()
            kill = Killing(collision.rect.center)
            all_sprites.add(kill)
            # генерируем выпадение "усилений"
            if random() > 0.8:
                powerup = Power(collision.rect.center)
                all_sprites.add(powerup)
                power_up.add(powerup)
            create_zombie()

        # проверяем на столкновения Игрока и зомби
        collisions = pg.sprite.spritecollide(player, zombies, True)
        for collision in collisions:
            player.health -= collision.damage
            kill_zombie = Killing(collision.rect.center)
            all_sprites.add(kill_zombie)
            create_zombie()
            # Проверка уровня жизни персонажа
            if player.health <= 0:
                load_game_sound()[2].play()
                death_player = Killing(player.rect.center)
                all_sprites.add(death_player)
                player.hide_player()
                player.lives -= 1
                player.health = 100

        # Проверяем столкновение Игрока и "модификаторов"
        gains_type = pg.sprite.spritecollide(player, power_up, True)
        for gain in gains_type:
            if gain.type_pow == 'health':
                player.health += randrange(10, 15)
                if player.health >= 100:
                    player.health = 100
                load_game_sound()[4].play()

            if gain.type_pow == 'gun':
                player.power_up_gun()
                load_game_sound()[5].play()

            # Проверяем жив ли игрок и есть ли у него жизни
        if player.lives == -1 and not death_player.alive():
            game_over = True

        # Отрисовка объектов на экране
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        text_draw(screen, str(score), 18, SCREEN_WIDTH // 2, 10)
        health_draw(screen, 5, 5, player.health)
        lives_draw(screen, SCREEN_WIDTH - 100, 5, player.lives, load_images()[5])
        # Переворачиваем дисплей для корректного отображения объектов на экране
        pg.display.flip()
        CLOCK.tick(FPS)

    pg.quit()


if __name__ == '__main__':
    main()
