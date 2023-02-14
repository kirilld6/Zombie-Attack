import sys
from Constants import *

# «аварийное завершение»
def terminate():
    pg.quit()
    sys.exit()


#######################################################################################################################
# Функции для отрисовки начальнго и финального экрана
#######################################################################################################################
# Старторвый экран
def start_screen_game(surface):

    bg_start_game = pg.image.load(path.join(IMG_DIR, 'Start.jpg')).convert()
    bg_start_game = pg.transform.scale(bg_start_game, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_start_game_rect = bg_start_game.get_rect()
    surface.blit(bg_start_game, bg_start_game_rect)
    text_draw(surface, 'Zombie Attack', 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6)
    text_draw(surface, 'Use the arrows on the keyboard to control the Player', 18, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
    text_draw(surface, 'During the game, press the SPACE bar to start shooting', 18, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.5)
    text_draw(surface, "Press SPACE key to begin", 32, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 2 / 3.5)
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


# Экран проигрыша
def game_over_screen(surface, score):
    bg_game_over = pg.image.load(path.join(IMG_DIR, 'BG_END.png')).convert()
    bg_game_over = pg.transform.scale(bg_game_over, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_game_over_rect = bg_game_over.get_rect()
    surface.blit(bg_game_over, bg_game_over_rect)
    text_draw(surface, 'Zombie Attack', 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6)
    text_draw(surface, "Press ESCAPE  to exit game", 20, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 2 / 4.5)
    text_draw(surface, "Press SPACE  to new game", 20, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 2 / 5)
    text_draw(surface, f"YOU SCORE {score} POINTS", 48, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 2 / 4)
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


#####################################################################################################################
# Функции загрузки изображений
#####################################################################################################################
# Загрузка фонового изображения игры
def main_bg():
    # Загрузка изображений фонов
    background = pg.image.load(path.join(IMG_DIR, 'BG.png')).convert()
    background_rect = background.get_rect()
    return background, background_rect


# Скин игрока
def load_player_skin():
    return pg.image.load(path.join(IMG_DIR, 'player.png')).convert()


# Загрузка изображения жиpней
def load_health_img():
    health_player = pg.image.load(path.join(IMG_DIR, 'hearth.png')).convert()
    health_player = pg.transform.scale(health_player, (25, 25))
    return health_player


# Згрузка скинов для зомби
def load_zombie_skin():
    # Список скинов для зомби
    zombie_skins = []
    for skin in ['zombie1.png', 'zombie2.png', 'zombie3.png', 'zombie4.png', ]:
        zombie_skins.append(pg.image.load(path.join(IMG_DIR, skin)).convert())
    return zombie_skins


# Скин ддля пули
def load_bullet_skin():
    return pg.image.load(path.join(IMG_DIR, 'bullet.png')).convert()


# Изображения для анимации крови
def load_blood_animation():
    # Список изображений для анимации крови
    blood_animation = []
    for blood in ['blood1.png', 'blood2.png', 'blood3.png']:
        img = pg.image.load(path.join(IMG_DIR, blood)).convert()
        img.set_colorkey(WHITE)
        blood_animation.append(img)
    return blood_animation


# Загрузка изображения для усилений игрока
def load_powerup_img():
    power_up_images = dict()
    power_up_images['health'] = pg.image.load(path.join(IMG_DIR, 'pharm.png')).convert()
    power_up_images['gun'] = pg.image.load(path.join(IMG_DIR, 'gun.png')).convert()
    return power_up_images


# Загрузка скина усиления игрока
def load_player_skin_powerup():
    return pg.image.load(path.join(IMG_DIR, 'player_pow.png')).convert()


# Загрузка фспышки при выстреле
def load_glok_fire_images():
    return pg.image.load(path.join(IMG_DIR, 'glock_fire.png')).convert()


#######################################################################################################################
# Загрузка звукового сопровождения игры
#######################################################################################################################
# Звук выстрела
def load_shoot_sound():
    return pg.mixer.Sound(path.join(SND_DIR, 'shoot_vfx.wav'))


# Звук выстрела магнума
def load_shoot_mgn_snd():
    return pg.mixer.Sound(path.join(SND_DIR, 'mgn_shoot_vfx.wav'))


# Звук использования аптечки
def load_pharm_snd():
    return pg.mixer.Sound(path.join(SND_DIR, 'pharm.mp3'))


# Звук использования усиления оружия
def powerup_gun_snd():
    return pg.mixer.Sound(path.join(SND_DIR, 'power_gun.mp3'))


# Звук сметри игрока
def kill_player_snd():
    return pg.mixer.Sound(path.join(SND_DIR, 'player_death.ogg'))


# Звуки убийства зомби
def load_kill_zombie_snd():
    # Список звуков при убийстве зомби
    zombie_dead = []
    for dead_snd in ['zombieDeath1.wav', 'zombieDeath2.wav', 'zombieDeath3.wav', 'zombieDeath4.wav', ]:
        zombie_dead.append(pg.mixer.Sound(path.join(SND_DIR, dead_snd)))
    return zombie_dead

def collision_snd():
    return pg.mixer.Sound(path.join(SND_DIR, 'collision.wav'))


# Загрузка фоновой музыки
def load_background_music():
    pg.mixer.music.load(path.join(SND_DIR, 'Mystery Manor.mp3'))
    pg.mixer.music.set_volume(0.4)
    pg.mixer.music.play(loops=-1)


#######################################################################################################################
# Функции отрисовки элементов интерфейса
#######################################################################################################################

# Функция рисования текста на экране
def text_draw(surface, text, font_size, x, y):
    font = pg.font.Font(path.join(FONT_DIR, 'ZombieControl.otf'), font_size)
    font_surface = font.render(text, True, WHITE)
    font_rect = font_surface.get_rect()
    font_rect.midtop = (x, y)
    surface.blit(font_surface, font_rect)


# Отрисовка количество "попыток"
def lives_draw(surface, x, y, lives, img):
    for health in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * health
        img_rect.y = y
        surface.blit(img, img_rect)


# Отрисовка текущего состояния здоровья
def health_draw(surface, x, y, health):
    # Проверка, что жизни не ушли в минус
    if health < 0:
        health = 0
    fill = (health / 100) * HEALTH_LENGHT
    health_outline_rect = pg.Rect(x, y, HEALTH_LENGHT, HEALTH_WIDTH)
    health_fill_rect = pg.Rect(x, y, fill, HEALTH_WIDTH)
    pg.draw.rect(surface, GREEN, health_fill_rect)
    pg.draw.rect(surface, WHITE, health_outline_rect, 2)
