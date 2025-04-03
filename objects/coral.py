import numpy as np
import abc
from . import object3d
from .models.coral import coral

#Classe para os corais decorativos que ocupam o fundo da cena.
class Coral(object3d.Object3d):
    #É possível escolher a posição de cada coral por meio dos parâmetros
    def __init__(self, x=0, y=0, z=0.4):
        super().__init__(
            model=coral,
            position=[x, y, z],
            scale=0.25, 
            angles=[-np.pi/4, np.pi/4, 0]
        )

