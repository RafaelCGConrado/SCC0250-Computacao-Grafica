import numpy as np
import abc
from .object3d import Object3d
from .models.floor import floor

class Floor(Object3d):
    def __init__(self):
        super().__init__(
            model=floor,
            scale=1.2, 
            position=[0, -0.6, 0.6], 
            angles=[np.pi/3, 0, 0],
        )
    

    def key_event(self, key):
        if key == 89: self.angles[0] += 0.01
 

