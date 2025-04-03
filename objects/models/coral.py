from . import primitives

coral_color = (0.7,0,0.7)

coral = {
    "vertices": {
        #"Montante" 1 -> Conjunto de pequenas pirâmides Concatenadas
        "coral1": primitives.piramid(0.6, 1.5, 0.4, x=-0.1, y =-0.3, z=2),
        "coral2": primitives.piramid(0.68, 1.0, 0.5, x=-0.12, y =-0.35, z=2.5),
        "coral3": primitives.piramid(0.9, 1.7, 0.6, x=-0.21, y =-0.5, z=2.8),
        "coral4": primitives.piramid(0.8, 1.9, 0.7, x=-0.8, y =-0.5, z=2.9),
        "coral5": primitives.piramid(0.7, 1.5, 0.4, x=-1.0, y =-0.4, z=3.4),
    },

    #Em relação as cores, optamos por oscilar para ter um efeito melhor de destaque
    "color": {
        "coral1": coral_color,
        "coral2": (0.5, 0, 0.5),
        "coral3": coral_color,
        "coral4": (0.5, 0, 0.5),
        "coral5": coral_color,
    }

}