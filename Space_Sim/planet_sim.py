# Libraries we will use
import pygame

from solar_object import SolarObject
from helpers import Constants, Color


def main():
    # Setting up the Pygame window and items
    pygame.init()
    win = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    pygame.display.set_caption("Planet Simulation")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("monospace", 40)

    # Setting up information for planet simulation.
    start_date = "2022-07-18"

    sun = SolarObject("0", start_date, 30, Color.YELLOW, 1.98847 * 10 ** 30, sun=True)
    mercury = SolarObject("1", start_date, 8, Color.GREY, 3.285 * 10 ** 23)
    venus = SolarObject("2", start_date, 16, Color.ORANGE, 4.867 * 10 ** 24)
    earth = SolarObject("3", start_date, 16, Color.BLUE, 5.972 * 10 ** 24)
    mars = SolarObject("4", start_date, 12, Color.RED, 6.39 * 10 ** 23)
    jupiter = SolarObject("5", start_date, 20, Color.ORANGE, 1.898 * 10 ** 27)
    saturn = SolarObject("6", start_date, 19, Color.BLUE, 5.683 * 10 ** 26)
    uranus = SolarObject("7", start_date, 17, Color.BLUE, 8.681 * 10 ** 25)
    neptune = SolarObject("8", start_date, 17, Color.BLUE, 1.024 * 10 ** 26)

    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    elapsed_time = 0

    run = True
    while run:
        clock.tick(30)

        win.fill(Color.BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(win)

        elapsed_time += 1
        label = font.render(f"Day: {elapsed_time}", 1, (0, 255, 255))
        win.blit(label, (10, 10))
        pygame.display.update()
        
    
    pygame.quit()


if __name__ == "__main__":
    main()
