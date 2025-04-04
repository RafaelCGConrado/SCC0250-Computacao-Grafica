from . import object3d
from .models.hook1 import hook1
import math

#Classe para o anzol 1 da cena.
#Ele oscila (sobe e desce) continuamente e não é
#controlável pelo usuário.
class Hook1(object3d.Object3d):
    def __init__(self):
        self.ocilate = 0
        super().__init__(
            model=hook1,
            position=[0, 0.6, 0]
        )

    def draw(self, program, loc_color, delta_time):
        self.ocilate += 0.01
        self.position[1] = math.sin(self.ocilate)/10 + 0.3
        super().draw(program, loc_color, delta_time)

