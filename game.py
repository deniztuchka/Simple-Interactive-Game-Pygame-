import pygame
import random
import time

pygame.init()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dodge the Falling Blocks")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()

player_width = 50
player_height = 50
player_x = screen_width // 2
player_y = screen_height - player_height - 10
player_speed = 7

block_width = 50
block_height = 50
block_speed = 5
block_list = []

score = 0
difficulty_increase_timer = time.time()

def create_block():
    x = random.randint(0, screen_width - block_width)
    y = -block_height
    block_list.append([x, y])

def draw_player(x, y):
    pygame.draw.rect(screen, white, [x, y, player_width, player_height])

def draw_block(block):
    pygame.draw.rect(screen, red, [block[0], block[1], block_width, block_height])

def display_score(score):
    font = pygame.font.SysFont(None, 35)
    text = font.render(f"Score: {score}", True, white)
    screen.blit(text, [10, 10])

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    screen.fill(black)

    if time.time() - difficulty_increase_timer > 10:
        block_speed += 1
        difficulty_increase_timer = time.time()

    if random.randint(1, 20) == 1:
        create_block()

    for block in block_list:
        block[1] += block_speed
        if block[1] > screen_height:
            block_list.remove(block)
            score += 1
        if player_x < block[0] < player_x + player_width or player_x < block[0] + block_width < player_x + player_width:
            if player_y < block[1] + block_height < player_y + player_height:
                game_over = True
        draw_block(block)

    draw_player(player_x, player_y)
    display_score(score)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
