# Libraries we will use
import pygame
import math

# Library to get the starting information for the Planets
# X, Y coords and X, Y Velocity: in AUs
from astroquery.jplhorizons import Horizons
from astropy.time import Time


def main():
    # Setting up the Pygame window and items
    pygame.init()
    win = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    pygame.display.set_caption("Planet Simulation")
    clock = pygame.time.Clock()

    # Setting up information for planet simulation.
    start_date = "2022-07-18"

    sun = Solor_Object("0", start_date, 30, Color.yellow, 1.98847 * 10 ** 30, sun=True)
    mercury = Solor_Object("1", start_date, 8, Color.grey, 3.285 * 10 ** 23)
    venus = Solor_Object("2", start_date, 16, Color.orange, 4.867 * 10 ** 24)
    earth = Solor_Object("3", start_date, 16, Color.blue, 5.972 * 10 ** 24)
    mars = Solor_Object("4", start_date, 12, Color.red, 6.39 * 10 ** 23)
    jupiter = Solor_Object("5", start_date, 20, Color.orange, 1.898 * 10 ** 27)
    saturn = Solor_Object("6", start_date, 19, Color.blue, 5.683 * 10 ** 26)
    uranus = Solor_Object("7", start_date, 17, Color.blue, 8.681 * 10 ** 25)
    neptune = Solor_Object("8", start_date, 17, Color.blue, 1.024 * 10 ** 26)

    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    run = True
    while run:
        clock.tick(60)

        win.fill(Color.black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(win)

        pygame.display.update()
    
    pygame.quit()


class Solor_Object:
    """Class that builds and holds information for solar objects. """

    def __init__(self, id, date, radius, color, mass, sun=False):
            self.radius = radius
            self.color = color
            self.mass = mass

            self.orbit = []
            self.sun = sun
            self.distance_to_sun = 0

            self.vectors = self.get_starting_vectors(id, date)
            self.x = self.vectors["x"][-1] * Constants.AU # m
            self.y = self.vectors["y"][-1] * Constants.AU # m
            self.x_vel = self.vectors["vx"][-1] * Constants.AU / 24 / 3600 # m/s
            self.y_vel = self.vectors["vy"][-1] * Constants.AU / 24 / 3600 # m/s

    def get_starting_vectors(self, body_id, date):
        tdb_time = Time(date).jd1
        obj = Horizons(id=body_id, location="@Sun", epochs=tdb_time)
        return obj.vectors()

    def draw(self, win):
        x = self.x * Constants.SCALE + Constants.WIDTH / 2
        y = self.y * Constants.SCALE + Constants.WIDTH / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                point_x, point_y = point
                point_x = point_x * Constants.SCALE + Constants.WIDTH / 2
                point_y = point_y * Constants.SCALE + Constants.HEIGHT / 2
                updated_points.append((point_x, point_y))

            pygame.draw.lines(win, self.color, False, updated_points, 1)

        pygame.draw.circle(win, self.color, (x, y), self.radius / Constants.WIN_EDGE_FROM_SUN)

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
    WIN_EDGE_FROM_SUN = 10 # how many AUs is the Edge of the window
    
    AU = 149597870700
    G = 6.67430e-11
    SCALE = WIDTH / 2 / WIN_EDGE_FROM_SUN / AU # Sets AU to pixels
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
