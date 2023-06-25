import random

import pygame

from kangaroo import Kangaroo

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Jumper')

green = (0, 255, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()

kangaroo_img = pygame.image.load('image/kangaroo.png')
background_img = pygame.image.load('image/background.png')
background = pygame.transform.scale(background_img, (display_width, display_height))


def show_score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def draw_object(obj_x, obj_y, obj_width, obj_height, color):
    pygame.draw.rect(gameDisplay, color, [obj_x, obj_y, obj_width, obj_height])


def draw_kangaroo(kangaroo):
    gameDisplay.blit(kangaroo_img, (kangaroo.kangaroo_x, kangaroo.kangaroo_y))


def keyboard_up(event):
    return event.type == pygame.KEYDOWN and event.key == pygame.K_UP


def game_loop():
    game_exit = False
    score = 0

    # height of water and ground
    object_height = 106

    # kangaroo
    kangaroo = Kangaroo(display_height, object_height)

    # water
    water_x = display_width
    water_y = display_height - object_height
    water_min_width = 50
    water_max_width = 200
    water_width = random.randrange(water_min_width, water_max_width)

    # background index
    bg_index = 0

    # object scrolling speed (how fast objects go from right to left)
    scroll_speed = 10

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        if keyboard_up(event) and not kangaroo.is_in_air:
            kangaroo.jump()
        else:
            kangaroo.fall_down()

        gameDisplay.fill(white)

        # background
        gameDisplay.blit(background, (bg_index, 0))
        gameDisplay.blit(background, (bg_index + display_width, 0))

        if bg_index < - display_width:
            bg_index = 0

        # how fast background moves (background scrolling)
        bg_index -= 2

        # kangaroo
        draw_kangaroo(kangaroo)

        # show score
        show_score(score)

        # draw ground
        # draw_object(0, display_height - object_height, display_width, object_height, green)

        # animate water
        draw_object(water_x, water_y, water_width, object_height, blue)
        water_x -= scroll_speed
        if water_x < -water_width:
            water_x = display_width
            water_width = random.randrange(water_min_width, water_max_width)
            score += 1

        pygame.display.update()
        clock.tick(60)

        # check for crash (if kangaroo on ground)
        if kangaroo.kangaroo_y + kangaroo.kangaroo_height == water_y and \
                (water_x < kangaroo.kangaroo_x + kangaroo.kangaroo_width - 10 < water_x + water_width or
                 water_x < kangaroo.kangaroo_x + 20 < water_x + water_width):
            water_x = display_width
            bg_index = 0
            score = 0

        # log the command and distance to water in current frame
        # distance = water_x - kangaroo_x + kangaroo_width


game_loop()
pygame.quit()
quit()
