import pygame
from pygame.sprite import Sprite


class Car(Sprite):
    """A class to manage car images."""

    def __init__(self, road, screen, ai_settings):
        super().__init__()
        """Initialize car attributes."""
        self.screen = screen
        self.road = road
        self.ai_settings = ai_settings

        # Load car image and set pos.
        self.image = pygame.image.load("images/Black_viper.bmp")
        self.rect = self.image.get_rect()
        self.rect.bottom = road.rect.bottom - 20
        self.rect.centerx = road.rect.centerx

        # store x-cor as a decimal.
        self.x = float(self.rect.centerx)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update ships pos."""
        if self.moving_right and self.rect.right < self.road.rect.right:
            self.x += self.ai_settings.car_speed_factor
        if self.moving_left and self.rect.left > self.road.rect.left:
            self.x -= self.ai_settings.car_speed_factor

        # update x position
        self.rect.centerx = self.x

    def center(self):
        """Center ship."""
        self.x = self.road.rect.centerx

    def blitme(self):
        """Draw car to screen."""
        self.screen.blit(self.image, self.rect)
