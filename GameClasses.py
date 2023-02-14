from random import randrange, choice
from GameFunction import *


# Класс игрока на основе класса Sprite библиотеки pygame
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Задаем изображение игрока
        self.image = pg.transform.scale(load_player_skin(), (48, 48))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        # Начальная позиция игрока на экране
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        # Начальная скорость игрока
        self.speed_x = 0
        self.speed_y = 0
        # Колличество жизни, количество попыток(жизней)
        self.health = 100
        self.lives = 3
        ##############################################
        self.hidden_player = False
        self.time_hidden = pg.time.get_ticks()
        # Уровень урона игрока
        self.power_gun = 1
        self.power_time = pg.time.get_ticks()

    def update(self):
        # Время действия усиления
        if self.power_gun >= 2 and pg.time.get_ticks() - self.power_time > POWER_UP_TIME:
            self.power_gun -= 1
            self.power_time = pg.time.get_ticks()
            self.image = pg.transform.scale(load_player_skin(), (48, 48))

        # Задержка перед появлением после гибели игрока
        if self.hidden_player and pg.time.get_ticks() - self.time_hidden > 1000:
            self.hidden_player = False
            self.rect.centerx = SCREEN_WIDTH / 2
            self.rect.bottom = SCREEN_HEIGHT - 10
            self.image = pg.transform.scale(load_player_skin(), (48, 48))

        self.speed_x = 0
        self.speed_y = 0
        if pg.key.get_pressed()[pg.K_LEFT]:  # or pg.key.get_pressed()[pg.K_a]
            self.speed_x = -8
        if pg.key.get_pressed()[pg.K_RIGHT]:  # or pg.key.get_pressed()[pg.K_d]
            self.speed_x = 8
        if pg.key.get_pressed()[pg.K_UP]:  # or pg.key.get_pressed()[pg.K_w]
            self.speed_y = -8
        if pg.key.get_pressed()[pg.K_DOWN]:  # or pg.key.get_pressed()[pg.K_s]
            self.speed_y = 8
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Ограничиваем передвижения персонажа внутри игрового поля
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def power_up_gun(self):
        # Увеличиваем мощьность игрока и устанавливаем время начала действи я усиления
        self.power_gun += 1
        self.power_time = pg.time.get_ticks()
        self.image = pg.transform.scale(load_player_skin_powerup(), (48, 48))
        self.image.set_colorkey(WHITE)

    def player_shooter(self):
        if self.power_gun == 1:
            return Bullet(self.rect.centerx, self.rect.top), BulletFire(self.rect.centerx + 1, self.rect.top + 8)
        if self.power_gun >= 2:
            return Bullet(self.rect.left + 10, self.rect.centery), Bullet(self.rect.right - 10, self.rect.centery), \
                BulletFire(self.rect.left + 10, self.rect.centery - 15), BulletFire(self.rect.right - 10,
                                                                                    self.rect.centery - 15)

    def hide_player(self):
        self.hidden_player = True
        self.time_hidden = pg.time.get_ticks()
        self.image = pg.transform.scale(load_player_skin(), (0, 0))
        self.speed_x = -8
        self.speed_y = 8


# Класс врага, в нашем случае зомби на основе класса Sprite библиотеки pygame
class Zombie(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(choice(load_zombie_skin()), (32, 32))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = randrange(-120, -60)
        self.speedy = randrange(1, 3)
        self.damage = randrange(20, 35)

    def update(self):
        self.rect.y += self.speedy
        # При достижении нижней части экрана перемещаем зомби обратно на верх в новую координату x,y
        # и задаем новое значение скорости движения, ускоряя зомби на целую часть его урона
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = randrange(-100, -40)
            self.speedy = randrange(1, 3) * self.damage // 10


# Класс пули на основе класса Sprite библиотеки pygame
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(load_bullet_skin(), (5, 8))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        # Удаляем пулю если она улетела за пределы экрана
        if self.rect.bottom < 0:
            self.kill()


# Класс изображения выстрела на основе класса Sprite библиотеки pygame
class BulletFire(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(load_glok_fire_images(), (10, 18))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.time_fire = pg.time.get_ticks()

    def update(self):
        if pg.time.get_ticks() - self.time_fire > 40:
            self.kill()


# Класс анимации убийтсва на основе класса Sprite библиотеки pygame
class Killing(pg.sprite.Sprite):

    def __init__(self, center):
        super().__init__()
        self.image = load_blood_animation()[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 90

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(load_blood_animation()):
                self.kill()
            else:
                center = self.rect.center
                self.image = load_blood_animation()[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


# Класс усилений и аптечки на основе класса Sprite библиотеки pygame
class Power(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.type_pow = choice(['health', 'gun'])
        self.image = pg.transform.scale(load_powerup_img()[self.type_pow], (25, 25))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.power_time = pg.time.get_ticks()

    def update(self):
        if pg.time.get_ticks() - self.power_time > randrange(2000, 4000):
            self.kill()
