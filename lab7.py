import pygame

pygame.init()

# Размеры окна
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Параметры мяча
radius = 25
x = WIDTH // 2
y = HEIGHT // 2
speed = 20

# Игровой цикл
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - radius - speed >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + radius + speed <= WIDTH:
        x += speed
    if keys[pygame.K_UP] and y - radius - speed >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + radius + speed <= HEIGHT:
        y += speed

    # Рисуем шар
    pygame.draw.circle(screen, RED, (x, y), radius)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()