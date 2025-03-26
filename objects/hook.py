from . import object3d
from .models.hook import hook
import math
class Hook(object3d.Object3d):
    def __init__(self):
        self.ocilate = 0
        super().__init__(
            model=hook,
            position=[0, 0.6, 0]
        )

    def draw(self, program, loc_color):
        self.ocilate += 0.01
        self.position[1] = math.sin(self.ocilate)/10 + 0.3
        super().draw(program, loc_color)

