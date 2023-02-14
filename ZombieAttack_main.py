from random import randrange, choice, random
from GameFunction import *
from Constants import *
from GameClasses import Player, Zombie, Killing, Power


# Главный игровой цикл
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

    # Загрузка фоновой музыки
    load_background_music()

    # Загрузка фона основного экрана
    main_bg()

    # Игровые флаги

    start_game = True
    game_over = False
    running = True

    # Основной игровой цикл
    while running:

        # Показать начальный экран игры
        if start_game:
            start_screen_game(screen)
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
            # Обнуляем счетчик очков
            score = 0

        # Частота обновления основного игрового цикла
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
                        load_shoot_sound().play()
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
                        load_shoot_mgn_snd().play()

        # Если игрок проиграл, показать экран проигрыша
        if game_over:
            game_over_screen(screen, score)
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
            # Обнуляем счетчик очков
            score = 0

        # Обновляем группу со спрайтами
        all_sprites.update()

        # проверяем на столкновения сняряда и зомби
        collisions = pg.sprite.groupcollide(zombies, bullets, True, True)
        for collision in collisions:
            score += randrange(1, 4)
            choice(load_kill_zombie_snd()).play()
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
                kill_player_snd().play()
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
                load_pharm_snd().play()

            if gain.type_pow == 'gun':
                player.power_up_gun()
                load_shoot_mgn_snd().play()

            # Проверяем жив ли игрок и есть ли у него жизни
        if player.lives == -1 and not death_player.alive():
            game_over = True

        # Отрисовка объектов на экране
        screen.fill(BLACK)  # технический цвет фона экрана
        screen.blit(main_bg()[0], main_bg()[1])
        all_sprites.draw(screen)
        text_draw(screen, str(score), 18, SCREEN_WIDTH // 2, 10)
        health_draw(screen, 5, 5, player.health)
        lives_draw(screen, SCREEN_WIDTH - 100, 5, player.lives, load_health_img())

        # Переворачиваем дисплей для корректного отображения объектов на экране
        pg.display.flip()
        CLOCK.tick(FPS)

    pg.quit()


if __name__ == '__main__':
    main()
