import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import glm
import math
from objects.spongebob import SpongeBob
from objects.floor import Floor

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

    # Request a program and shader slots from GPU
    program = glCreateProgram()
    
    vertex = create_shader(vertex_code, GL_VERTEX_SHADER)
    fragment = create_shader(fragment_code, GL_FRAGMENT_SHADER)
    
    compile_shader(vertex)
    compile_shader(fragment)

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
    floor = Floor()
    vertices_list = bob.load(vertices_list)
    vertices_list = floor.load(vertices_list)

    vertices = np.zeros(len(vertices_list), [("position", np.float32, 3)])
    vertices['position'] = vertices_list

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
    
    def key_event(window,key,scancode,action,mods):
        bob.key_event(key)
        floor.key_event(key)

    glfw.set_key_callback(window,key_event)

    glfw.show_window(window)

    # ### Loop principal da janela.

    glEnable(GL_DEPTH_TEST) ### importante para 3D

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
        glClearColor(0.2, 0.5, 1.0, 1.0)

        floor.draw(program, loc_color)
        bob.draw(program, loc_color)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
