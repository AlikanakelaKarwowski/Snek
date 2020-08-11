import pygame
import random

pygame.init()

white = (214, 239, 199)
yellow = (251, 253, 138)
black = (0, 0, 0)
red = (213, 50, 80)
green = (57, 255, 20)
blue = (1, 169, 180)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snek Gam')

clock = pygame.time.Clock()

snek_block = 10
snek_speed = 15

font_style = pygame.font.SysFont("dejavusansmon", 25)
score_font = pygame.font.SysFont("dejavuserif", 30)


def myScore(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def my_snek(snek_block, snek_list):
    for x in snek_list:
        pygame.draw.rect(dis,green, [round(x[0]), round(x[1]), snek_block, snek_block])


def message(msg, color):
    text = font_style.render(msg, True, color)
    dis.blit(text, [round(dis_width / 6), round(dis_height / 3)])


def gamLoop():
    gam_over = False
    gam_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snek_List = []
    lenOfSnek = 1

    foodX = round(random.randrange(0, dis_width - snek_block) / 10.0) * 10.0
    foodY = round(random.randrange(0, dis_height - snek_block) /10.0) * 10.0

    while not gam_over:

        while gam_close == True:
            dis.fill(black)
            message("You Lost! Press P-Play Again or Q-Quit", red)
            myScore(lenOfSnek - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gam_over = True
                        gam_close = False
                    if event.key == pygame.K_p:
                        gamLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snek_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snek_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snek_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snek_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            gam_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [int(foodX), int(foodY), snek_block, snek_block])
        snek_Head = []
        snek_Head.append(x1)
        snek_Head.append(y1)
        snek_List.append(snek_Head)

        if len(snek_List) > lenOfSnek:
            del snek_List[0]

        for x in snek_List[:-1]:
            if x == snek_Head:
                gam_close = True

        my_snek(snek_block, snek_List)
        myScore(lenOfSnek - 1)

        pygame.display.update()

        if x1 == foodX and y1 == foodY:
            foodX = round(random.randrange(0, dis_width - snek_block) / 10.0) * 10.0
            foodY = round(random.randrange(0, dis_height - snek_block) / 10.0) * 10.0
            lenOfSnek += 1

        clock.tick(snek_speed)

    pygame.quit()


gamLoop()
