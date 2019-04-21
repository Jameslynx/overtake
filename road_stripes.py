import pygame
from pygame.sprite import Sprite


class Stripes(Sprite):
    """A class to manage stripes."""

    def __init__(self, road, screen, ai_settings):
        """Initiate stripes attributes."""
        super().__init__()

        self.screen = screen
        self.color = ai_settings.stripe_color
        self.ai_settings = ai_settings

        # Create stripes and set pos.
        self.rect = pygame.Rect(0, 0, ai_settings.stripe_width, ai_settings.stripe_height)
        self.rect.centerx = road.rect.centerx
        self.rect.top = road.rect.top

    def update(self):
        # Update self.rect.y
        self.rect.y += self.ai_settings.road_speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
