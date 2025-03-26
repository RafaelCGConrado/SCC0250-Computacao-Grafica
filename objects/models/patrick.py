from . import primitives
import math
body_color = (1,0,1)

patrick = {
    "vertices": {
        "body": primitives.cone(0.5, 1.4, 20, 20, y=0.2, tilt_angle=math.radians(90)),  
        "arm1": primitives.rectangle(0.1, 0.8, 0.1, x=-0.55, y=0.6), 
        "arm2": primitives.rectangle(0.1, 0.8, 0.1, x=0.55, y=0.6),
        "leg1": primitives.rectangle(0.1, 0.8, 0.1, x=0.25, y=-0.7),  
        "leg2": primitives.rectangle(0.1, 0.8, 0.1, x=-0.25, y=-0.7)  
    },

    "color": {
        "body": body_color,
        "arm1": body_color,
        "arm2": body_color,
        "leg1": body_color,
        "leg2": body_color
    }
}