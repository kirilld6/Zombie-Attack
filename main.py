from random import randrange, choice
from GameFunction import load_images, text_draw, load_game_sound, load_background_music, health_draw, lives_draw
from Constants import *
from GameClasses import Player, Zombie, Killing


def main():
    # Инициализация PyGame и создание игрового окна
    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Zombie Attack")
    clock = pg.time.Clock()
    # Загрузка игровой графики
    background = pg.image.load(path.join(IMG_DIR, 'BG.png')).convert()
    background_rect = background.get_rect()

    all_sprites = pg.sprite.Group()
    zombies = pg.sprite.Group()
    bullets = pg.sprite.Group()
    player = Player()
    all_sprites.add(player)

    # функция создания зомби,
    def create_zombie():
        zombie = Zombie()
        all_sprites.add(zombie)
        zombies.add(zombie)

    for _ in range(randrange(3, 9)):
        create_zombie()

    # Cчетчик очков
    score = 0
    # Фоновая музыка
    load_background_music()
    # Основной игровой цикл
    running = True
    while running:
        # Частота обновления цикла
        clock.tick(FPS)
        # Обработка событий
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    bullet = player.player_shooter()
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    load_game_sound()[0].play()

        # Обновляем группу со спрайтами спрайты
        all_sprites.update()

        # проверяем на столкновения Игрока и зомби
        collisions = pg.sprite.spritecollide(player, zombies, True)
        for collision in collisions:
            player.health -= collision.damage
            kill = Killing(collision.rect.center)
            all_sprites.add(kill)
            create_zombie()
            # Проверка уровня жихни персонажа
            if player.health <= 0:
                load_game_sound()[2].play()
                death_player = Killing(player.rect.center)
                all_sprites.add(death_player)
                player.hide_player()
                player.lives -= 1
                player.health = 100

            if player.health == 0 and kill.alive():
                running = False

        # проверяем на столкновения сняряда и зомби
        collisions = pg.sprite.groupcollide(zombies, bullets, True, True)
        for collision in collisions:
            score += 1
            choice(load_game_sound()[1]).play()
            kill = Killing(collision.rect.center)
            all_sprites.add(kill)
            create_zombie()

        # Отрисовка объектов на экране
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        text_draw(screen, str(score), 18, SCREEN_WIDTH // 2, 10)
        health_draw(screen, 5, 5, player.health)
        lives_draw(screen, SCREEN_WIDTH - 100, 5, player.lives, load_images()[5])
        # Переворачиваем дисплей для корректного отображения объектов на экране
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()


if __name__ == '__main__':
    main()
