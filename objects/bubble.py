from OpenGL.GL import *
import numpy as np
import abc
from . import object3d
from .models.bubble import bubble

#Classe para os corais decorativos que ocupam o fundo da cena.
class Bubble(object3d.Object3d):
    #É possível escolher a posição de cada coral por meio dos parâmetros
    def __init__(self, velocity):
        self.x_vary = 0
        self.velocity = velocity
        super().__init__(
            model=bubble,
            position=[np.random.uniform(-1, 1), np.random.uniform(-1, 1), -1],
        )
    def draw(self, program, loc_color):
        self.position[1] += self.velocity
        self.x_vary += 0.1
        if self.position[1] >= 1.5:
            self.position[1] = -1
            self.position[0] = np.random.uniform(-1, 1)
        self.position[0] += 0.005*np.sin(self.x_vary + self.velocity) 
        super().draw(program, loc_color, draw_type=GL_TRIANGLE_FAN)

