class Kangaroo:
    # image
    kangaroo_img = 'image/kangaroo.png'

    # kangaroo position
    kangaroo_height = 0
    kangaroo_width = 0
    kangaroo_x = 0
    kangaroo_y = 0

    # kangaroo jump
    max_vert_acceleration = 15
    vertical_acceleration = max_vert_acceleration
    is_in_air = False

    def __init__(self, display_height, height_above_ground):
        self.kangaroo_height = 100
        self.kangaroo_width = 85
        self.kangaroo_x = 100
        self.kangaroo_y = display_height - self.kangaroo_height - height_above_ground

    def jump(self):
        if self.vertical_acceleration > 0:
            # reduce vertical offset gradually
            self.vertical_acceleration -= 1
            self.kangaroo_y -= self.vertical_acceleration
            # if we jumped to mx height then prevent hanging in the air and start falling back
            if self.vertical_acceleration == 0:
                self.is_in_air = True

    def fall_down(self):
        if self.vertical_acceleration < self.max_vert_acceleration:
            # decrease vertical offset gradually
            self.kangaroo_y += self.vertical_acceleration
            self.vertical_acceleration += 1
            # just a switch to prevent mid-air jumping
            self.is_in_air = True
            if self.vertical_acceleration == self.max_vert_acceleration:
                self.is_in_air = False

