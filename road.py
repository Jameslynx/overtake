import pygame


class Road():
    """A class to manage road."""

    def __init__(self, screen, ai_settings):
        """set road attributes."""
        self.screen = screen
        self.ai_settings = ai_settings
        self.color = ai_settings.road_color
        self.screen_rect = screen.get_rect()

        # Create road and set pos.
        self.rect = pygame.Rect(0, 0, ai_settings.road_width, ai_settings.road_height)
        self.rect.top = self.screen_rect.top
        self.rect.left = self.screen_rect.left + 500

    def draw(self):
        """Draw road to screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
