import pygame
import random
import time

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")

# Загрузка изображений и звуков
image_background = pygame.image.load('resources/AnimatedStreet.png')
image_player = pygame.image.load('resources/Player.png')
image_enemy = pygame.image.load('resources/Enemy.png')
image_coin = pygame.image.load('resources/coin.png')  # Добавь coin.png в resources

#pygame.mixer.music.load('resources/background.wav')
#pygame.mixer.music.play(-1)
#sound_crash = pygame.mixer.Sound('resources/crash.wav')

# Шрифт и текст
font = pygame.font.SysFont("Verdana", 30)
font_big = pygame.font.SysFont("Verdana", 60)
image_game_over = font_big.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 10
        self.generate_random_rect()

    def generate_random_rect(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()

# Класс монетки
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin
        self.rect = self.image.get_rect()
        self.generate_random_pos()

    def generate_random_pos(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.width)
        self.rect.top = random.randint(0, HEIGHT // 2)

    def move(self):
        self.rect.move_ip(0, 3)
        if self.rect.top > HEIGHT:
            self.generate_random_pos()

# Игровые переменные
running = True
clock = pygame.time.Clock()
FPS = 60
score = 0

player = Player()
enemy = Enemy()
coin = Coin()

# Группы спрайтов
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

all_sprites.add(player, enemy, coin)
enemy_sprites.add(enemy)
coin_sprites.add(coin)

# Игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move()

    screen.blit(image_background, (0, 0))

    for entity in all_sprites:
        if hasattr(entity, "move"):
            entity.move()
        screen.blit(entity.image, entity.rect)

    # Проверка столкновения с врагом
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()
        time.sleep(3)
        running = False

    # Проверка сбора монеты
    if pygame.sprite.spritecollideany(player, coin_sprites):
        score += 1
        coin.kill()
        coin = Coin()
        coin_sprites.add(coin)
        all_sprites.add(coin)

    # Отображение очков
    score_text = font.render(f"Coins: {score}", True, "white")
    screen.blit(score_text, (WIDTH - 140, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()