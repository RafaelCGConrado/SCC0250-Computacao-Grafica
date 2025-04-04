import numpy as np
import abc
from .object3d import Object3d
from .models.floor import floor

#Classe para o Chão (areia) da cena.
class Floor(Object3d):
    def __init__(self):
        super().__init__(
            model=floor,
            scale=2, 
            position=[0, 0.2, 1], 
            angles=[np.pi/4, 0, 0],
        )
    

