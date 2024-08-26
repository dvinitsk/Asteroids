from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill() #this asteroid is destroyed, we may spawn new ones
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20, 50) #new angle for the split asteroids
        velocity_1 = self.velocity.rotate(new_angle)
        velocity_2 = self.velocity.rotate(-new_angle)
        
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid1.velocity = velocity_1 * 1.2
        asteroid2.velocity = velocity_2 * 1.2
