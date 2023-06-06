import pygame
import math

# Library to get the starting information for the Planets
# X, Y coords and X, Y Velocity: in AUs
from astroquery.jplhorizons import Horizons
from astropy.time import Time

from helpers import Constants


class SolarObject:
    """Class that builds and holds information for solar objects. """

    def __init__(self, id, date, radius, color, mass, sun=False):
            self.radius = radius
            self.color = color
            self.mass = mass

            self.orbit = []
            self.sun = sun
            self.distance_to_sun = 0

            self.vectors = self.get_starting_vectors(id, date)
            self.x = self.vectors["x"][-1] * Constants.AU # meters
            self.y = self.vectors["y"][-1] * Constants.AU # meters
            self.x_vel = self.vectors["vx"][-1] * Constants.AU / 24 / 3600 # m/s
            self.y_vel = self.vectors["vy"][-1] * Constants.AU / 24 / 3600 # m/s

    def get_starting_vectors(self, body_id, date):
        tdb_time = Time(date).jd1
        obj = Horizons(id=body_id, location="@Sun", epochs=tdb_time)
        return obj.vectors()

    def draw(self, win):
        x = self.x * Constants.SCALE + Constants.WIDTH / 2
        y = self.y * Constants.SCALE + Constants.HEIGHT / 2

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
        # a = (a**2 + b**2)**(1/2) Distance to Sun
        distance_x = other.x - self.x
        distance_y = other.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        # F = G(m1m2)/(r**2)
        force = Constants.G * self.mass * other.mass / distance ** 2
        # Break Force into x and y component 
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

        #f=ma > f=mv/t > v=f/m*t
        self.x_vel += total_force_x / self.mass * Constants.TIMESTEP
        self.y_vel += total_force_y / self.mass * Constants.TIMESTEP
        
        self.x += self.x_vel * Constants.TIMESTEP
        self.y += self.y_vel * Constants.TIMESTEP
        self.orbit.append((self.x, self.y))

