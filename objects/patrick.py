import numpy as np
import abc
from . import object3d
from .models.patrick import patrick

#Classe para o objeto do Patrick.
#Este personagem anda para frente (translada) e vira para os lados (rotaciona)
class Patrick(object3d.Object3d):
    def __init__(self):
        super().__init__(
            model=patrick,
            scale=0.3, 
            position=[0.5, -0.2, 0],
            angles=[-np.pi/4, -np.pi/4, 0]
        )

    def key_event(self, key, delta_time):
        if key == 262: self.angles[1] += 2*delta_time #Seta para direita (vira para a direita)
        if key == 263: self.angles[1] -= 2*delta_time #Seta para esquerda (vira para a esquerda)
        if key == 265: #Seta para cima (anda para frente)
            self.position[0] += delta_time*np.cos(self.angles[1] - np.pi/2)
            self.position[1] += delta_time*np.sin(self.angles[1] - np.pi/2)
            self.position[2] += delta_time*np.sin(self.angles[1] - np.pi/2)
