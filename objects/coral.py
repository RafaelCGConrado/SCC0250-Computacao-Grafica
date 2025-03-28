import numpy as np
import abc
from . import object3d
from .models.coral import coral


class Coral(object3d.Object3d):
    def __init__(self):
        super().__init__(
            model=coral,
            scale=0.3, 
            angles=[-np.pi/4, np.pi/4, 0]
        )

