from OpenGL.GL import *
import numpy as np
import math
from .utils import multiplica_matriz
import abc

class Object3d(object):
    def __init__(self, model, position=[0, 0, 0], angles=[0, 0, 0], scale=1):    
        self.model = model

        self.init = {x: 0 for x in self.model}
        self.len = {x: 0 for x in self.model}
        self.angles = angles.copy()
        self.position = position.copy()
        self.scale = scale

        self.mat_transform = np.array([
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        ], np.float32)

    @abc.abstractmethod
    def key_event(self, key):
        return

    def load(self, vertices_list):
        for piece in self.model['vertices']:        
            self.init[piece] = len(vertices_list)

            for v in self.model['vertices'][piece]:
                vertices_list.append(v)

            self.len[piece] = len(vertices_list) - self.init[piece]
        return vertices_list

    def get_center(self):
        pieces = list(self.model['vertices'].values())
        y_list = [v[1] for vs in pieces for v in vs]
        return np.mean(y_list)


    def draw(self, program, loc_color, draw_type=GL_TRIANGLE_STRIP):
        cos_d_x = math.cos(self.angles[0])
        sin_d_x = math.sin(self.angles[0])
        cos_d_y = math.cos(self.angles[1])
        sin_d_y = math.sin(self.angles[1])
        cos_d_z = math.cos(self.angles[2])
        sin_d_z = math.sin(self.angles[2])
        
        mat_rotate_z = np.array([
            cos_d_z, -sin_d_z, 0, 0,
            sin_d_z, cos_d_z, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1,
        ], np.float32)
        
        mat_rotate_y = np.array([
            cos_d_y, 0, -sin_d_y, 0,
            0, 1, 0, 0,
            sin_d_y, 0, cos_d_y, 0,
            0, 0, 0, 1,
        ], np.float32)

        mat_rotate_x = np.array([
            1, 0, 0, 0,
            0, cos_d_x, -sin_d_x, 0,
            0, sin_d_x, cos_d_x, 0,
            0, 0, 0, 1,
        ], np.float32)
        
        mat_scale = np.array([     self.scale,  0.0, 0.0,     0, 
                                        0.0,    self.scale,   0.0, 0, 
                                        0.0,    0.0,   self.scale, 0.0, 
                                        0.0,    0.0,   0.0, 1.0], np.float32)

        mat_position = np.array([     1,  0.0, 0.0, self.position[0], 
                                        0.0,    1,   0.0, self.position[1], 
                                        0.0,    0.0,   1, self.position[2], 
                                        0.0,    0.0,   0.0, 1.0], np.float32)

        self.mat_transform = multiplica_matriz(mat_rotate_y, mat_rotate_z)
        self.mat_transform = multiplica_matriz(mat_rotate_x, self.mat_transform)
        self.mat_transform = multiplica_matriz(mat_scale, self.mat_transform)
        self.mat_transform = multiplica_matriz(mat_position, self.mat_transform)

        loc_transformation = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, self.mat_transform) 
        
        for piece in self.model['color']:
            rgb = self.model['color'][piece]
            glUniform4f(loc_color, rgb[0], rgb[1], rgb[2], 1.0) ### vermelho    
            glDrawArrays(draw_type, self.init[piece], self.len[piece])
    
