import pygame

from kangaroo import Kangaroo
from water import Water

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Jumper')

black = (0, 0, 0)

clock = pygame.time.Clock()

kangaroo_img = pygame.image.load('image/kangaroo.png')
background_img = pygame.image.load('image/background.png')
background = pygame.transform.scale(background_img, (display_width, display_height))

# object scrolling speed (how fast objects go from right to left)
scroll_speed = 10

# height of water and ground (how high from the ground are the objects)
height_above_ground = 106


def show_score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def animate_water(water, x):
    pygame.draw.rect(gameDisplay, water.water_color,
                     [water.water_x, water.water_y, water.water_width, water.water_height])
    # if the water is of the screen re-initialize water
    if water.water_x < -water.water_width:
        water.reset(x)
    water.water_x -= scroll_speed


def draw_kangaroo(kangaroo):
    gameDisplay.blit(kangaroo_img, (kangaroo.kangaroo_x, kangaroo.kangaroo_y))


def keyboard_up(event):
    return event.type == pygame.KEYDOWN and event.key == pygame.K_UP


def game_loop():
    game_exit = False
    score = 0

    # kangaroo
    kangaroo_jack = Kangaroo(display_height, height_above_ground)

    # water
    blue_water = Water(display_width, display_height, height_above_ground)

    # background index
    bg_index = 0

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        if keyboard_up(event) and not kangaroo_jack.is_jum_in_progress:
            kangaroo_jack.jump()
        else:
            kangaroo_jack.fall_down()

        # background
        gameDisplay.blit(background, (bg_index, 0))
        gameDisplay.blit(background, (bg_index + display_width, 0))

        if bg_index < - display_width:
            bg_index = 0

        # how fast background moves (background scrolling)
        bg_index -= 2

        # kangaroo
        draw_kangaroo(kangaroo_jack)

        # animate water
        animate_water(blue_water, display_width)

        # check to increase score (water is off the screen)
        if blue_water.water_x < -blue_water.water_width:
            score += 1

        # show score
        show_score(score)

        # check for crash (if kangaroo on ground)
        if kangaroo_jack.is_in_water(blue_water):
            blue_water.water_x = display_width
            bg_index = 0
            score = 0

        pygame.display.update()
        clock.tick(40)


game_loop()
pygame.quit()
quit()
