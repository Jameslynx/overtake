import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf
from road import Road
from car import Car
from gamestats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    """Main game function"""

    filename = "Highscore.json"

    # initiate pygame and create screen.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Overtake!')

    # create road, car and traffic.
    road = Road(screen, ai_settings)
    car = Car(road, screen, ai_settings)
    stripes = Group()
    traffic = Group()

    # create stripes and traffic.
    gf.create_stripes(stripes, road, screen, ai_settings)
    gf.create_traffic(traffic, screen, ai_settings, road)

    # Initiatialize game statistics
    stats = GameStats(ai_settings, filename)

    # Create Button.
    play_button = Button(screen, stats, "Play")
    sb = Scoreboard(ai_settings, screen, stats, road)

    while True:
        """Main game loop"""
        gf.check_event(car, play_button, stats, stripes, road, screen, ai_settings, traffic, sb)
        if stats.game_active:
            car.update()
            gf.update_traffic(traffic, screen, ai_settings, road, car, stats, filename, sb)
            gf.update_stripes(stripes, road, screen, ai_settings)
        gf.update_screen(screen, ai_settings, road, car, stripes, traffic, play_button, stats, sb)


run_game()
