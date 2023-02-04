class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 200, 200)
        self.fullscreen = True

        # 1 = Arrow control, 2 = WASD control
        if self.fullscreen == False:
            self.ship_speed = 1.5
            self.bullet_speed = 1
        else:
            self.ship_speed = 3.5
            self.bullet_speed = 2.5
        self.movement_keys = "2"
        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.difficulty = 2