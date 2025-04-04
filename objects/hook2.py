from . import object3d
from .models.hook2 import hook2
import math

#Classe para o segundo anzol da cena. Apesar de sua aparência
#ser diferente do primeiro, ele também oscila continuamente
#sem interferência do usuário.
class Hook2(object3d.Object3d):
    def __init__(self):
        self.ocilate = 0
        super().__init__(
            model=hook2,
            position=[0.3, 0.6, 0]
        )

    def draw(self, program, loc_color, delta_time):
        self.ocilate += delta_time
        self.position[1] = math.sin(self.ocilate + 0.5)/10 + 0.3
        super().draw(program, loc_color, delta_time)

