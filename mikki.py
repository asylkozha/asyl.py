import pygame
import datetime

pygame.init()

# Размеры окна 
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# Загрузка изображений
background = pygame.image.load('resources/clock.png')
left_hand = pygame.image.load('resources/left_hand.png')
right_hand = pygame.image.load('resources/right_hand.png')
print("Left hand size:", left_hand.get_size())
print("Right hand size:", right_hand.get_size())
# Центр вращения (центр часов)
center_x, center_y = WIDTH // 2, HEIGHT // 2

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем текущее время
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute

    # Углы поворота
    second_angle = -6 * seconds  # 360 / 60 = 6 градусов на каждую секунду
    minute_angle = -6 * minutes

    # Очистка экрана
    screen.blit(background, (0, 0))

    # Сначала смещаем руки, чтобы крутить от их основания
    offset = pygame.Vector2(0, -80)  # длина "руки" от центра

    # Левая (секундная)
    rotated_left = pygame.transform.rotate(left_hand, second_angle)
    left_pos = offset.rotate(-second_angle) + (center_x, center_y)
    left_rect = rotated_left.get_rect(center=left_pos)

    # Правая (минутная)
    rotated_right = pygame.transform.rotate(right_hand, minute_angle)
    right_pos = offset.rotate(-minute_angle) + (center_x, center_y)
    right_rect = rotated_right.get_rect(center=right_pos)

    # Отрисовка рук
    screen.blit(rotated_right, right_rect)
    screen.blit(rotated_left, left_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()