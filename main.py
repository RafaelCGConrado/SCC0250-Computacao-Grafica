import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import glm
import math
from objects.spongebob import SpongeBob
from objects.patrick import Patrick
from objects.floor import Floor
from objects.hook1 import Hook1
from objects.hook2 import Hook2
from objects.hook3 import Hook3
from objects.coral import Coral
from objects.bubble import Bubble
from objects.rock import Rock
from objects.flower import Flower
from functools import partial

def init_window():
    glfw.init()
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
    window = glfw.create_window(700, 700, "Programa", None, None)

    if (window == None):
        print("Failed to create GLFW window")
        glfwTerminate()
        
    glfw.make_context_current(window)

    return window

def create_shader(code, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, code)

    return shader

def compile_shader(shader):
    glCompileShader(shader)
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(vertex).decode()
        print(error)
        raise RuntimeError(f"Erro de compilacao do {vertex} Shader")
 
#Carrega os objetos que serão utilizados/exibidos na cena
def load_objects():
    #Todos os objetos que compõe a cena
    objects = [
        SpongeBob(),
        Patrick(),
        Hook1(),
        Hook2(),
        Hook3(),
        Floor(),
        Coral(x=-0.15),
        Coral(x=0.4),
        Coral(x=0.9),
        Coral(x=1.4),
        Rock(x=-0.2, y=-0.1, z=0.5, angle=0, scale=0.2),
        Rock(x=-0.9, y=-0.4, z=0.2, angle=0.6, scale=0.2),
        Rock(x=-0.1, y=-0.5, z=0, angle=0.1, scale=0.2),
        Rock(x=0.6, y=-0.7, z=-0.5, angle=-0.8, scale=0.2),
        Flower(x=0.1, y=0.8, z=0, color=(0.5, 0.7, 0.0)),
        Flower(x=0.7, y=0.9, z=0, color=(1.0, 0.0, 0.0)),
        Flower(x=-0.9, y=0.5, z=0, color=(0.0, 0.0, 1.0)),
        Flower(x=-1, y=0.95, z=0, color=(0.5, 0.7, 0.0)),
        Flower(x=-0.6, y=0.8, z=0, color=(1.0, 0.0, 0.0)),
        Flower(x=0.6, y=0.5, z=0, color=(0.5, 0.7, 0.0)),
        Bubble(0.5),
        Bubble(0.7),
        Bubble(0.4),
        Bubble(1),
        Bubble(0.9),
    ]

    vertices_list = []
    for obj in objects:
        vertices_list = obj.load(vertices_list)

    return objects, vertices_list



def main():
    window = init_window()
    
    vertex_code = """
            attribute vec3 position;
            uniform mat4 mat_transformation;
            void main(){
                gl_Position = mat_transformation * vec4(position,1.0);
            }
            """


    fragment_code = """
            uniform vec4 color;
            void main(){
                gl_FragColor = color;
            }
            """

    #Requisita slots na GPU para o programa e shaders
    program = glCreateProgram()
    
    #Cria shaders para vertex e fragments
    vertex = create_shader(vertex_code, GL_VERTEX_SHADER)
    fragment = create_shader(fragment_code, GL_FRAGMENT_SHADER)
    
    #Compila os shaders criados anteriormente
    compile_shader(vertex)
    compile_shader(fragment)

    # Liga os shaders ao programa criado
    glAttachShader(program, vertex)
    glAttachShader(program, fragment)

    glLinkProgram(program)
    if not glGetProgramiv(program, GL_LINK_STATUS):
        print(glGetProgramInfoLog(program))
        raise RuntimeError('Linking error')
    glUseProgram(program)

    # Carrega objetos e listas de vértices
    objects, vertices_list = load_objects()

    vertices = np.zeros(len(vertices_list), [("position", np.float32, 3)])
    vertices['position'] = vertices_list
    
    # Upload dos dados para a GPU
    buffer_VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, buffer_VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
    stride = vertices.strides[0]
    offset = ctypes.c_void_p(0)
    loc_vertices = glGetAttribLocation(program, "position")
    glEnableVertexAttribArray(loc_vertices)
    glVertexAttribPointer(loc_vertices, 3, GL_FLOAT, False, stride, offset)

    loc_color = glGetUniformLocation(program, "color")

    draw_lines = False
    delta_time = 0

    def key_event(objects,window,key,scancode,action,mods):
        nonlocal draw_lines, delta_time

        #Tecla P -> Exibe na tela as malhas dos objetos
        if key == 80 and action == glfw.PRESS:
            draw_lines = not draw_lines

        for obj in objects:
            obj.key_event(key, delta_time)


    key_ev = partial(key_event, objects)
    glfw.set_key_callback(window,key_ev)

    glfw.show_window(window)
    # ### Loop principal da janela.

    glEnable(GL_DEPTH_TEST) ### importante para 3D
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    hold = True
    lastFrame = 0

    while not glfw.window_should_close(window):
        currentFrame = glfw.get_time()
        delta_time = currentFrame - lastFrame
        lastFrame = currentFrame
        
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
        glClearColor(0.2, 0.9, 1.0, 1.0)

        if draw_lines and hold:
            glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
        
        for obj in objects:
            obj.draw(program, loc_color, delta_time=delta_time)
        
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
