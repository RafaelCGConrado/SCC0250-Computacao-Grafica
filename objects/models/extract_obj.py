import os

objects = {}

with open("bobesp.obj", "r") as f:
    curr_object = ""
    temp_verticies = []
    for line in f:
        if line.startswith("o "):
            curr_object = line[2:].strip()
            objects[curr_object] = []
        if line.startswith("v "):
            numbers = tuple([float(x) for x in line[2:].strip().split(" ")])
            temp_verticies.append(numbers)
        if line.startswith("f "):
            for num in [int(x) for x in line[2:].strip().split(" ")]:
                objects[curr_object].append(temp_verticies[num - 1])
