
import pygame
import numpy as np
import matplotlib.pyplot as plt

vonmises_dispersion = 10

class Corr_Random_Walker:
    def __init__(self, x, y):

        self.position = pygame.Vector2(x,y)
        vec = np.array([1 * np.cos(np.random.randint(0, 360, 1)), 1 * np.sin(np.random.randint(0, 360, 1))])
        self.velocity = pygame.Vector2(*vec)
        self.random_von_mises_value = float(np.degrees(np.random.vonmises(0, vonmises_dispersion, 1)))

    def define_new_velocity(self):

        self.random_von_mises_value = float(np.degrees(np.random.vonmises(0, vonmises_dispersion, 1)))
        self.velocity = self.velocity.rotate(self.random_von_mises_value)

    def move(self):

        self.position += self.velocity

Agents = Corr_Random_Walker( x= 0, y = 0)

X_Coordinates = []
Y_Coordinates = []
for i in range(1000):
    Agents.define_new_velocity()
    Agents.move()
    X_Coordinates.append(Agents.position.x)
    Y_Coordinates.append(Agents.position.y)

plt.plot(X_Coordinates, Y_Coordinates)
plt.legend()
plt.show()