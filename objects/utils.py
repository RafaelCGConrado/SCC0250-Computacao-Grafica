import numpy as np

#Realiza a multiplicação de duas matrizes a e b
#É importante para realizar todas as transformações (rotacao e translacao)
#dos objetos da cena.
def multiplica_matriz(a,b):
    m_a = a.reshape(4,4)
    m_b = b.reshape(4,4)
    m_c = np.dot(m_a,m_b)
    c = m_c.reshape(1,16)
    return c

