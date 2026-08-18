
import pygame
import constants
import sys
from asteroidfield import AsteroidField
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from shot import Shot



def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0.0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    radius = constants.PLAYER_RADIUS
    player = Player(x, y, constants.PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"""
        Screen width: {constants.SCREEN_WIDTH}
        Screen height: {constants.SCREEN_HEIGHT}
    """)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill("black")
        updatable.update(dt)
        for thing in asteroids:
            if player.collides_with(thing):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(thing):
                    log_event("asteroid_shot")
                    thing.split()
                    shot.kill()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    print("frame")
    main()
