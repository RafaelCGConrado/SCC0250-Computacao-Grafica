import numpy as np
import abc
from . import object3d
from .models.rock import rock

#Classe para os objetos pedras. Puramente decorativas.
class Rock(object3d.Object3d):
    #É possível escolher por meio dos parâmetros em qual posição (coordenadas) 
    #cada objeto Pedra será gerado na cena
    def __init__(self, x=0, y=0, z=0.2, angle=0, scale=0.2):
        super().__init__(
            model=rock,
            position=[x, y, z],
            scale=scale, 
            angles=[-np.pi/4, np.pi/4, angle]
        )
