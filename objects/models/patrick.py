from . import primitives
import math

body_color = (1.0, 0.72, 0.87)
pants_color = (0, 1, 0)

patrick = {
    "vertices": {
        "body": primitives.piramid(0.8, 3.0, 0.8, y=0.2),  #tronco do patrick
        "arm1": primitives.rectangle(0.1, 0.8, 0.1, x=-0.50, y=-0.1), #braço esquerdo
        "arm2": primitives.rectangle(0.1, 0.8, 0.1, x=0.50, y=-0.1), #braço direito
        "leg1": primitives.rectangle(0.1, 0.8, 0.1, x=0.25, y=-0.5),  #perna esquerda
        "leg2": primitives.rectangle(0.1, 0.8, 0.1, x=-0.25, y=-0.5), #perna direita
        "pants": primitives.rectangle(0.95, 0.2, 0.95, y=0.1)  #calça do patrick
        #Escolhemos desenhar a calça como um retângulo porque ficou visualmente melhor do
        #que quando fizemos com tronco de piramide.
    },

    #Cores do patrick
    "color": {
        "body": body_color,
        "arm1": body_color,
        "arm2": body_color,
        "leg1": body_color,
        "leg2": body_color,
       "pants": pants_color
    }
}