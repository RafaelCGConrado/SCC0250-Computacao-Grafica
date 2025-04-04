from OpenGL.GL import *
import numpy as np
import abc
from . import object3d
from .models.flower import flower
import copy

#Classe para o objeto do Patrick.
#Este personagem anda para frente (translada) e vira para os lados (rotaciona)
class Flower(object3d.Object3d):
    def __init__(self,x=0, y=0, z=0, color=None):
        model_copy = copy.deepcopy(flower)

        if color:
            model_copy["color"]["body"] = color
    

        super().__init__(
            model=model_copy,
            scale=0.3, 
            position=[x, y, z],
            angles=[-np.pi/4, -0.0353, 0]
        )
    def draw(self, program, loc_color, delta_time):
        super().draw(program, loc_color, delta_time, draw_type=GL_LINE_STRIP)

            
    