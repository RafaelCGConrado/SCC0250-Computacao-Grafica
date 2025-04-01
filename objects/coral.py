import numpy as np
import abc
from . import object3d
from .models.coral import coral


class Coral(object3d.Object3d):
    def __init__(self, x=0, y = -0.2, z = 0.5):
        super().__init__(
            model=coral,
            position=[x, y, z],
            scale=0.25, 
            angles=[-np.pi/4, np.pi/4, 0]
        )

