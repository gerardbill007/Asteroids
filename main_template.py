import pygame
from player import Player
from asteroid import Asteroid

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    # SpriteGroups
    all_sprites = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Wire containers so new instances auto-add to groups
    from circleshape import CircleShape
    CircleShape.containers = (all_sprites, drawable)

    # Create objects (auto-added to groups)
    player = Player(400, 300)
    rock = Asteroid(100, 100, vx=120, vy=40)

    dt = 0.0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Group update
        for sprite in all_sprites:
            sprite.update(dt)

        # Render
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()