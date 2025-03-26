import math
import numpy as np

def square(w, h, x=0, y=0):
    return rectangle(w, h, 0, x, y, 0)

def rectangle(w, h, d, x=0, y=0, z=0):
    w, h, d = w/2, h/2, d/2
    return [(-w + x, -h + y, +d + z),
            (+w + x, -h + y, +d + z),
            (-w + x, +h + y, +d + z),
            (+w + x, +h + y, +d + z),

            # w + xaceh + y2 dd + z Cubo
            (+w + x, -h + y, +d + z),
            (+w + x, -h + y, -d + z),         
            (+w + x, +h + y, +d + z),
            (+w + x, +h + y, -d + z),
            
            # w + xaceh + y3 dd + z Cubo
            (+w + x, -h + y, -d + z),
            (-w + x, -h + y, -d + z),            
            (+w + x, +h + y, -d + z),
            (-w + x, +h + y, -d + z),

            # w + xaceh + y4 dd + z Cubo
            (-w + x, -h + y, -d + z),
            (-w + x, -h + y, +d + z),         
            (-w + x, +h + y, -d + z),
            (-w + x, +h + y, +d + z),

            # w + xaceh + y5 dd + z Cubo
            (-w + x, -h + y, -d + z),
            (+w + x, -h + y, -d + z),         
            (-w + x, -h + y, +d + z),
            (+w + x, -h + y, +d + z),
            
            # w + xaceh + y6 dd + zubo
            (-w + x, +h + y, +d + z),
            (+w + x, +h + y, +d + z),           
            (-w + x, +h + y, -d + z),
            (+w + x, +h + y, -d + z)]


PI = 3.141592
r = 0.1 # raio
H = 0.9
num_sectors = 20 # qtd de sectors (longitude)
num_stacks = 20 # qtd de stacks (latitude)

# grid sectos vs stacks (longitude vs latitude)
sector_step = (PI*2)/num_sectors # variar de 0 até 2π
stack_step = H/num_stacks # variar de 0 até H

# Entrada: angulo de t, altura h, raio r
# Saida: coordenadas no cilindro
def CoordCone(t, h, base_r, H, x, y, z, tilt_angle=0):
    radius = base_r * (1 - h / H)  # raio diminui conforme a altura aumenta
    x = radius * math.cos(t) + x
    y = radius * math.sin(t) + y
    z = h + z
    
    # Aplicando a inclinação no eixo Y
    new_x = x * math.cos(tilt_angle) - z * math.sin(tilt_angle)
    new_z = x * math.sin(tilt_angle) + z * math.cos(tilt_angle)
    
    return (new_x, y, new_z)
def CoordCone(t, h, base_r, H, x, y, z, tilt_angle=0):
    radius = base_r * (1 - h / H)  # raio diminui conforme a altura aumenta
    x = radius * math.cos(t) + x
    y = h + y  # Alterar para que a altura seja aplicada no eixo Y
    z = radius * math.sin(t) + z
    
    # Aplicando a inclinação no eixo Z
    new_x = x * math.cos(tilt_angle) - y * math.sin(tilt_angle)
    new_y = x * math.sin(tilt_angle) + y * math.cos(tilt_angle)
    
    return (new_x, new_y, z)

def cone(r, h, num_sectors, num_stacks, x=0, y=0, z=0, tilt_angle=0):
    vertices_list = []
    sector_step = 2 * math.pi / num_sectors  # Passo para os setores
    stack_step = h / num_stacks  # Passo para as pilhas
    
    # Gerando as faces laterais
    for j in range(num_stacks):
        for i in range(num_sectors):
            u = i * sector_step
            v = j * stack_step
            un = (i + 1) * sector_step if i + 1 < num_sectors else 2 * math.pi
            vn = (j + 1) * stack_step if j + 1 < num_stacks else h
            
            p0 = CoordCone(u, v, r, h, x, y, z, tilt_angle)
            p1 = CoordCone(u, vn, r, h, x, y, z, tilt_angle)
            p2 = CoordCone(un, v, r, h, x, y, z, tilt_angle)
            p3 = CoordCone(un, vn, r, h, x, y, z, tilt_angle)
            
            # Triângulo lateral
            vertices_list.append(p0)
            vertices_list.append(p2)
            vertices_list.append(p1)
            
            if vn < h:
                vertices_list.append(p1)
                vertices_list.append(p3)
                vertices_list.append(p2)
    
    # Criando a base do cone
    for i in range(num_sectors):
        u = i * sector_step
        un = (i + 1) * sector_step if i + 1 < num_sectors else 2 * math.pi
        
        p0 = CoordCone(u, 0, r, h, x, y, z, tilt_angle)
        p1 = CoordCone(un, 0, r, h, x, y, z, tilt_angle)
        center = (x, y, z)  # Centro da base no novo local
        
        vertices_list.append(p0)
        vertices_list.append(p1)
        vertices_list.append(center)
    
    # Adicionando o vértice do topo
    topo = CoordCone(0, h, r, h, x, y, z, tilt_angle)
    for i in range(num_sectors):
        u = i * sector_step
        un = (i + 1) * sector_step if i + 1 < num_sectors else 2 * math.pi
        
        p0 = CoordCone(u, h - stack_step, r, h, x, y, z, tilt_angle)
        p1 = CoordCone(un, h - stack_step, r, h, x, y, z, tilt_angle)
        
        vertices_list.append(p0)
        vertices_list.append(p1)
        vertices_list.append(topo)
    
    return vertices_list