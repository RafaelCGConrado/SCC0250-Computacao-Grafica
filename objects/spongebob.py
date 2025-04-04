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
            position=[-0.5, -0.1, -0.5],
            scale=0.3, 
            angles=[-np.pi/4, np.pi/4, 0]
        )

<<<<<<< HEAD

<<<<<<< HEAD
    def key_event(self, key, delta_time):
=======
    def key_event(self, key):
>>>>>>> parent of 651dcc6 (delta_time)
        if key == 88: #Tecla X -> Aumenta de tamanho
            self.scale += 0.01
            self.position[1] += 0.01
        if key == 90:  #Tecla Z -> Diminui de tamanho
            self.scale -= 0.01
            self.position[1] -= 0.01

        print(self.position[1])

=======
>>>>>>> parent of c4a0ded (More z ajustments and limit spongebob scale)
        #Abaixo, definimos limites para aumento e diminuição do objeto.
        #Não queremos que ele fique grande demais (e ocupe toda a cena) 
        # ou pequeno demais (e desapareça)

        #Se a escala é superior a 0.7, seu crescimento é interrompido
        #e ele agora pode apenas diminuir
        if self.scale >= 0.7 and self.position[1] >= 0.3:
            self.scale = 0.7
            self.position[1] = 0.3
        

        #Se é inferior a 0.06, sua diminuição também é interrompida.
        if self.scale <= 0.06 and self.position[1] <= -0.34:
            self.scale = 0.06
            self.position[1] = -0.34
 
