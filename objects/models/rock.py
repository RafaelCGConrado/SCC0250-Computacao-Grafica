from . import primitives

color_rock = (0.5, 0.5, 0.5)

rock = {
    "vertices": {
        #'monte' 1
        "hill11": primitives.esphere(0.3, x=0, y=0),
        "hill12": primitives.esphere(0.4, x=0.5, y=0),
        "hill13": primitives.esphere(0.4, x=0.5, y=-0.4),
        "hill14": primitives.esphere(0.4, x=0.8, y=-0.4),
        
        #'monte' 2
#        "hill21": primitives.esphere(0.3, x=-4.2, y=-1.0),
#        "hill22": primitives.esphere(0.4, x=-4.2, y=-1.2),
#        "hill23": primitives.esphere(0.4, x=-4.2, y=-1.4),
#        "hill24": primitives.esphere(0.4, x=-4.2, y=-1.4),
# #'monte' 3
#        "hill31": primitives.esphere(0.5, x=2.0, y=-3.5),
#        "hill32": primitives.esphere(0.6, x=2.5, y=-3.7),
#        "hill33": primitives.esphere(0.4, x=2.3, y=-4.0),
#        "hill34": primitives.esphere(0.3, x=2.8, y=-4.2),
#
#        #'monte' 4
#        "hill41": primitives.esphere(0.3, x=-3.6, y=1.4),
#        "hill42": primitives.esphere(0.5, x=-3.9, y=2.1),
#        "hill43": primitives.esphere(0.4, x=-4.0, y=2.5),
    },

    "color": {
        "hill11": (0.6, 0.6, 0.6),
        "hill12": (0.3, 0.3, 0.3),
        "hill13": (0.2, 0.2, 0.2),
        "hill14": (0.5, 0.5, 0.5),

#        "hill21": color_rock,
#        "hill22": color_rock,
#        "hill23": color_rock,
#        "hill24": color_rock,
#
#        "hill31": color_rock,
#        "hill32": color_rock,
#        "hill33": color_rock,
#        "hill34": color_rock,
#
#        "hill41": color_rock,
#        "hill42": color_rock,
#        "hill43": color_rock,
    }
}