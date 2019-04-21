import json


class GameStats():
    """A class to manage game statistics."""

    def __init__(self, ai_settings, filename):
        """Initiate statistics attributes."""
        self.ai_settings = ai_settings
        self.game_active = False
        with open(filename) as f_obj:
            self.highscore = json.load(f_obj)

        self.reset_stats()

    def reset_stats(self):
        self.score = 0
        self.level = 0
        self.car_limit = self.ai_settings.car_limit
