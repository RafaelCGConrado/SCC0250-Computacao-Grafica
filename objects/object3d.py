from OpenGL.GL import *
import numpy as np
import math
from .utils import multiplica_matriz
import abc

#Classe para desenhar todos os Objetos 3D que compõe a cena
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

        #Cada objeto possui sua própria matriz de transformação
        # que é iniciada como uma matriz identidade
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

    #'Carrega' o objeto a partir da lista de vértices que o compõe
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

    #Determina o centroide do objeto
    def get_center(self):
        pieces = list(self.model['vertices'].values())
        y_list = [v[1] for vs in pieces for v in vs]
        return np.mean(y_list)

    #Desenha o objeto na cena a partir das definicoes anteriores
    #Utilizamos GL_TRIANGLE_STRIP para desenhar o objeto por meio
    #de triangulos menores
    def draw(self, program, loc_color, draw_type=GL_TRIANGLE_STRIP):
        cos_d_x = math.cos(self.angles[0])
        sin_d_x = math.sin(self.angles[0])
        cos_d_y = math.cos(self.angles[1])
        sin_d_y = math.sin(self.angles[1])
        cos_d_z = math.cos(self.angles[2])
        sin_d_z = math.sin(self.angles[2])
        
        #Define a matriz de rotação do objeto no eixo Z
        mat_rotate_z = np.array([
            cos_d_z, -sin_d_z, 0, 0,
            sin_d_z, cos_d_z, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1,
        ], np.float32)
        
        #Matriz de Rotação ao redor do eixo Y
        mat_rotate_y = np.array([
            cos_d_y, 0, -sin_d_y, 0,
            0, 1, 0, 0,
            sin_d_y, 0, cos_d_y, 0,
            0, 0, 0, 1,
        ], np.float32)

        #Matriz de rotação ao redor de X
        mat_rotate_x = np.array([
            1, 0, 0, 0,
            0, cos_d_x, -sin_d_x, 0,
            0, sin_d_x, cos_d_x, 0,
            0, 0, 0, 1,
        ], np.float32)
        
        #Matriz de Escala do objeto
        mat_scale = np.array([     self.scale,  0.0, 0.0,     0, 
                                        0.0,    self.scale,   0.0, 0, 
                                        0.0,    0.0,   self.scale, 0.0, 
                                        0.0,    0.0,   0.0, 1.0], np.float32)

        #Matriz de translação para a posição inicial do objeto
        mat_position = np.array([     1,  0.0, 0.0, self.position[0], 
                                        0.0,    1,   0.0, self.position[1], 
                                        0.0,    0.0,   1, self.position[2], 
                                        0.0,    0.0,   0.0, 1.0], np.float32)

        #Realiza a multiplicação das matrizes e transforma o objeto
        #até a posicao desejada
        self.mat_transform = multiplica_matriz(mat_rotate_y, mat_rotate_z)
        self.mat_transform = multiplica_matriz(mat_rotate_x, self.mat_transform)
        self.mat_transform = multiplica_matriz(mat_scale, self.mat_transform)
        self.mat_transform = multiplica_matriz(mat_position, self.mat_transform)

        # Transfere a matriz final de transformação do vertex shader
        loc_transformation = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, self.mat_transform) 
        
        #Desenha os objetos na cor desejada
        for piece in self.model['color']:
            rgb = self.model['color'][piece]
            alpha = rgb[3] if len(rgb) == 4 else 1.0
            glUniform4f(loc_color, rgb[0], rgb[1], rgb[2], alpha)     
            glDrawArrays(draw_type, self.init[piece], self.len[piece])
    
