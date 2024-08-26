# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group() #all objects that can be updated
    drawable = pygame.sprite.Group() #all objects that can be drawn
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid_group, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shot_group, updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    while True:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroid_group:
            if asteroid.has_collided(player):
                print("Game Over!")
                sys.exit()

        for obj in drawable:
            obj.draw(screen)
    
        pygame.display.flip()
        dt = clock.tick(60) / 1000 #returns the delta time

if __name__ == "__main__":
    main()


