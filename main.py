import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import glm
import math
from sponge import SpongeBob

def bind_verticies_from_model(verticies_list, model_verticies):
    init = len(verticies_list)

    for v in model_verticies:
        verticies_list.append(v)

    return verticies_list

def main():
    glfw.init()
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE);
    window = glfw.create_window(700, 700, "Programa", None, None)

    if (window == None):
        print("Failed to create GLFW window")
        glfwTerminate()
        
    glfw.make_context_current(window)

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

    # Request a program and shader slots from GPU
    program  = glCreateProgram()
    vertex   = glCreateShader(GL_VERTEX_SHADER)
    fragment = glCreateShader(GL_FRAGMENT_SHADER)

    # Set shaders source
    glShaderSource(vertex, vertex_code)
    glShaderSource(fragment, fragment_code)

    # Compile shaders
    glCompileShader(vertex)
    if not glGetShaderiv(vertex, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(vertex).decode()
        print(error)
        raise RuntimeError("Erro de compilacao do Vertex Shader")

    glCompileShader(fragment)
    if not glGetShaderiv(fragment, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(fragment).decode()
        print(error)
        raise RuntimeError("Erro de compilacao do Fragment Shader")

    # Attach shader objects to the program
    glAttachShader(program, vertex)
    glAttachShader(program, fragment)

    glLinkProgram(program)
    if not glGetProgramiv(program, GL_LINK_STATUS):
        print(glGetProgramInfoLog(program))
        raise RuntimeError('Linking error')
        
    glUseProgram(program)

    vertices_list = []

    # Load Object
    bob = SpongeBob()
    bob.load(vertices_list)

    vertices = np.zeros(len(vertices_list), [("position", np.float32, 3)])
    vertices['position'] = vertices_list

    print(vertices_list)

    buffer_VBO = glGenBuffers(1)

    # Upload data
    glBindBuffer(GL_ARRAY_BUFFER, buffer_VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
    stride = vertices.strides[0]
    offset = ctypes.c_void_p(0)
    loc_vertices = glGetAttribLocation(program, "position")
    glEnableVertexAttribArray(loc_vertices)
    glVertexAttribPointer(loc_vertices, 3, GL_FLOAT, False, stride, offset)

    loc_color = glGetUniformLocation(program, "color")
    
    # incrementos para translacao
    x_inc = 0.0
    y_inc = 0.0

    # incrementos para rotacao
    r_inc = 0.0

    # coeficiente de escala
    s_inc = 1.0


    def key_event(window,key,scancode,action,mods):
        global x_inc, y_inc, r_inc, s_inc
        
        if key == 263: x_inc -= 0.0001 #esquerda
        if key == 262: x_inc += 0.0001 #direita

        if key == 265: y_inc += 0.0001 #cima
        if key == 264: y_inc -= 0.0001 #baixo
            
        if key == 65: r_inc += 0.1 #letra a
        if key == 83: r_inc -= 0.1 #letra s
            
        if key == 90: s_inc += 0.1 #letra z
        if key == 88: s_inc -= 0.1 #letra x
            
    glfw.set_key_callback(window,key_event)

    glfw.show_window(window)

    # ### Loop principal da janela.

    glEnable(GL_DEPTH_TEST) ### importante para 3D

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
        glClearColor(1.0, 1.0, 1.0, 1.0)

        bob.draw(program, loc_color)
        
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
