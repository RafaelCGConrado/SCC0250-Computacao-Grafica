import numpy as np
import abc
from . import object3d
from .models.patrick import patrick


class Patrick(object3d.Object3d):
    def __init__(self):
        super().__init__(model=patrick, scale=0.3, position=[0,0,0], angles=[0,0,0])

    def key_event(self, key):
        if (key==10):
            print('a') 
 
