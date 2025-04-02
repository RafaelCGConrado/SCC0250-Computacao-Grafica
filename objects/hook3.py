from . import object3d
from .models.hook1 import hook1
import math

class Hook3(object3d.Object3d):
    def __init__(self):
        self.ocilate = 0
        super().__init__(
            model=hook1,
            position=[-0.3, 0.6, 0]
        )

    def key_event(self, key):
        if key == 81: self.position[1] -= 0.01
        if key == 65: self.position[1] += 0.01
        if self.position[1] <= 0:
            self.position[1] = 0
        elif self.position[1] >= 1.22:
            self.position[1] = 1.22