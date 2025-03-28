from . import object3d
from .models.hook2 import hook2
import math

class Hook2(object3d.Object3d):
    def __init__(self):
        self.ocilate = 0
        super().__init__(
            model=hook2,
            position=[0.3, 0.6, 0]
        )

    def draw(self, program, loc_color):
        self.ocilate += 0.01
        self.position[1] = math.sin(self.ocilate + 0.5)/10 + 0.3
        super().draw(program, loc_color)

