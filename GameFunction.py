import sys

from Constants import *


def terminate():
    pg.quit()
    sys.exit()


def start_screen_game(surface, bg, bg_rec):
    surface.blit(bg, bg_rec)
    text_draw(surface, 'Zombie Attack', 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
    text_draw(surface, "Press SPACE key to begin", 18, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 2 / 4)
    pg.display.flip()
    waiting = True
    while waiting:
        CLOCK.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    waiting = False


def game_over_screen(surface, bg, bg_rec, score):
    surface.blit(bg, bg_rec)
    text_draw(surface, 'Zombie Attack', 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
    text_draw(surface, "Press ESCAPE  to exit game", 18, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 2 / 4)
    text_draw(surface, "Press SPACE  to new game", 18, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 2 / 4.5)
    text_draw(surface, f"YOU SCORE {score} POINTS", 48, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 2 / 5)
    pg.display.flip()
    waiting = True
    while waiting:
        CLOCK.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    terminate()
                if event.key == pg.K_SPACE:
                    waiting = False

# Функция загрузки изображений
def load_images():
    player_skin = pg.image.load(path.join(IMG_DIR, 'player.png')).convert()
    health_player = pg.image.load(path.join(IMG_DIR, 'hearth.png')).convert()
    health_player = pg.transform.scale(health_player, (25, 25))
    # Список скинов для зомби
    zombie_skins = []
    for skin in ['zombie1.png', 'zombie2.png', 'zombie3.png', 'zombie4.png', ]:
        zombie_skins.append(pg.image.load(path.join(IMG_DIR, skin)).convert())
    bullet_skin = pg.image.load(path.join(IMG_DIR, 'bullet.png')).convert()
    # Список изображений для анимации крови
    blood_animation = []
    for blood in ['blood1.png', 'blood2.png', 'blood3.png']:
        img = pg.image.load(path.join(IMG_DIR, blood)).convert()
        img.set_colorkey(WHITE)
        blood_animation.append(img)

    power_up_images = dict()
    power_up_images['health'] = pg.image.load(path.join(IMG_DIR, 'pharm.png')).convert()
    power_up_images['gun'] = pg.image.load(path.join(IMG_DIR, 'gun.png')).convert()

    player_skin_power_up = pg.image.load(path.join(IMG_DIR, 'player_pow.png')).convert()
    glock_fire = pg.image.load(path.join(IMG_DIR, 'glock_fire.png')).convert()

    return 0, player_skin, zombie_skins, bullet_skin, blood_animation, health_player, power_up_images, \
        player_skin_power_up, glock_fire


def load_game_sound():
    shoot_sound = pg.mixer.Sound(path.join(SND_DIR, 'shoot_vfx.wav'))
    shoot_sound_mgn = pg.mixer.Sound(path.join(SND_DIR, 'mgn_shoot_vfx.wav'))
    pharm_snd = pg.mixer.Sound(path.join(SND_DIR, 'pharm.mp3'))
    gun_sound = pg.mixer.Sound(path.join(SND_DIR, 'power_gun.mp3'))

    # Список звуков при убийстве зомби
    zombie_dead = []
    for dead_snd in ['zombieDeath1.wav', 'zombieDeath2.wav', 'zombieDeath3.wav', 'zombieDeath4.wav', ]:
        zombie_dead.append(pg.mixer.Sound(path.join(SND_DIR, dead_snd)))
    player_death = pg.mixer.Sound(path.join(SND_DIR, 'player_death.ogg'))
    return shoot_sound, zombie_dead, player_death, shoot_sound_mgn, pharm_snd, gun_sound


def load_background_music():
    pg.mixer.music.load(path.join(SND_DIR, 'Mystery Manor.mp3'))
    pg.mixer.music.set_volume(0.4)
    pg.mixer.music.play(loops=-1)


# Функция рисования текста на экране
def text_draw(surface, text, font_size, x, y):
    font = pg.font.Font(path.join(FONT_DIR, 'ZombieControl.otf'), font_size)
    font_surface = font.render(text, True, WHITE)
    font_rect = font_surface.get_rect()
    font_rect.midtop = (x, y)
    surface.blit(font_surface, font_rect)


def lives_draw(surface, x, y, lives, img):
    for health in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * health
        img_rect.y = y
        surface.blit(img, img_rect)


def health_draw(surface, x, y, health):
    # Проверка, что жизни не ушли в минус
    if health < 0:
        health = 0
    fill = (health / 100) * HEALTH_LENGHT
    health_outline_rect = pg.Rect(x, y, HEALTH_LENGHT, HEALTH_WIDTH)
    health_fill_rect = pg.Rect(x, y, fill, HEALTH_WIDTH)
    pg.draw.rect(surface, GREEN, health_fill_rect)
    pg.draw.rect(surface, WHITE, health_outline_rect, 2)




