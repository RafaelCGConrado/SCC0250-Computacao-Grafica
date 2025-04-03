from OpenGL.GL import *
import numpy as np
import math
from .utils import multiplica_matriz
import abc


# Classe base para a criação de objetos
class Object3d(object):
    # Parâmetros
    #   model: dicionário com os vértices do modelo
    #   position: posição inicial do modelo
    #   angles: ângulos do objeto
    #   scale: escala do objeto
    def __init__(self, model, position=[0, 0, 0], angles=[0, 0, 0], scale=1):    
        self.model = model

        # Vértices iniciais das partes do modelo
        self.init = {x: 0 for x in self.model} 

        # Quantidade de vértices nas partes dos modelos
        self.len = {x: 0 for x in self.model}

        self.angles = angles.copy()
        self.position = position.copy()
        self.scale = scale

        # Matriz inicial de transformação
        self.mat_transform = np.array([
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        ], np.float32)

    # Classe abstrata para os eventos de teclado de cada objeto.
    # Parâmetros:
    #   key: variável do glfw que possui o código do botão pressionado.
    @abc.abstractmethod
    def key_event(self, key):
        return

    # Carrega os vétices para a lista de vértices de renderização
    # Parâmtros:
    #   vertices_list: lista de vértices que serão passados para serem exibidos
    def load(self, vertices_list):
        # Cada pedaço do modelo possui sua lista de vértices.
        # O loop passará por cada uma dessas partes e transfere
        # seus vértices para a lista principal de vértices de 
        # renderização.
        for piece in self.model['vertices']:        
            self.init[piece] = len(vertices_list)

            for v in self.model['vertices'][piece]:
                vertices_list.append(v)

            self.len[piece] = len(vertices_list) - self.init[piece]
        return vertices_list
    
    # Retorna a posição central do objetos
    def get_center(self):
        pieces = list(self.model['vertices'].values())
        y_list = [v[1] for vs in pieces for v in vs]
        return np.mean(y_list)

    # Renderiza o objeto, aplicando as transformações necessárias.
    # Parâmetros: 
    #   program: programa opengl alocado na gpu.
    #   loc_color: localização da variável de cor no fragment shader.
    #   draw_type: tipo de renderização dos polígonos.
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
        
        mat_scale = np.array([  
            self.scale, 0.0,    0.0,    0, 
            0.0,    self.scale, 0.0,    0, 
            0.0,    0.0,    self.scale, 0.0, 
            0.0,    0.0,    0.0, 1.0
        ], np.float32)

        mat_position = np.array([   
            1,      0.0,    0.0,    self.position[0], 
            0.0,    1,      0.0,    self.position[1], 
            0.0,    0.0,    1,      self.position[2], 
            0.0,    0.0,   0.0,     1.0
        ], np.float32)

        self.mat_transform = multiplica_matriz(mat_rotate_y, mat_rotate_z)
        self.mat_transform = multiplica_matriz(mat_rotate_x, self.mat_transform)
        self.mat_transform = multiplica_matriz(mat_scale, self.mat_transform)
        self.mat_transform = multiplica_matriz(mat_position, self.mat_transform)

        # Transfere a matriz final de transformação do vertex shader
        loc_transformation = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, self.mat_transform) 
        
        # Irá colorir cada pedaço do modelo.
        for piece in self.model['color']:
            rgb = self.model['color'][piece]
            glUniform4f(loc_color, rgb[0], rgb[1], rgb[2], 1.0)     
            glDrawArrays(draw_type, self.init[piece], self.len[piece])
    
