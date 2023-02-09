from Constants import *


# Функция загрузки изображений
def load_images():
    background = pg.image.load(path.join(IMG_DIR, 'BG.png')).convert()
    player_skin = pg.image.load(path.join(IMG_DIR, 'player.png')).convert()
    zombie_skin = pg.image.load(path.join(IMG_DIR, 'zombie.png')).convert()
    bullet_skin = pg.image.load(path.join(IMG_DIR, 'bullet.png')).convert()
    return background, player_skin, zombie_skin, bullet_skin


def load_game_sound():
    shoot_sound = pg.mixer.Sound(path.join(SND_DIR, 'shoot_snd.wav'))
    return shoot_sound


# Функция рисования текста на экране
def text_draw(surface, text, font_size, x, y):
    font = pg.font.Font(FONT_NAME, font_size)
    font_surface = font.render(text, False, WHITE)
    font_rect = font_surface.get_rect()
    font_rect.midtop = (x, y)
    surface.blit(font_surface, font_rect)
