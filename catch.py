import pygame
from settings import Settings
from catcher import Catcher
from ball import Ball
import game_functions as gf

def run_game():
    # Initialise pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Catch")

    # Make a ship, a group of bullets and a group of aliens.
    catcher = Catcher(ai_settings, screen)
    ball = Ball(ai_settings, screen)

    clock = pygame.time.Clock()

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(catcher)
        catcher.update()
        gf.update_ball(ai_settings, ball, catcher)
        gf.update_screen(ai_settings, screen, ball, catcher)

        clock.tick(1000)  # Limit to 60 frames per second

run_game()