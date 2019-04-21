import pygame.font
from pygame.sprite import Group
from car import Car


class Scoreboard():
    """A class to manage the score board."""

    def __init__(self, ai_settings, screen, stats, road):
        """Initiate class attributes."""
        self.screen = screen
        self.road = road
        self.stats = stats
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.text_color = 30, 30, 30
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_highscore()
        self.prep_cars()

    def prep_score(self):
        """Create a rendered image of score."""
        score = int(round(self.stats.score))
        string_score = '{:,}'.format(score)
        self.score_image = self.font.render(string_score, True, self.text_color, self.ai_settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = self.screen_rect.top

    def prep_highscore(self):
        """Create a rendered image of score."""
        highscore = int(round(self.stats.highscore))
        string_highscore = '{:,}'.format(highscore)
        self.highscore_image = self.font.render(string_highscore, True, self.text_color, self.ai_settings.bg_color)
        self.highscore_image_rect = self.highscore_image.get_rect()
        self.highscore_image_rect.right = self.screen_rect.right - 100
        self.highscore_image_rect.top = self.screen_rect.top

    def prep_cars(self):
        """Show how many runs are left."""
        self.cars = Group()
        for i in range(self.stats.car_limit):
            new_car = Car(self.road, self.screen, self.ai_settings)
            new_car.rect.left = self.screen_rect.left + new_car.rect.width * i
            new_car.rect.top = self.screen_rect.top
            self.cars.add(new_car)

    def show_score(self):
        """Draw score to screen."""
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.highscore_image, self.highscore_image_rect)
        self.cars.draw(self.screen)
