from OpenGL.GL import *
import numpy as np
import abc
from . import object3d
from .models.bubble import bubble

#Classe para os corais decorativos que ocupam o fundo da cena.
class Bubble(object3d.Object3d):
    #É possível escolher a posição de cada coral por meio dos parâmetros
    def __init__(self, x=0, y=0, z=-0.5):
        super().__init__(
            model=bubble,
            position=[x, y, z],
        )
    def draw(self, program, loc_color):
        super().draw(program, loc_color, draw_type=GL_TRIANGLE_FAN)

