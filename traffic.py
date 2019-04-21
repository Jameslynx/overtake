import pygame
from random import choice
from pygame.sprite import Sprite


class Traffic(Sprite):
    """A class to manage other vehicle images."""

    def __init__(self, screen, ai_settings, road):
        """Initiate vehicle attributes."""
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings
        self.road = road

        # Load vehicle image and set pos.
        self.image = pygame.image.load(choice(["images/Audi.bmp", "images/Car.bmp", "images/police2.bmp",
                                               "images/Mini_truck.bmp", "images/Mini_van.bmp",
                                               "images/taxi.bmp", "images/truck.bmp", ]))
        self.rect = self.image.get_rect()
        self.rect.top = road.rect.top
        self.rect.left = road.rect.left + 100

        # Store y pos as decimal.
        self.y = float(self.rect.top)

    def update(self):
        """Update vehicles pos."""
        self.rect.top += self.ai_settings.vehicle_speed

    def blitme(self):
        """Draw vehicles to screen."""
        self.screen.blit(self.image, self.rect)
