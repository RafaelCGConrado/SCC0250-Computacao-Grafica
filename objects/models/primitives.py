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