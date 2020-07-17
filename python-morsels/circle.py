"""This week I want you to make a class that represents a circle.

The circle should have a radius, a diameter, and an area. It should also have
a nice string representation.

For example:

>>> c = Circle(5)
>>> c
Circle(5)
>>> c.radius
5
>>> c.diameter
10
>>> c.area
78.53981633974483
Additionally the radius should default to 1 if no radius is specified when you
create your circle:"""


import math


class Circle:
    """Class representing a circle with radius, area, and diameter."""

    def __init__(self, radius=1):
        self.radius = radius

    @property
    def radius(self):
        """Gets or sets a value indicating circle's radius."""
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")

        self.__radius = radius

    @property
    def diameter(self):
        """Gets or sets a value indicating circle's diameter."""
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        """Gets a value indicating circle's area."""
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f"{type(self).__name__}({self.radius!r})"
