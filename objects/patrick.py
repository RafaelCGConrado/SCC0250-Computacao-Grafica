import numpy as np
import abc
from . import object3d
from .models.patrick import patrick


class Patrick(object3d.Object3d):
    def __init__(self):
        super().__init__(
            model=patrick,
            scale=0.3, 
            position=[0.5, -0.1, 0],
            angles=[-np.pi/4, -np.pi/4, 0]
        )


    def key_event(self, key):
        if key == 262: self.position[0] += 0.01 #esquerda
        if key == 263: self.position[0] -= 0.01 #esquerda
