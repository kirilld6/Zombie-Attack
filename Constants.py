from os import path
import pygame as pg

# Дерриктория с изображениями спрайтов
IMG_DIR = path.join(path.dirname(__file__), 'img')
# Дерриктория со звуком
SND_DIR = path.join(path.dirname(__file__), 'sound')
# Шрифт
FONT_DIR = path.join(path.dirname(__file__), 'fonts')
# Сохранения
DATA_DIR = path.join(path.dirname(__file__), 'DataSave')
# Задаем константами размеры  экрана
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 900

# Частота обновления кадров
FPS = 60
# Игровые часы
CLOCK = pg.time.Clock()

# Время действия усиления угрока в миллисекундах
POWER_UP_TIME = 6000

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Технические цвета для работы
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)

# Размер полосы жизней
HEALTH_LENGHT = 100
HEALTH_WIDTH = 10
