import numpy as np
import abc
from object3d import Object3d

class SpongeBob(Object3d):
    def key_event(self, key):
        if key == 262: self.position[0] += 0.01 #esquerda
        if key == 263: self.position[0] -= 0.01 #esquerda

        if key == 65: self.angles[1] += 0.01
        if key == 83: self.angles[1] -= 0.01
        if key == 88: self.angles[0] += 0.01
        if key == 90: self.angles[0] -= 0.01
 
