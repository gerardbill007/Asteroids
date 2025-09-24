import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Sprite Groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    # Containers
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    delta_time = 0.0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Group update
        updateable.update(delta_time)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        # Render
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        
        # Limit the games's fps to 60
        delta_time = clock.tick(60) / 1000
        
        
if __name__ == "__main__":
    main()
