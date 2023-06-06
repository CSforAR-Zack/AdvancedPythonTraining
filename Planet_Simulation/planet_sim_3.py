import pygame
import math

def main():
    pygame.init()
    win = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    pygame.display.set_caption("Planet Simulation")
    font = pygame.font.SysFont("comicsans", 16)

    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, Color.yellow, 1.98847 * 10 ** 30)
    sun.sun = True

    earth = Planet(-1 * Constants.AU, 0, 16, Color.blue, 5.972 * 10 ** 24)
    earth.y_vel = 29.783 * 1000 
    mars = Planet(-1.524 * Constants.AU, 0, 12, Color.red, 6.39 * 10 ** 23)
    mars.y_vel = 24.077 * 1000
    venus = Planet(-.7 * Constants.AU, 0, 16, Color.orange, 4.867 * 10 ** 24)
    venus.y_vel = 35.02 * 1000
    mercury = Planet(-.4 * Constants.AU, 0, 8, Color.grey, 3.285 * 10 ** 23)
    mercury.y_vel = 47.4 * 1000

    planets = [sun, earth, mars, venus, mercury]

    while run:
        clock.tick(60)

        win.fill(Color.black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(win, font)

        pygame.display.update()
    
    pygame.quit()


class Planet:
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win, font):
        x = self.x * Constants.SCALE + Constants.WIDTH / 2
        y = self.y * Constants.SCALE + Constants.HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                point_x, point_y = point
                point_x = point_x * Constants.SCALE + Constants.WIDTH / 2
                point_y = point_y * Constants.SCALE + Constants.HEIGHT / 2
                updated_points.append((point_x, point_y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

        if not self.sun:
            distance = round(self.distance_to_sun / 1000, 1)
            distance_text = font.render(f"{distance} km", 1, Color.white)
            win.blit(distance_text, (x - distance_text.get_width() / 2, y))

    def attraction(self, other):
        distance_x = other.x - self.x
        distance_y = other.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = Constants.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self, planets):
        total_force_x = total_force_y = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_force_x += fx
            total_force_y += fy

        self.x_vel += total_force_x / self.mass * Constants.TIMESTEP
        self.y_vel += total_force_y / self.mass * Constants.TIMESTEP

        self.x += self.x_vel * Constants.TIMESTEP
        self.y += self.y_vel * Constants.TIMESTEP
        self.orbit.append((self.x, self.y))


class Constants:
    WIDTH = 800
    HEIGHT = 800

    AU = 149597870700
    G = 6.67430e-11
    SCALE = 250 / AU # 1AU = 100 pixels
    TIMESTEP = 3600 * 24 # 1 Day


class Color:
    black = (0, 0, 0)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    orange = (255, 120, 0)
    grey = (200, 200, 200)


if __name__ == "__main__":
    main()