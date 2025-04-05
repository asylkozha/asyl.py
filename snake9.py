import pygame
import random
from color_palette import *

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont("Arial", 24)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, foods):
        global score
        head = self.body[0]
        for food in foods[:]:
            if head.x == food.pos.x and head.y == food.pos.y:
                for _ in range(food.weight):
                    self.body.append(Point(head.x, head.y))
                score += food.weight
                foods.remove(food)

class Food:
    def __init__(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
        self.weight = random.randint(1, 3)
        self.spawn_time = pygame.time.get_ticks()
# меняет цвет еды в зависимости от веса еды
    def draw(self):
        color = colorGREEN
        if self.weight == 2:
            color = colorBLUE
        elif self.weight == 3:
            color = colorRED
        pygame.draw.rect(screen, color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

# Переменные для игры
score = 0
level = 1
foods = [Food()]
FPS = 5
clock = pygame.time.Clock()
snake = Snake()

running = True
while running:
    screen.fill(colorBLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx = 0
                snake.dy = -1

    draw_grid_chess()
    snake.move()

    # Проверка выхода за границу
    head = snake.body[0]
    if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
        print("Game Over: вышел за границу")
        running = False

    current_time = pygame.time.get_ticks()
    foods = [f for f in foods if current_time - f.spawn_time < 5000]

    if random.randint(1, 40) == 1:
        foods.append(Food())

    snake.check_collision(foods)
    snake.draw()
    for f in foods:
        f.draw()

    # Обновление уровня за каждые 4 еды
    level = score // 4 + 1
    FPS = 5 + (level - 1) * 2

    # Отображение очков и уровня
    score_text = font.render(f"Очки: {score}", True, colorWHITE)
    level_text = font.render(f"Уровень: {level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()