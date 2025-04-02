import numpy as np
import abc
from . import object3d
from .models.spongebob import sponge_bob

class SpongeBob(object3d.Object3d):
    def __init__(self):
        super().__init__(
            model=sponge_bob,
            position=[-0.5, -0.1, -0.5],
            scale=0.3, 
            angles=[-np.pi/4, np.pi/4, 0]
        )

    def key_event(self, key):
        if key == 88: 
            self.scale += 0.01
            self.position[1] += 0.01
        if key == 90: 
            self.scale -= 0.01
            self.position[1] -= 0.01

        if self.scale >= 0.7 and self.position[1] >= 0.3:
            self.scale = 0.7
            self.position[1] = 0.3
        

        
        if self.scale <= 0.06 and self.position[1] <= -0.34:
            self.scale = 0.06
            self.position[1] = -0.34
 
