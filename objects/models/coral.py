from . import primitives
# patrick = {
#     "vertices": {
#         "body": primitives.piramid(0.8, 3.0, 0.8, y=0.2),  
#         "arm1": primitives.rectangle(0.1, 0.8, 0.1, x=-0.50, y=-0.1), 
#         "arm2": primitives.rectangle(0.1, 0.8, 0.1, x=0.50, y=-0.1),
#         "leg1": primitives.rectangle(0.1, 0.8, 0.1, x=0.25, y=-0.5),  
#         "leg2": primitives.rectangle(0.1, 0.8, 0.1, x=-0.25, y=-0.5),
#         "pants": primitives.rectangle(0.95, 0.2, 0.95, y=0.1)  
#     },

coral_color = (1,0,1)

coral = {
    "vertices": {
        #"montante" 1
        "coral1": primitives.piramid(0.6, 1.5, 0.4, x=-0.1, y =-0.3, z=2),
        "coral2": primitives.piramid(0.68, 1.0, 0.5, x=-0.12, y =-0.35, z=2.5),
        "coral3": primitives.piramid(0.9, 1.7, 0.6, x=-0.21, y =-0.5, z=2.8),
        "coral4": primitives.piramid(0.8, 1.9, 0.7, x=-0.8, y =-0.5, z=2.9),
        "coral5": primitives.piramid(0.7, 1.5, 0.4, x=-1.0, y =-0.4, z=3.4),

        # "coral6": primitives.piramid(0.6, 1.5, 0.4, x=3.1, y =-0.3, z=2),
        # "coral7": primitives.piramid(0.68, 1.0, 0.5, x=3.2, y =-0.35, z=7.3),
        # "coral8": primitives.piramid(0.9, 1.7, 0.6, x=-0.21, y =-0.5, z=2.8),
        # "coral9": primitives.piramid(0.8, 1.9, 0.7, x=-0.8, y =-0.5, z=2.9),
        # "coral10": primitives.piramid(0.7, 1.5, 0.4, x=-1.0, y =-0.4, z=3.4)
    },

    "color": {
        "coral1": coral_color,
        "coral2": coral_color,
        "coral3": coral_color,
        "coral4": coral_color,
       # "coral5": coral_color,
        #"coral6": coral_color
    }

}