import numpy as np
import abc
from . import object3d
from .models.spongebob import sponge_bob

class SpongeBob(object3d.Object3d):
    def __init__(self):
        super().__init__(
            model=sponge_bob,
            scale=0.3, 
            angles=[-np.pi/4, np.pi/4, 0]
        )

    def key_event(self, key):
        if key == 88: self.scale += 0.01
        if key == 90: self.scale -= 0.01
    
    def draw(self, program, loc_color):
        self.angles[1] += 0.01
        super().draw(program, loc_color)

 
