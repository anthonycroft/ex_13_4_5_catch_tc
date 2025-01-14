class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """initialise the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.catcher_speed_factor = 1.5

        # Ball settings
        self.ball_drop_speed = 0.6