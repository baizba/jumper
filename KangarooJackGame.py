import pygame

from Kangaroo import Kangaroo
from Water import Water


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

        # game exit control (when you click X)
        self.game_exit = False

        # score
        self.score = 0

        # index for background animation
        self.bg_index = 0

        # kangaroo
        self.kangaroo_jack = Kangaroo(self.display_height, self.height_above_ground)

        # water
        self.blue_water = Water(self.display_width, self.display_height, self.height_above_ground)

        # last event
        self.event = None

    def keyboard_up(self):
        if self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_UP:
            return True
        return False

    def show_score(self):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Dodged: " + str(self.score), True, self.black)
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

    def reset_game(self):
        # reset score
        self.score = 0

        # background animation index reset
        self.bg_index = 0

        # reset water to right
        self.blue_water.reset(self.display_width)

    def is_game_exit(self):
        for event in pygame.event.get():
            # remember the last event for later usage
            self.event = event
            if event.type == pygame.QUIT:
                return True
        return False

    def step(self):
        if self.keyboard_up() and not self.kangaroo_jack.is_jum_in_progress:
            self.kangaroo_jack.jump()
        else:
            self.kangaroo_jack.fall_down()

        # check to increase score (water is off the screen)
        if self.blue_water.water_x < -self.blue_water.water_width:
            self.score += 1

    def render(self, frame_rate):
        # background
        self.gameDisplay.blit(self.background, (self.bg_index, 0))
        self.gameDisplay.blit(self.background, (self.bg_index + self.display_width, 0))
        if self.bg_index < - self.display_width:
            self.bg_index = 0

        # how fast background moves (background scrolling)
        self.bg_index -= 2

        # kangaroo
        self.draw_kangaroo(self.kangaroo_jack)

        # animate water
        self.animate_water(self.blue_water, self.display_width)

        # show score
        self.show_score()

        pygame.display.update()
        self.clock.tick(frame_rate)

    def is_crash(self):
        return self.kangaroo_jack.is_in_water(self.blue_water)

    def update_display(self, frame_rate):
        pygame.display.update()
        self.clock.tick(frame_rate)
