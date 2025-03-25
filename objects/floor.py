import numpy as np
import abc
from .object3d import Object3d
from .models.floor import floor

class Floor(Object3d):
    def __init__(self):
        super().__init__(
            model=floor, 
            position=[0, -0.5, 0.5], 
            angles=[np.pi/4, 0, 0],
            scale=2
        )
    

    def key_event(self, key):
        if key == 89: self.angles[0] += 0.01
 

