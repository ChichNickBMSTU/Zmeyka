import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()


import pygame
import time
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Змейка')


white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
yellow = (255, 255, 0)

snake_block = 10
snake_speed = 7

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [800 / 6, 600 / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = 400
    y1 = 300

    x1_change = 0
    y1_change = 0

    snake_List = []
    dlina_of_snake = 1
    snake_speed = 7

    foodx = round(random.randrange(0, 800 - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0

    zyax = round(random.randrange(0, 800 - snake_block) / 10.0) * 10.0
    zyay = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0
    while not game_over:

        while game_close == True:
            screen.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(screen, yellow, [zyax, zyay, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > dlina_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for x in snake_List:
            pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, 800 - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0
            dlina_of_snake += 1
        if x1 == zyax and y1 == zyay:
            zyax = round(random.randrange(0, 800 - snake_block) / 10.0) * 10.0
            zyay = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0
            dlina_of_snake += 3
            snake_speed += 1


        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()