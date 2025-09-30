import random
import pygame
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Randomise the angle of the asteroid split
        random_angle = random.uniform(20, 50)
        
        # Two new vectors for the split asteroids
        vector_1 = self.velocity.rotate(random_angle)
        vector_2 = self.velocity.rotate(-random_angle)
        
        # Generate the split asteroid objects
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = vector_1 * 1.2
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = vector_2 * 1.2
