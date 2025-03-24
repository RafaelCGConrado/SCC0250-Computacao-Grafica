import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math
from utils import multiplica_matriz

class Object3d():
    def __init__(self, model, position=(0, 0), angle=0):    
        #self.model = {'body': [(0.571431, 4.4702, -1.392401), (0.571431, 1.859953, -1.392401), (0.571431, 4.4702, 1.392401), (0.571431, 1.859953, 1.392401), (-0.571431, 4.4702, -1.392401), (-0.571431, 1.859953, -1.392401), (-0.571431, 4.4702, 1.392401), (-0.571431, 1.859953, 1.392401), (0.571431, 1.492484, -1.392401), (0.571431, 0.860696, -1.392401), (0.571431, 1.492484, 1.392401), (0.571431, 0.860696, 1.392401), (-0.571431, 1.492484, -1.392401), (-0.571431, 0.860696, -1.392401), (-0.571431, 1.492484, 1.392401), (-0.571431, 0.860696, 1.392401), (0.571431, 1.858779, -1.392401), (0.571431, 1.487587, -1.392401), (0.571431, 1.858779, 1.392401), (0.571431, 1.487587, 1.392401), (-0.571431, 1.858779, -1.392401), (-0.571431, 1.487587, -1.392401), (-0.571431, 1.858779, 1.392401), (-0.571431, 1.487587, 1.392401)], 'arm1': [(-0.105449, 3.026096, 1.368144), (-0.105449, 1.381176, 1.368144), (-0.105449, 3.026096, 1.576045), (-0.105449, 1.381176, 1.576045), (0.105432, 3.026096, 1.368144), (0.105432, 1.381176, 1.368144), (0.105432, 3.026096, 1.576045), (0.105432, 1.381176, 1.576045)], 'arm2': [(-0.105449, 3.026096, -1.395071), (-0.105449, 1.381176, -1.395072), (-0.105449, 3.026096, -1.602973), (-0.105449, 1.381176, -1.602973), (0.105432, 3.026096, -1.395071), (0.105432, 1.381176, -1.395072), (0.105432, 3.026096, -1.602973), (0.105432, 1.381176, -1.602973)], 'leg1': [(-0.105449, 0.866614, 0.580552), (-0.105449, -0.778306, 0.580552), (-0.105449, 0.866614, 0.788453), (-0.105449, -0.778306, 0.788453), (0.105432, 0.866614, 0.580552), (0.105432, -0.778306, 0.580552), (0.105432, 0.866614, 0.788453), (0.105432, -0.778306, 0.788453)], 'leg2': [(-0.105449, 0.866614, -0.580552), (-0.105449, -0.778306, -0.580552), (-0.105449, 0.866614, -0.788453), (-0.105449, -0.778306, -0.788453), (0.105432, 0.866614, -0.580552), (0.105432, -0.778306, -0.580552), (0.105432, 0.866614, -0.788453), (0.105432, -0.778306, -0.788453)]}
        self.model = model

        self.init = {x: 0 for x in self.model}
        self.len = {x: 0 for x in self.model}
        self.angle = angle
        self.position = position

    def load(self, vertices_list):
        for piece in self.model['vertices']:        
            self.init[piece] = len(vertices_list)

            for v in self.model['vertices'][piece]:
                vertices_list.append(v)

            self.len[piece] = len(vertices_list) - self.init[piece]
        return vertices_list


    def draw(self, program, loc_color):
        self.angle -= 0.01
        cos_d = math.cos(self.angle)
        sin_d = math.sin(self.angle)

        mat_rotate_x = np.array([
            cos_d, -sin_d, 0, 0,
            sin_d, cos_d, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1,
        ], np.float32)

        mat_scale = np.array([     0.2,  0.0, 0.0,     0, 
                                        0.0,    0.2,   0.0, 0, 
                                        0.0,    0.0,   0.2, 0.0, 
                                        0.0,    0.0,   0.0, 1.0], np.float32)

        mat_transform = np.array([     1,  0.0, 0.0,     0, 
                                        0.0,    1,   0.0, 0, 
                                        0.0,    0.0,   1, 0.0, 
                                        0.0,    0.0,   0.0, 1.0], np.float32)

        mat_transform = multiplica_matriz(mat_rotate_x, mat_transform)
        mat_transform = multiplica_matriz(mat_scale, mat_transform)
        
        loc_transformation = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
        
        for piece in self.model['color']:
            rgb = self.model['color'][piece]
            glUniform4f(loc_color, rgb[0], rgb[1], rgb[2], 1.0) ### vermelho    
            glDrawArrays(GL_TRIANGLES, self.init[piece], self.len[piece])
    
