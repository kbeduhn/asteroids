import pygame
from constants import *
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_event
import sys
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # new groups for player and containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # create a new group for the asteroids & containers
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

   # new group for the asteroid field & containers
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    # shots group
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    # initialize pygame
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x, y)

    # create the screen object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # the game loop
    while True:
        log_state()
    # handle events (like clicking "x" to close)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60)/1000

        # player update
        updatable.update(dt)

    # collision check
        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!", file=sys.stderr)
                sys.exit()

    # collision check 2
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        # fill screen
        screen.fill("black")

        # draw the player
        for obj in drawable:
            obj.draw(screen)

        # refresh the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
