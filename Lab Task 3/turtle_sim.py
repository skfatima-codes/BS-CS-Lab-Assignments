
import math

class Turtle:
    def __init__(self, x=100.0, y=100.0, angle=0.0):
        self.x = x
        self.y = y
        self.angle = angle
        self.path = [(x, y)]

    def forward(self, distance=20.0):
        rad = math.radians(self.angle)
        self.x += distance * math.cos(rad)
        self.y += distance * math.sin(rad)
        self.path.append((self.x, self.y))
        print(f"Forward to ({self.x:.1f}, {self.y:.1f})")

    def turn_left(self, degrees=90):
        self.angle = (self.angle + degrees) % 360
        print(f"Turn left to {self.angle}°")

    def turn_right(self, degrees=90):
        self.angle = (self.angle - degrees) % 360
        print(f"Turn right to {self.angle}°")
