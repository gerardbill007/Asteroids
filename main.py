import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    delta_time = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill display surface with solid background colour
        screen.fill((0, 0, 0))
        # Draw player to the screen
        player.draw(screen)
        # Funtion to update the entire display screen
        pygame.display.flip()
        
        # Limit the games's fps to 60
        delta_time = clock.tick(60) / 1000

        
if __name__ == "__main__":
    main()
