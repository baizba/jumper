import pygame

from Kangaroo import Kangaroo
from Water import Water


def keyboard_up(event):
    return event.type == pygame.KEYDOWN and event.key == pygame.K_UP


def quit_game():
    pygame.quit()


class KangarooJackGame:

    def __init__(self):
        pygame.init()

        self.display_width = 800
        self.display_height = 600

        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Kangaroo Jack')

        self.black = (0, 0, 0)

        self.clock = pygame.time.Clock()

        self.kangaroo_img = pygame.image.load('image/kangaroo.png')
        background_img = pygame.image.load('image/background.png')
        self.background = pygame.transform.scale(background_img, (self.display_width, self.display_height))

        # object scrolling speed (how fast objects go from right to left)
        self.scroll_speed = 10

        # height of water and ground (how high from the ground are the objects)
        self.height_above_ground = 106

    def show_score(self, count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Dodged: " + str(count), True, self.black)
        self.gameDisplay.blit(text, (0, 0))

    def animate_water(self, water, x):
        pygame.draw.rect(self.gameDisplay, water.water_color,
                         [water.water_x, water.water_y, water.water_width, water.water_height])
        # if the water is of the screen re-initialize water
        if water.water_x < -water.water_width:
            water.reset(x)
        water.water_x -= self.scroll_speed

    def draw_kangaroo(self, kangaroo):
        self.gameDisplay.blit(self.kangaroo_img, (kangaroo.kangaroo_x, kangaroo.kangaroo_y))

    def game_loop(self):
        game_exit = False
        score = 0

        # kangaroo
        kangaroo_jack = Kangaroo(self.display_height, self.height_above_ground)

        # water
        blue_water = Water(self.display_width, self.display_height, self.height_above_ground)

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
            self.gameDisplay.blit(self.background, (bg_index, 0))
            self.gameDisplay.blit(self.background, (bg_index + self.display_width, 0))
            if bg_index < - self.display_width:
                bg_index = 0

            # how fast background moves (background scrolling)
            bg_index -= 2

            # kangaroo
            self.draw_kangaroo(kangaroo_jack)

            # animate water
            self.animate_water(blue_water, self.display_width)

            # check to increase score (water is off the screen)
            if blue_water.water_x < -blue_water.water_width:
                score += 1

            # show score
            self.show_score(score)

            # check for crash (if kangaroo on ground)
            if kangaroo_jack.is_in_water(blue_water):
                blue_water.water_x = self.display_width
                bg_index = 0
                score = 0

            pygame.display.update()
            self.clock.tick(40)

    def update_display(self, frame_rate):
        pygame.display.update()
        self.clock.tick(frame_rate)
