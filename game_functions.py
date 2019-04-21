import pygame
import json
import sys
from road_stripes import Stripes
from traffic import Traffic
from random import shuffle, randint, sample
from time import sleep


def check_keydown_events(event, car):
    """Check which key has been pressed."""
    if event.key == pygame.K_RIGHT:
        car.moving_right = True
    elif event.key == pygame.K_LEFT:
        car.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, car):
    """Check which key has been unpressed.(lol)"""
    if event.key == pygame.K_RIGHT:
        car.moving_right = False
    elif event.key == pygame.K_LEFT:
        car.moving_left = False


def check_event(car, play_button, stats, stripes, road, screen, ai_settings, traffic, sb):
    """Check screen events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, car)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, car)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            start_game(car, play_button, stats, stripes, road, screen, ai_settings, traffic, mouse_x, mouse_y, sb)


def start_game(car, play_button, stats, stripes, road, screen, ai_settings, traffic, mouse_x, mouse_y, sb):
    """Start game."""
    mouse_button = play_button.rect.collidepoint(mouse_x, mouse_y)
    if mouse_button and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        sb.prep_score()
        sb.prep_highscore()
        sb.prep_cars()
        traffic.empty()
        stripes.empty()
        create_stripes(stripes, road, screen, ai_settings)
        create_traffic(traffic, screen, ai_settings, road)
        car.center()
        stats.game_active = True


def total_stripes(road, screen, ai_settings):
    """calculate total stripes from available height."""
    stripe = Stripes(road, screen, ai_settings)
    num_stripes = road.rect.height / stripe.rect.height + 30
    return num_stripes


def create_stripes(stripes, road, screen, ai_settings):
    num_stripes = int(total_stripes(road, screen, ai_settings))
    for num in range(num_stripes):
        stripe = Stripes(road, screen, ai_settings)
        stripe.rect.y = ((stripe.rect.height + 60) * num)
        stripes.add(stripe)


def update_screen(screen, ai_settings, road, car, stripes, traffic, play_button, stats, sb):
    """Update screen."""
    screen.fill(ai_settings.bg_color)
    # show score
    sb.show_score()
    # Draw road.
    road.draw()
    # Draw stripes.
    for stripe in stripes.sprites():
        stripe.draw()
    # draw car
    car.blitme()
    # Draw traffic.
    traffic.draw(screen)
    # Draw button if game inactive.
    if not stats.game_active:
        play_button.show_button()
    pygame.display.flip()


def update_stripes(stripes, road, screen, ai_settings):
    # update stripe pos
    stripes.update()
    # remove stripes that hit edge.
    check_stripe_edge(stripes, road, screen, ai_settings)


def check_stripe_edge(stripes, road, screen, ai_settings):
    """Check if stripe has hit edge."""
    for stripe in stripes.copy():
        if stripe.rect.top == road.rect.bottom:
            stripes.remove(stripe)
            sts = Stripes(road, screen, ai_settings)
            sts.rect.bottom = road.rect.top - 60
            stripes.add(sts)


def set_y_pos(traffic, road):
    """Set y-cor of vehicle."""
    # Get all cars index
    car_nums = [0, 1, 2, 3]
    shuffle(car_nums)
    # Sample only three index.
    sample_value = randint(1, 3)
    cars = sample(car_nums, sample_value)
    # Get height to add to original height.
    height = randint(210.0, 230.0)
    for value in cars:
        """ Get car using value as index"""
        car = traffic.sprites()[value]
        car.rect.y = -10 - height


def create_traffic(traffic, screen, ai_settings, road):
    """Create vehicles for traffic."""
    for i in range(4):
        new_car = Traffic(screen, ai_settings, road)
        traffic.add(new_car)
    shuffle(list(traffic))
    for num, car in enumerate(traffic):
        car.rect.x = road.rect.left + randint(35, 40) + (car.rect.width + randint(45, 55)) * num
    set_y_pos(traffic, road)


def check_vehicle_bottom(traffic, road):
    """Check if vehicle has past edge of screen."""
    for vehicle in traffic.copy():
        if vehicle.rect.top == road.rect.bottom:
            traffic.remove(vehicle)


def remove_vehicles(car, traffic, screen, ai_settings, road, stats, filename, sb):
    """Remove vehicles that are past bottom of screen."""
    check_vehicle_bottom(traffic, road)
    # check if traffic is empty and create new vehicles.
    if len(traffic) == 0:
        ai_settings.speed_up()
        stats.score += ai_settings.score
        sb.prep_score()
        check_high_score(stats, filename)
        sb.prep_highscore()
        create_traffic(traffic, screen, ai_settings, road)
        add_car_ycor(car, ai_settings)


def check_high_score(stats, filename):
    """Check high score against score."""
    if stats.score > stats.highscore:
        stats.highscore = stats.score
        with open(filename, 'w') as f_obj:
            json.dump(stats.highscore, f_obj)


def check_collision(traffic, car, screen, ai_settings, road, stats, sb):
    """Checks if traffic hit car."""
    if pygame.sprite.spritecollideany(car, traffic):
        stats.car_limit -= 1
        sb.prep_cars()
        traffic.empty()
        sleep(0.5)
        car.center()
        create_traffic(traffic, screen, ai_settings, road)
    end_game(stats, ai_settings)


def add_car_ycor(car, ai_settings):
    """Add forward movement to car."""
    car.rect.y -= ai_settings.meters


def end_game(stats, ai_settings):
    """Check if all cars have crushed."""
    if stats.car_limit < 0:
        pygame.mouse.set_visible(True)
        stats.game_active = False


def update_traffic(traffic, screen, ai_settings, road, car, stats, filename, sb):
    """Update vehicles pos."""
    for vehicle in traffic.sprites():
        vehicle.update()
    remove_vehicles(car, traffic, screen, ai_settings, road, stats, filename, sb)
    check_collision(traffic, car, screen, ai_settings, road, stats, sb)
