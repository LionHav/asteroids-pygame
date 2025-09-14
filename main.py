import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt=0 #delta time
    clock=pygame.time.Clock()

    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()

    Player.containers =(updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers =(updatable)
    Shot.containers = (shots,updatable,drawable)
    
    asteroid_field = AsteroidField()
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        for obj in asteroids:
            if player.check_collission(obj) == True:
                print('Game over!')
                sys.exit()
        
        for obj in asteroids:
            for bullet in shots:
                if obj.check_collission(bullet) == True:
                    obj.split()
                    bullet.kill()

        # limit the framerate to 60 FPS
        dt=clock.tick(60)/1000

if __name__ == "__main__":
    main()
