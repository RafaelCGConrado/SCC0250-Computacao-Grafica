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
            position=[0.5, -0.2, 0.2],
            angles=[-np.pi/4, -np.pi/4, 0]
        )

    def key_event(self, key):
        if key == 262: self.angles[1] += 0.05 #Seta para direita (vira para a direita)
        if key == 263: self.angles[1] -= 0.05 #Seta para esquerda (vira para a esquerda)
        
        if key == 265: #Seta para cima (anda para frente)
            self.position[0] += 0.01*np.cos(self.angles[1] - np.pi/2)
            self.position[1] += 0.01*np.sin(self.angles[1] - np.pi/2)
            self.position[2] += 0.01*np.sin(self.angles[1] - np.pi/2)
        
        #Limita o movimento do Patrick para que ele não avance sobre os limites da cena
        #Limite no eixo Y
        if self.position[1] >= 0:
            self.position[1] = 0

        #Caso ultrapasse o limite no eixo Z
        if self.position[2] >= 0:
            self.position[2] = 0
