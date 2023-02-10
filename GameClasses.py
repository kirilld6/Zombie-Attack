# Создаем класс игрока на основе pygame.sprite.Sprite
from random import randrange, choice
from Constants import *
from GameFunction import load_images


# Класс игрока на основе класса Sprite библиотеки pygame
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(load_images()[1], (48, 48))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0
        self.speed_y = 0
        self.health = 100
        self.lives = 3
        self.hidden_player = False
        self.time_hidden = pg.time.get_ticks()

    def update(self):
        if self.hidden_player and pg.time.get_ticks() - self.time_hidden > 1000:
            self.hidden_player = False
            self.rect.centerx, self.rect.bottom = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 10)

        self.speed_x = 0
        self.speed_y = 0
        if pg.key.get_pressed()[pg.K_LEFT] or pg.key.get_pressed()[pg.K_a]:
            self.speed_x = -8
        if pg.key.get_pressed()[pg.K_RIGHT] or pg.key.get_pressed()[pg.K_d]:
            self.speed_x = 8
        if pg.key.get_pressed()[pg.K_UP] or pg.key.get_pressed()[pg.K_w]:
            self.speed_y = -8
        if pg.key.get_pressed()[pg.K_DOWN] or pg.key.get_pressed()[pg.K_s]:
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

    def player_shooter(self):
        return Bullet(self.rect.centerx, self.rect.top)

    def hide_player(self):
        self.hidden_player = True
        self.time_hidden = pg.time.get_ticks()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT + 200)


# Класс врага, в нашем случае зомби на основе класса Sprite библиотеки pygame
class Zombie(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(choice(load_images()[2]), (32, 32))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = randrange(-120, -60)
        self.speedy = randrange(1, 3)
        self.damage = randrange(5, 10)

    def update(self):
        self.rect.y += self.speedy
        # При достижении нижней части экрана перемещвем зомби обратно на верх в новую координату x,y
        # и задаем новое значение скорости движения
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = randrange(-100, -40)
            self.speedy = randrange(1, 3)


# Класс пули
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(load_images()[3], (5, 8))
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


# Класс анимации убийтсва
class Killing(pg.sprite.Sprite):

    def __init__(self, center):
        super().__init__()
        self.image = load_images()[4][0]
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
        if self.frame == len(load_images()[4]):
            self.kill()
        else:
            center = self.rect.center
            self.image = load_images()[4][self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center


class Power(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.type_pow = ['shield', 'gun']
        self.image = pg.transform.scale(load_images()[3], (5, 8))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        # Удаляем пулю если она улетела за пределы экрана
        if self.rect.bottom < 0:
            self.kill()




