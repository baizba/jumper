import random

import pygame

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

carImg = pygame.image.load('image/kangaroo.png')
background_img = pygame.image.load('image/background.png')
background = pygame.transform.scale(background_img, (display_width, display_height))


def show_score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def draw_object(obj_x, obj_y, obj_width, obj_height, color):
    pygame.draw.rect(gameDisplay, color, [obj_x, obj_y, obj_width, obj_height])


def draw_kangaroo(x, y):
    gameDisplay.blit(carImg, (x, y))


def going_up(event, falling_down):
    return event.type == pygame.KEYDOWN and event.key == pygame.K_UP and not falling_down


def game_loop():
    game_exit = False
    score = 0

    # height of water and ground
    object_height = 106

    # kangaroo position
    kangaroo_height = 100
    kangaroo_width = 85
    kangaroo_x = 100
    kangaroo_y = display_height - kangaroo_height - object_height

    # kangaroo jump
    max_vert_offset = 15
    vertical_offset = max_vert_offset
    is_falling_down = False

    # water
    water_x = display_width
    water_y = display_height - object_height
    water_min_width = 50
    water_max_width = 200
    water_width = random.randrange(water_min_width, water_max_width)

    # background index
    bg_index = 0

    # scrolling speed (how fast objects go from right to left)
    scroll_speed = 10

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        if going_up(event, is_falling_down):
            if vertical_offset > 0:
                # reduce vertical offset gradually
                vertical_offset -= 1
                kangaroo_y -= vertical_offset
                # if we jumped to mx height then prevent hanging in the air and start falling back
                if vertical_offset == 0:
                    is_falling_down = True
        else:
            if vertical_offset < max_vert_offset:
                # decrease vertical offset gradually
                kangaroo_y += vertical_offset
                vertical_offset += 1
                # just a switch to prevent mid-air jumping
                is_falling_down = True
                if vertical_offset == max_vert_offset:
                    is_falling_down = False

        gameDisplay.fill(white)

        # background
        gameDisplay.blit(background, (bg_index, 0))
        gameDisplay.blit(background, (bg_index + display_width, 0))

        if bg_index < - display_width:
            bg_index = 0

        bg_index -= scroll_speed

        # kangaroo
        draw_kangaroo(kangaroo_x, kangaroo_y)

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
        if kangaroo_y + kangaroo_height == water_y and \
                (water_x < kangaroo_x + kangaroo_width - 10 < water_x + water_width or
                 water_x < kangaroo_x + 20 < water_x + water_width):
            water_x = display_width
            bg_index = 0
            score = 0


game_loop()
pygame.quit()
quit()
