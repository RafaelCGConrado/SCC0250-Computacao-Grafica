from . import primitives

color_rock = (0.5, 0.5, 0.5)

rock = {
    "vertices": {
        "hill1": primitives.esphere(0.3, x=0.2, y=-2.6),
        "hill2": primitives.esphere(0.4, x=0.7, y=-2.6),
        "hill3": primitives.esphere(0.4, x=0.7, y=-3.0),
        "hill4": primitives.esphere(0.4, x=1.0, y=-3.0)
    },

    "color": {
        "hill1": color_rock,
        "hill2": color_rock,
        "hill3": color_rock,
        "hill4": color_rock
    }
}