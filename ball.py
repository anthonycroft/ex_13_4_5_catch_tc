import pygame
from pygame.examples.testsprite import screen_dims
from random import randint

class Ball():
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialise the ball and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ball image and set its rect attribute
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start the ball at a random horizontal position at the top of the screen
        self.rect.x = randint(0, self.screen_rect.width - self.rect.width)
        self.rect.bottom = self.screen_rect.top  # Start at the top of the screen

    def blitme(self):
        """draw the ball at its current location"""
        self.screen.blit(self.image, self.rect)



