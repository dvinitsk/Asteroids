# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group() #all objects that can be updated
    drawable = pygame.sprite.Group() #all objects that can be drawn

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)
    
        pygame.display.flip()
        dt = clock.tick(60) / 1000 #returns the delta time

if __name__ == "__main__":
    main()


