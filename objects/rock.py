import numpy as np
import abc
from . import object3d
from .models.rock import rock


class Rock(object3d.Object3d):
    def __init__(self):
        super().__init__(
            model=rock,
            scale=0.3, 
            angles=[-np.pi/4, np.pi/4, 0]
        )
