import pygame.font


class Button():
    """A class to manage the score board."""

    def __init__(self, screen, stats, msg):
        """Initiate class attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.button_color = 0, 255, 0
        self.text_color = 255, 255, 255
        self.font = pygame.font.SysFont(None, 48)

        # Create button.
        self.width, self.height = 200, 50
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep(msg)

    def prep(self, msg):
        """Create a rendered image of msg."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def show_button(self):
        """Draw image to screen."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
