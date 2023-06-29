import random


class Water:

    def __init__(self, display_width, display_height, height_above_ground):
        self.water_min_width = 50
        self.water_max_width = 200
        self.water_x = display_width
        self.water_y = display_height - height_above_ground
        self.water_width = random.randrange(self.water_min_width, self.water_max_width)
        self.water_height = height_above_ground
        self.water_color = (0, 0, 255)

    def reset(self, x):
        self.water_x = x
        self.water_width = random.randrange(self.water_min_width, self.water_max_width)
