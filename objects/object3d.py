from OpenGL.GL import *
import numpy as np
import math
from .utils import multiplica_matriz
import abc

class Object3d(object):
    def __init__(self, model, position=[0, 0], angles=[0, 0, 0], scale=0.2):    
        self.model = model

        self.init = {x: 0 for x in self.model}
        self.len = {x: 0 for x in self.model}
        self.angles = angles
        self.position = position
        self.scale = scale

    @abc.abstractmethod
    def key_event(self):
        return

    def load(self, vertices_list):
        for piece in self.model['vertices']:        
            self.init[piece] = len(vertices_list)

            for v in self.model['vertices'][piece]:
                vertices_list.append(v)

            self.len[piece] = len(vertices_list) - self.init[piece]
        return vertices_list

    def set_position(position):
        self.position = position
    
    def set_angle(angle):
        self.angles = angles
    
    def set_scale(scale):
        self.scale = scale 

    def draw(self, program, loc_color):
        cos_d_x = math.cos(self.angles[0])
        sin_d_x = math.sin(self.angles[0])
        cos_d_y = math.cos(self.angles[1])
        sin_d_y = math.sin(self.angles[1])
        
        mat_rotate_x = np.array([
            cos_d_x, -sin_d_x, 0, 0,
            sin_d_x, cos_d_x, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1,
        ], np.float32)
        
        mat_rotate_y = np.array([
            cos_d_y, 0, -sin_d_y, 0,
            0, 1, 0, 0,
            sin_d_y, 0, cos_d_y, 0,
            0, 0, 0, 1,
        ], np.float32)
        
        mat_scale = np.array([     self.scale,  0.0, 0.0,     0, 
                                        0.0,    self.scale,   0.0, 0, 
                                        0.0,    0.0,   0.2, 0.0, 
                                        0.0,    0.0,   0.0, 1.0], np.float32)

        mat_position = np.array([     1,  0.0, 0.0,     self.position[0], 
                                        0.0,    1,   0.0, self.position[1], 
                                        0.0,    0.0,   1, 0.0, 
                                        0.0,    0.0,   0.0, 1.0], np.float32)

        mat_transform = multiplica_matriz(mat_rotate_y, mat_rotate_x)
        mat_transform = multiplica_matriz(mat_scale, mat_transform)
        mat_transform = multiplica_matriz(mat_position, mat_transform)
        
        loc_transformation = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
        
        for piece in self.model['color']:
            rgb = self.model['color'][piece]
            glUniform4f(loc_color, rgb[0], rgb[1], rgb[2], 1.0) ### vermelho    
            glDrawArrays(GL_TRIANGLES, self.init[piece], self.len[piece])
    
