import numpy as np
import abc
from . import object3d
from .models.flower import flower

#Classe para o objeto do Patrick.
#Este personagem anda para frente (translada) e vira para os lados (rotaciona)
class Flower(object3d.Object3d):
    def __init__(self,x=0, y=0, z=0):
        super().__init__(
            model=flower,
            scale=0.3, 
            position=[x, y, z],
            angles=[-np.pi/4, -0.0353, 0]
        )
    
            
    