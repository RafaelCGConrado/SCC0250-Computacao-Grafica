import numpy as np
import abc
from . import object3d
from .models.patrick import patrick


class Patrick(object3d.Object3d):
    def __init__(self):
        super().__init__(
            model=patrick,
            scale=0.3, 
            angles=[-np.pi/4, np.pi/4, 0]
        )


    def key_event(self, key):
        # if key == 262: self.position[0] += 0.01 #esquerda
        # if key == 263: self.position[0] -= 0.01 #esquerda

        if key == 74: self.angles[1] += 0.01
        if key == 75: self.angles[1] -= 0.01
        # if key == 88: self.angles[0] += 0.01
        # if key == 90: self.angles[0] -= 0.01

        # print(self.angles[1])

    # def draw(self, program, loc_color):
    #     self.angles[1] += 0.01
    #     super().draw(program, loc_color)
 
