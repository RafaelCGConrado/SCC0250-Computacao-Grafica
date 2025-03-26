from . import primitives
import math
body_color = (1,0,1)
pants_color = (144/238, 1, 144/238)

patrick = {
    "vertices": {
        "body": primitives.piramid(0.8, 3.0, 0.4, y=0.2),  
        "arm1": primitives.rectangle(0.1, 0.8, 0.1, x=-0.40, y=-0.1), 
        "arm2": primitives.rectangle(0.1, 0.8, 0.1, x=0.40, y=-0.1),
        "leg1": primitives.rectangle(0.1, 0.8, 0.1, x=0.25, y=-0.5),  
        "leg2": primitives.rectangle(0.1, 0.8, 0.1, x=-0.25, y=-0.5)
       # "pants": primitives.tronco_piramid(0.8, 0.5, 0.4, 0.5, 1.5,y=0.2)  
    },

    "color": {
        "body": body_color,
        "arm1": body_color,
        "arm2": body_color,
        "leg1": body_color,
        "leg2": body_color
       # "pants": pants_color
    }
}