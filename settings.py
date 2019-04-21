class Settings():
    """A class to manage all game settings."""

    def __init__(self):
        """Initialize settings attributes."""
        # ---------Static Settings------------ #

        # Screen settings
        self.screen_width = 1300
        self.screen_height = 680
        self.bg_color = 230, 230, 230

        # road settings.
        self.road_width = 400
        self.road_height = 680
        self.road_color = 255, 255, 255

        # Stripes settings.
        self.stripe_width = 5
        self.stripe_height = 30
        self.stripe_color = 90, 90, 90

        # Car settings
        self.car_limit = 3

        # Speed up scale.
        self.speed = 1.005

        # car y-cor increment
        self.meters = 1

        # dyamic settings
        self.initialize_dynamic_settings()
        self.speed_up()

    def initialize_dynamic_settings(self):
        """Initialize dynamic settings attributes."""
        # ------------Dynamic Settings------------- #
        self.road_speed = 2
        self.score = 20
        self.vehicle_speed = 1.8
        self.car_speed_factor = 0.8

    def speed_up(self):
        """Speed up the pace of the game."""
        self.road_speed *= self.speed
