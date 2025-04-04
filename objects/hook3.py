from . import object3d
from .models.hook1 import hook1
import math

#Terceiro Anzol da cena. Dessa vez, o usuário pode
#controlar sua oscilação via teclado.
class Hook3(object3d.Object3d):
    def __init__(self):
        self.ocilate = 0
        super().__init__(
            model=hook1,
            position=[-0.3, 0.6, 0]
        )

    def key_event(self, key, delta_time):
        if key == 65: self.position[1] -= 0.01 #Tecla A -> Desce o anzol no eixo Y
        if key == 81: self.position[1] += 0.01 #Tecla Q -> Sobe o anzol no eixo Y
        
        #Abaixo, definimos limites para a oscilação do anzol; Não queremos que ele suba demais
        #e desapareça da cena, e nem que desça demais e ultrapasse o chão.
        
        #Se a posição em Y é menor ou igual a 0, mantemos em 0
        if self.position[1] <= 0:
            self.position[1] = 0

        #Se a posição em Y é maior do que 1.22, mantemos em 1.22
        elif self.position[1] >= 1.22:
            self.position[1] = 1.22