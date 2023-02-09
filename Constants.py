from os import path
import pygame as pg

# Дерриктория с изображениями спрайтов
IMG_DIR = path.join(path.dirname(__file__), 'img')

# Задаем константами размеры  экрана
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 700

# Частота обновления кадров
FPS = 60

# Шрифт
FONT_NAME = pg.font.match_font('arial')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
