import numpy as np
import abc
from . import object3d
from .models.spongebob import sponge_bob

#Classe para o Bob Esponja. Esse personagem aumenta ou diminui de tamanho (escala),
#afinal de contas é uma esponja e pode absorver água.
class SpongeBob(object3d.Object3d):
    def __init__(self):
        super().__init__(
            model=sponge_bob,
            position=[-0.5, 0, 0],
            scale=0.3, 
            angles=[-np.pi/4, np.pi/4, 0]
        )

    def key_event(self, key, delta_time):
        if key == 88: #Tecla X -> Aumenta de tamanho
            self.scale += delta_time
            self.position[1] += delta_time
        if key == 90:  #Tecla Z -> Diminui de tamanho
            self.scale -= delta_time
            self.position[1] -= 0.01*delta_time

        # print(self.position[1])

        #Abaixo, definimos limites para aumento e diminuição do objeto.
        #Não queremos que ele fique grande demais (e ocupe toda a cena) 
        # ou pequeno demais (e desapareça)
        #Se a escala é superior a 0.5, seu crescimento é interrompido
        #e ele agora pode apenas diminuir
        if self.scale >= 0.5 and self.position[1] >= 0.2:
            self.scale = 0.5
            self.position[1] = 0.2
        

        #Se é inferior a 0.06, sua diminuição também é interrompida.
        if self.scale <= 0.06 and self.position[1] <= -0.24:
            self.scale = 0.06
            self.position[1] = -0.24
 

