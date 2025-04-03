import math
import numpy as np


#Retorna o conjunto de pontos que formam
#um quadrado.
#Parâmetros: w -> Comprimento da base (Width)
#            h -> Comprimento da altura (height)
#           x, y, z -> Coordenadas iniciais do objeto
def square(w, h, x=0, y=0):
    return rectangle(w, h, 0, x, y, 0)

#Retorna o conjunto de vértices que formam
#um retângulo
#Parâmetros: w -> Comprimento da Base
#            h -> Altura
#            d -> Profundidade (Depth)
#           x,y,z -> Coordenadas iniciais do objeto
def rectangle(w, h, d, x=0, y=0, z=0):
    w, h, d = w/2, h/2, d/2
    return [
            #Face 1
            (-w + x, -h + y, +d + z),
            (+w + x, -h + y, +d + z),
            (-w + x, +h + y, +d + z),
            (+w + x, +h + y, +d + z),

            #Face 2
            (+w + x, -h + y, +d + z),
            (+w + x, -h + y, -d + z),         
            (+w + x, +h + y, +d + z),
            (+w + x, +h + y, -d + z),
            
            #Face 3
            (+w + x, -h + y, -d + z),
            (-w + x, -h + y, -d + z),            
            (+w + x, +h + y, -d + z),
            (-w + x, +h + y, -d + z),

            #Face 4
            (-w + x, -h + y, -d + z),
            (-w + x, -h + y, +d + z),         
            (-w + x, +h + y, -d + z),
            (-w + x, +h + y, +d + z),

            #Face 5
            (-w + x, -h + y, -d + z),
            (+w + x, -h + y, -d + z),         
            (-w + x, -h + y, +d + z),
            (+w + x, -h + y, +d + z),
            
            #Face 6
            (-w + x, +h + y, +d + z),
            (+w + x, +h + y, +d + z),           
            (-w + x, +h + y, -d + z),
            (+w + x, +h + y, -d + z)]

#Retorna o conjunto de vértices que formam uma pirâmide
#Parâmetros: w -> Comprimento da Base
#            h -> Altura
#            d -> Profundidade (Depth)
#           x,y,z -> Coordenadas iniciais do objeto
def piramid(w, h, d, x=0, y=0, z=0):
    w, h, d = w / 2, h / 2, d / 2
    return [
        # Face 1 da Pirâmide (triângulo)
        (x + 0.0, y + h, z + 0.0),
        (x + w, y + 0.0, z - d),
        (x + w, y + 0.0, z + d),

        # Face 2 da Pirâmide (triângulo)
        (x + 0.0, y + h, z + 0.0),
        (x + w, y + 0.0, z + d),
        (x - w, y + 0.0, z + d),

        # Face 3 da Pirâmide (triângulo)
        (x + 0.0, y + h, z + 0.0),
        (x - w, y + 0.0, z + d),
        (x - w, y + 0.0, z - d),

        # Face 4 da Pirâmide (triângulo)
        (x + 0.0, y + h, z + 0.0),
        (x - w, y + 0.0, z - d),
        (x + w, y + 0.0, z - d),

        # Face 5 (base) da Pirâmide (quadrado)
        (x + w, y + 0.0, z + d),
        (x + w, y + 0.0, z - d),
        (x - w, y + 0.0, z + d),
        (x - w, y + 0.0, z - d),
    ]



# Retorna as coordenadas polares para gerar a esfera
# Parâmetros: u ->angulo de longitude
#             v -> angulo de latitude 
#             r -> raio da esfera
def F_Esphere(u,v,r):
    x = r*math.sin(v)*math.cos(u)
    y = r*math.sin(v)*math.sin(u)
    z = r*math.cos(v)
    return (x,y,z)


#Retorna o conjunto de vértices que representam a superfície da esfera
#Parâmetros:    r -> Raio da Esfera
#               x,y,z -> Posições iniciais da esfera
def esphere(r, x=0, y=0, z=0):
    PI = 3.141592
    num_sectors = 32  # Quantidade de sectors (longitude)
    num_stacks = 32  # Quantidade de stacks (latitude)

    sector_step = (PI * 2) / num_sectors  #Variam de 0 até 2π
    stack_step = PI / num_stacks  #Variam de 0 até π

    vertices_list = []
    for i in range(0, num_sectors):  #Para cada sector (longitude)
        for j in range(0, num_stacks):  #Para cada stack (latitude)
            u = i * sector_step  #angulo do setor
            v = j * stack_step  #angulo do stack

            un = 0  # angulo do proximo sector
            if i + 1 == num_sectors:
                un = PI * 2
            else:
                un = (i + 1) * sector_step

            vn = 0  # angulo do proximo stack
            if j + 1 == num_stacks:
                vn = PI
            else:
                vn = (j + 1) * stack_step

            #Define os vértices do polígono
            p0 = F_Esphere(u, v, r)
            p1 = F_Esphere(u, vn, r)
            p2 = F_Esphere(un, v, r)
            p3 = F_Esphere(un, vn, r)

            #Adiciona deslocamento (x, y, z) para cada vértice
            p0 = (p0[0] + x, p0[1] + y, p0[2] + z)
            p1 = (p1[0] + x, p1[1] + y, p1[2] + z)
            p2 = (p2[0] + x, p2[1] + y, p2[2] + z)
            p3 = (p3[0] + x, p3[1] + y, p3[2] + z)

            #Triangulo 1 (primeira parte do poligono)
            vertices_list.append(p0)
            vertices_list.append(p2)
            vertices_list.append(p1)

            #Triangulo 2 (segunda e ultima parte do poligono)
            vertices_list.append(p3)
            vertices_list.append(p1)
            vertices_list.append(p2)

    return vertices_list