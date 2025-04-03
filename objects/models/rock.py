from . import primitives

rock = {
    "vertices": {
        #'monte' 1
        #Os Montes de pedras são conjuntos de esferas
        #de diferentes raios concatenadas.
        "hill11": primitives.esphere(0.3, x=0, y=0),
        "hill12": primitives.esphere(0.4, x=0.5, y=0),
        "hill13": primitives.esphere(0.4, x=0.5, y=-0.4),
        "hill14": primitives.esphere(0.4, x=0.8, y=-0.4),
    },

    "color": {
        "hill11": (0.6, 0.6, 0.6),
        "hill12": (0.3, 0.3, 0.3),
        "hill13": (0.2, 0.2, 0.2),
        "hill14": (0.5, 0.5, 0.5)
    }
}