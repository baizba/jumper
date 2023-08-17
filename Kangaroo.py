class Kangaroo:
    # image
    kangaroo_img = 'image/kangaroo.png'

    def __init__(self, display_height, height_above_ground):
        # kangaroo position
        self.kangaroo_height = 100
        self.kangaroo_width = 85
        self.kangaroo_x = 100
        self.kangaroo_y = display_height - self.kangaroo_height - height_above_ground
        self.ground_level = self.kangaroo_y

        # kangaroo jump
        self.max_vert_acceleration = 15
        self.vertical_acceleration = self.max_vert_acceleration
        self.is_jum_in_progress = False

    def jump(self):
        if self.vertical_acceleration > 0:
            # reduce vertical offset gradually
            self.vertical_acceleration -= 1
            self.kangaroo_y -= self.vertical_acceleration
            # if we jumped to mx height then prevent hanging in the air and start falling back
            if self.vertical_acceleration == 0:
                self.is_jum_in_progress = True

    def fall_down(self):
        if self.vertical_acceleration < self.max_vert_acceleration:
            # decrease vertical offset gradually
            self.kangaroo_y += self.vertical_acceleration
            self.vertical_acceleration += 1
            # just a switch to prevent mid-air jumping
            self.is_jum_in_progress = True
            if self.vertical_acceleration == self.max_vert_acceleration:
                self.is_jum_in_progress = False

    def is_on_ground(self):
        return self.kangaroo_y == self.ground_level

    def is_in_water(self, water):
        return self.is_on_ground() and \
               (water.water_x < self.kangaroo_x + self.kangaroo_width - 10 < water.water_x + water.water_width or
                water.water_x < self.kangaroo_x + 20 < water.water_x + water.water_width)
