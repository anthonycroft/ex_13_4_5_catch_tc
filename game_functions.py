import sys

import pygame
from random import randint

def check_events(catcher):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, catcher)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, catcher)

def check_keydown_events(event, catcher):
    """respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = True
    elif event.key == pygame.K_LEFT:
        catcher.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, catcher):
    """respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = False
    if event.key == pygame.K_LEFT:
        catcher.moving_left = False

def update_screen(ai_settings, screen, ball, catcher):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    catcher.blitme()
    ball.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()


def update_ball(ai_settings, ball, catcher):
    """
    Update the position of the ball.
    """
    ball.rect.y += ai_settings.ball_drop_speed

    # Reset the ball's position if it moves off the screen
    if ball.rect.top >= ai_settings.screen_height:
        ball.rect.bottom = 0
        ball.rect.x = randint(0, ball.screen_rect.width - ball.rect.width)
        # ai_settings.ball_drop_speed += 0.1  # Increase speed each time the ball resets

    check_ball_caught(ball, catcher)


def check_ball_caught(ball, catcher):
    """Respond to ball-catcher collisions."""
    # reposition ball at top of screen at a random x-coordinate
    if catcher.rect.colliderect(ball.rect):
        ball.rect.bottom = 0
        ball.rect.x = randint(0, ball.screen_rect.width - ball.rect.width)
