import pygame
import random
from circleshape import *
from constants import *
from logger import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        asteroid_one_velocity = self.velocity.rotate(angle)
        asteroid_two_velocity = self.velocity.rotate(-angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_one.velocity = asteroid_one_velocity * 1.2
        asteroid_two.velocity = asteroid_two_velocity * 1.2
    


