# -*- coding: utf-8 -*-
"""
Advent of Code Day 3
Crossed Wires
@ttalikka
"""

import matplotlib.pyplot as plt

def get_coordinates(path):
    point = [0, 0]
    L = []
    L.append(tuple(point))
    for i in path:
        dir = i[0]
        val = int(i[1:])
        if dir == "R":
            point[0] += val
        elif dir == "L":
            point[0] -= val
        elif dir == "D":
            point[1] -= val
        elif dir == "U":
            point[1] += val
        L.append(tuple(point))
    return L

def get_x_coordinates(L):
    X = []
    for i in L:
        X.append(i[0])
    return X

def get_y_coordinates(L):
    Y = []
    for i in L:
        Y.append(i[1])
    return Y


def get_lines(L):
    lines = []
    for i in range(len(L)):
        if i == len(L)-1:
            break
        else:
            line = L[i],L[i+1]
            lines.append(line)
    return lines

def line_intersection(line1, line2):
    # Was too lazy to write my own formula for line-line intersection
    # Function from: https://stackoverflow.com/a/20677983
    # Holiday cheers to Paul Draper who wrote this!
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def taxi(collision):
    return abs(collision[0]) + abs(collision[1])

def get_steps(L):
    steps = []
    for i in L:
        steps.append(abs(i[0][0]-i[1][0])+abs(i[0][1]-i[1][1]))
    return steps

with open("input","r") as f:
    input = f.readlines()

path1 = input[0].split(",")
path2 = input[1].split(",")

L = get_coordinates(path1)
X = get_x_coordinates(L)
Y = get_y_coordinates(L)

L2 = get_coordinates(path2)
X2 = get_x_coordinates(L2)
Y2 = get_y_coordinates(L2)

lines1 = get_lines(L)
lines2 = get_lines(L2)
steps1 = get_steps(lines1)
steps2 = get_steps(lines2)

distances = []
combined_steps = []

for i in lines1:
    for n in lines2:
        intersect = line_intersection(i,n)
        if intersect == None:
            pass
        else:
            # Crudely checking that the lines actually cross, as the intersection routine
            # only checks if the lines intersect on infinite lines
            if n[0][0] in range(min(i[0][0],i[1][0]),max(i[0][0],i[1][0])) or i[0][0] in range(min(n[0][0],n[1][0]),max(n[0][0],n[1][0])):
                if n[0][1] in range(min(i[0][1],i[1][1]),max(i[0][1],i[1][1])) or i[0][1] in range(min(n[0][1],n[1][1]),max(n[0][1],n[1][1])):
                    if intersect[0] == 0.0 or intersect[1] == 0.0:
                        pass
                    else:
                        print("Collision at {}".format(intersect))
                        print("Manhattan distance: {}".format(taxi(intersect)))
                        print("Collision happened at line index {} (i) {} (n)".format(lines1.index(i),lines2.index(n)))
                        i_steps=steps1[:lines1.index(i)]
                        n_steps=steps2[:lines2.index(n)]
                        extra_i = int(abs(i[0][0]-intersect[0])+abs(i[0][1]-intersect[1]))
                        extra_n = int(abs(n[0][0]-intersect[0])+abs(n[0][1]-intersect[1]))
                        print("Steps to collision (i): {} plus extra {} (total {})".format(i_steps,extra_i,sum(i_steps)+extra_i))
                        print("Steps to collision (n): {} plus extra {} (total {})".format(n_steps,extra_n,sum(n_steps)+extra_n))
                        print("Total steps required: {}\n".format(sum(i_steps) + sum(n_steps) + extra_i + extra_n))
                        distances.append(taxi(intersect))
                        combined_steps.append(sum(i_steps) + sum(n_steps) + extra_i + extra_n)
                else:
                    pass
            else:
                pass

print(distances)
print(combined_steps)
            
plt.plot(X,Y,linewidth=1)
plt.plot(X2,Y2,linewidth=1)
plt.show()
